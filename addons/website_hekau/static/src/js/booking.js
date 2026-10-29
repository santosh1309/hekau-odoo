import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";

/**
 * Hekau Booking block: Calendly's booking calendar, loaded when the block
 * comes near the screen (Calendly's script is only fetched on pages that
 * show it). What the visitor typed in the contact form is remembered for the
 * session and filled in, so booking from the thank-you page is one click.
 * Without JavaScript, or if Calendly can't load, the block keeps its link.
 */
const PREFILL_KEY = "hk_booking_prefill";
const WIDGET_JS = "https://assets.calendly.com/assets/external/widget.js";

let widgetPromise = null;

function loadWidget() {
    if (window.Calendly) {
        return Promise.resolve(window.Calendly);
    }
    if (!widgetPromise) {
        widgetPromise = new Promise((resolve, reject) => {
            const script = document.createElement("script");
            script.src = WIDGET_JS;
            script.async = true;
            script.onload = () => (window.Calendly ? resolve(window.Calendly) : reject(new Error("Calendly")));
            script.onerror = () => {
                widgetPromise = null;
                reject(new Error("Calendly"));
            };
            document.head.appendChild(script);
        });
    }
    return widgetPromise;
}

function readPrefill() {
    try {
        return JSON.parse(window.sessionStorage.getItem(PREFILL_KEY) || "null");
    } catch {
        return null;
    }
}

export class HekauBooking extends Interaction {
    static selector = ".s_hk_booking";

    setup() {
        this.embed = this.el.querySelector(".hk-booking-embed");
        this.mounted = false;
    }

    start() {
        if (!this.embed || !this.embed.dataset.url) {
            return;
        }
        if (!("IntersectionObserver" in window)) {
            this.mount();
            return;
        }
        const observer = new IntersectionObserver(
            (entries) => {
                if (entries.some((entry) => entry.isIntersecting)) {
                    observer.disconnect();
                    this.mount();
                }
            },
            { rootMargin: "400px 0px" }
        );
        observer.observe(this.embed);
        this.registerCleanup(() => observer.disconnect());
    }

    async mount() {
        if (this.mounted) {
            return;
        }
        this.mounted = true;
        let Calendly;
        try {
            Calendly = await this.waitFor(loadWidget());
        } catch {
            return; // the fallback link stays
        }
        const data = readPrefill() || {};
        const notes = [
            data.company && `Company: ${data.company}`,
            data.service && `Interested in: ${data.service}`,
            data.notes,
        ].filter(Boolean).join("\n");
        const prefill = {};
        if (data.name) {
            prefill.name = data.name;
        }
        if (data.email) {
            prefill.email = data.email;
        }
        if (notes) {
            prefill.customAnswers = { a1: notes };
        }
        // Calendly reads the details from the booking link itself; encoded
        // with encodeURIComponent (URLSearchParams' "+" for spaces would show
        // up as "+" in Calendly's form).
        const params = { primary_color: "2d29df", name: prefill.name, email: prefill.email, a1: notes };
        const query = Object.entries(params)
            .filter(([, value]) => value)
            .map(([key, value]) => `${key}=${encodeURIComponent(value)}`)
            .join("&");
        const base = this.embed.dataset.url;
        const url = `${base}${base.includes("?") ? "&" : "?"}${query}`;
        // Leave the page as it was when the interaction stops (e.g. the website
        // builder opens), so Calendly's iframe is never saved into the page.
        const fallback = [...this.embed.childNodes];
        this.removeChildren(this.embed);
        this.embed.classList.add("hk-booking-loaded");
        this.registerCleanup(() => {
            [...this.embed.childNodes].filter((node) => !fallback.includes(node)).forEach((node) => node.remove());
            this.embed.classList.remove("hk-booking-loaded");
        });
        Calendly.initInlineWidget({
            url,
            parentElement: this.embed,
            prefill,
            utm: { utmSource: "website", utmMedium: "booking-calendar", utmContent: window.location.pathname },
        });
    }
}

/**
 * Contact form: remember the answers for the booking calendar on the
 * thank-you page (sessionStorage only: never sent anywhere by this code).
 */
export class HekauBookingPrefill extends Interaction {
    static selector = ".s_hk_contact form";
    dynamicContent = {
        ".s_website_form_send": { "t-on-click": this.remember },
    };

    remember() {
        const form = new FormData(this.el);
        const get = (name) => (form.get(name) || "").toString().trim();
        const data = {
            name: get("contact_name"),
            email: get("email_from"),
            company: get("partner_name"),
            service: get("Service needed"),
            notes: get("description"),
        };
        try {
            window.sessionStorage.setItem(PREFILL_KEY, JSON.stringify(data));
        } catch {
            // private mode or storage blocked: the calendar just starts empty
        }
    }
}

registry
    .category("public.interactions")
    .add("website_hekau.booking", HekauBooking)
    .add("website_hekau.booking_prefill", HekauBookingPrefill);
