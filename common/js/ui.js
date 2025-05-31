import { Pane } from 'https://cdn.jsdelivr.net/npm/tweakpane@4.0.5/dist/tweakpane.min.js';

export function setupUI(pyodide) {
    console.log("Tweakpane loaded.");
    const pane = new Pane();

    const params = { gravity: 0.0 };

    // The new API for adding inputs:
    pane.addBinding(params, 'gravity', { min: 0.0, max: 9.8 })
        .on('change', (ev) => {
            pyodide.runPython(`set_gravity(${ev.value})`);
        });

    pane.element.style.position = "absolute";
    pane.element.style.top = "20px";
    pane.element.style.left = "20px";
    pane.element.style.zIndex = 999;
}
