import { initPyodideAndPackages } from '../../../common/js/pyodide-bridge.js';
import { createScene } from './renderer.js';
import { setupUI } from './ui.js';

let pyodide;
const particleCount = 1000;

async function main() {
    pyodide = await initPyodideAndPackages();

    // Load simulation.py into Pyodide virtual FS
    const response = await fetch('py/simulation.py');
    const code = await response.text();
    pyodide.runPython(code);
    pyodide.runPython('initialize()');

    const { renderer, scene, camera, geometry, positions } = createScene(
        document.getElementById("renderCanvas"), particleCount
    );

    setupUI(pyodide);

    function updatePositions() {
        const pos = pyodide.runPython("get_positions()").toJs();
        for (let i = 0; i < pos.length; i++) {
            positions[i*3 + 0] = pos[i][0];
            positions[i*3 + 1] = pos[i][1];
            positions[i*3 + 2] = pos[i][2];
        }
        geometry.attributes.position.needsUpdate = true;
    }

    function animate() {
        pyodide.runPython("step()");
        updatePositions();
        renderer.render(scene, camera);
        requestAnimationFrame(animate);
    }

    animate();
}

main();
