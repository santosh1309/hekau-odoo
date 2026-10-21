import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";

/**
 * Hekau Project List block: the category pills filter the project cards
 * (`data-filter` on a pill matches `data-category` on a card). Clicking the
 * active pill again shows every project.
 */
export class HekauProjectFilter extends Interaction {
    static selector = ".s_hk_project_list";
    dynamicContent = {
        ".hk-filter-pill": {
            "t-on-click": this.onPillClick,
            "t-att-aria-pressed": (el) => String(el.dataset.filter === this.active),
        },
        ".hk-work-card": {
            "t-att-class": (el) => ({
                "hk-filtered-out": !!this.active && el.dataset.category !== this.active,
            }),
        },
    };

    setup() {
        this.active = null;
    }

    onPillClick(ev) {
        const key = ev.currentTarget.dataset.filter;
        this.active = this.active === key ? null : key;
    }
}

registry.category("public.interactions").add("website_hekau.project_filter", HekauProjectFilter);
