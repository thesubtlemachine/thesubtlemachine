export async function initPyodideAndPackages() {
    const pyodide = await loadPyodide();
    await pyodide.loadPackage("numpy");
    return pyodide;
}
