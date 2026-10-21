import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";

/**
 * Hekau Testimonials block (desktop): the arrow buttons scroll the
 * horizontal card track by one card and are disabled at either end.
 */
export class HekauTestimonials extends Interaction {
    static selector = ".s_hk_testimonials";
    dynamicContent = {
        ".hk-arrow-prev": {
            "t-on-click": () => this.scrollByCard(-1),
            "t-att-disabled": () => this.atStart,
        },
        ".hk-arrow-next": {
            "t-on-click": () => this.scrollByCard(1),
            "t-att-disabled": () => this.atEnd,
        },
        ".hk-quotes": {
            // The debounced helper refreshes dynamicContent itself.
            "t-on-scroll.noUpdate": () => this.onScroll(),
        },
    };

    setup() {
        this.track = this.el.querySelector(".hk-quotes");
        this.onScroll = this.debounced(this.computeEdges, 50);
        this.computeEdges();
    }

    scrollByCard(direction) {
        const card = this.track?.querySelector(".hk-quote");
        if (!card) {
            return;
        }
        const gap = parseFloat(getComputedStyle(this.track).columnGap) || 0;
        this.track.scrollBy({ left: direction * (card.offsetWidth + gap), behavior: "smooth" });
    }

    computeEdges() {
        if (!this.track) {
            this.atStart = this.atEnd = true;
            return;
        }
        const { scrollLeft, scrollWidth, clientWidth } = this.track;
        this.atStart = scrollLeft <= 1;
        this.atEnd = scrollLeft + clientWidth >= scrollWidth - 1;
    }
}

registry.category("public.interactions").add("website_hekau.testimonials", HekauTestimonials);
