import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";

/**
 * Main menu: Odoo marks the item that links to the current page (`.active`).
 * This also marks the item a page sits under: /projects/<case study> under
 * Projects, /blog/<post> under Blog, and pages whose #wrap carries
 * data-hk-menu (the service pages say "/services").
 */
export class HekauMenuActive extends Interaction {
    static selector = "header#top";

    start() {
        const path = window.location.pathname.replace(/\/+$/, "") || "/";
        const section = document.querySelector("#wrap[data-hk-menu]")?.dataset.hkMenu;
        const links = [...this.el.querySelectorAll("ul.top_menu a.nav-link[href]")];
        if (links.some((link) => link.classList.contains("active"))) {
            return;
        }
        const added = [];
        for (const link of links) {
            const href = (link.getAttribute("href") || "").replace(/\/+$/, "");
            if (!href.startsWith("/") || href === "") {
                continue;
            }
            if (href === section || path.startsWith(href + "/")) {
                link.classList.add("active");
                link.setAttribute("aria-current", "page");
                added.push(link);
            }
        }
        this.registerCleanup(() => {
            for (const link of added) {
                link.classList.remove("active");
                link.removeAttribute("aria-current");
            }
        });
    }
}

registry.category("public.interactions").add("website_hekau.menu_active", HekauMenuActive);
