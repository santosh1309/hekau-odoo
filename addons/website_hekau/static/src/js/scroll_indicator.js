import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";

/**
 * Figma mobile scroll indicator: a 100x2 track whose 20px thumb follows the
 * horizontal scroll position of the `.hk-scroller` placed just before it.
 * Used by every Hekau block with swipeable cards (why-cards, testimonials).
 */
export class HekauScrollIndicator extends Interaction {
    static selector = ".hk-scroller";
    dynamicContent = {
        _root: {
            "t-on-scroll.noUpdate": () => this.update(),
        },
        _window: {
            "t-on-resize.noUpdate": () => this.update(),
        },
    };

    setup() {
        const next = this.el.nextElementSibling;
        this.indicator = next?.classList.contains("hk-scroll-indicator") ? next : null;
    }

    start() {
        this.update();
    }

    update() {
        if (!this.indicator) {
            return;
        }
        const { scrollLeft, scrollWidth, clientWidth } = this.el;
        const range = scrollWidth - clientWidth;
        const progress = range > 0 ? Math.min(1, Math.max(0, scrollLeft / range)) : 0;
        this.indicator.style.setProperty("--hk-progress", progress.toFixed(3));
    }

    destroy() {
        this.indicator?.style.removeProperty("--hk-progress");
    }
}

registry.category("public.interactions").add("website_hekau.scroll_indicator", HekauScrollIndicator);
