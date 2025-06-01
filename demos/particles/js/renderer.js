export function createScene(canvas, particleCount) {
    const renderer = new THREE.WebGLRenderer({ canvas });
    renderer.setSize(window.innerWidth, window.innerHeight);
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(70, window.innerWidth / window.innerHeight, 0.1, 100);
    camera.position.y = 2;
    camera.up.set(0, 0, 1);
    camera.lookAt(new THREE.Vector3(0, 0, 0));

    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    const material = new THREE.PointsMaterial({ color: 0xff5533, size: 0.02 });
    const points = new THREE.Points(geometry, material);
    scene.add(points);

    return { renderer, scene, camera, geometry, positions };
}