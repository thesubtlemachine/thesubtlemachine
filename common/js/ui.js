export function setupUI(pyodide) {
    const pane = new Tweakpane.Pane();
    const params = { gravity: 0.0 };
    pane.addInput(params, 'gravity', { min: 0.0, max: 9.8 })
        .on('change', (ev) => {
            pyodide.runPython(`set_gravity(${ev.value})`);
        });
}