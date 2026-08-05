(() => {
    const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)");
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    const reticle = document.querySelector(".cursor-reticle");

    if (!reticle) {
        return;
    }

    const coordinates = reticle.querySelector(".cursor-coordinates");
    const interactiveSelector = "a, button, input, textarea, select, summary, [role='button']";

    let pointerX = 0;
    let pointerY = 0;
    let frameId = null;
    let enabled = false;

    const shouldEnable = () => finePointer.matches && !reducedMotion.matches;

    const render = () => {
        reticle.style.transform = `translate3d(${pointerX - 8}px, ${pointerY - 8}px, 0)`;

        if (coordinates) {
            coordinates.textContent = `x: ${Math.round(pointerX)}, y: ${Math.round(pointerY)}`;
        }

        frameId = null;
    };

    const requestRender = () => {
        if (frameId === null) {
            frameId = window.requestAnimationFrame(render);
        }
    };

    const handlePointerMove = (event) => {
        if (!enabled) {
            return;
        }

        pointerX = event.clientX;
        pointerY = event.clientY;
        reticle.classList.toggle("is-targeting", Boolean(event.target.closest(interactiveSelector)));
        requestRender();
    };

    const setEnabled = () => {
        enabled = shouldEnable();
        document.body.classList.toggle("custom-cursor-enabled", enabled);
        reticle.setAttribute("aria-hidden", "true");

        if (!enabled) {
            reticle.classList.remove("is-targeting");
            reticle.style.transform = "translate3d(-999px, -999px, 0)";
        }
    };

    setEnabled();
    window.addEventListener("pointermove", handlePointerMove, { passive: true });
    finePointer.addEventListener("change", setEnabled);
    reducedMotion.addEventListener("change", setEnabled);
})();
