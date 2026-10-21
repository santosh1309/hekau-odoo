import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";

/**
 * Hekau Process block: steps light up (blue number, filled bar) once they
 * scroll past 60% of the screen height, so the timeline fills as the visitor
 * reads down. Hover/focus is handled in CSS.
 */
export class HekauProcess extends Interaction {
    static selector = ".s_hk_process";
    dynamicContent = {
        _window: {
            "t-on-scroll.noUpdate": () => this.schedule(),
            "t-on-resize.noUpdate": () => this.schedule(),
        },
    };

    setup() {
        this.steps = [...this.el.querySelectorAll(".hk-step")];
        this.frame = null;
    }

    start() {
        this.update();
    }

    schedule() {
        if (this.frame === null) {
            this.frame = requestAnimationFrame(() => {
                this.frame = null;
                this.update();
            });
        }
    }

    update() {
        const line = window.innerHeight * 0.6;
        for (const step of this.steps) {
            step.classList.toggle("hk-active", step.getBoundingClientRect().top < line);
        }
    }

    destroy() {
        if (this.frame !== null) {
            cancelAnimationFrame(this.frame);
        }
        for (const step of this.steps) {
            step.classList.remove("hk-active");
        }
    }
}

registry.category("public.interactions").add("website_hekau.process", HekauProcess);
