// Three.js scene setup
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Load 3D model
const loader = new THREE.GLTFLoader();
loader.load('assets/model.glb', function (gltf) {
    const model = gltf.scene;
    scene.add(model);
    camera.position.set(0, 1, 5);
    animate();

    // Load dialog text and start processing
    fetch('text/dialog.txt')
        .then(response => response.text())
        .then(text => processDialog(text, model));
});

function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

function processDialog(text, model) {
    const lines = text.split('\n');
    let index = 0;

    function processLine() {
        if (index < lines.length) {
            const line = lines[index];
            index++;

            // Process the line (e.g., generate mouth movements and actions)
            console.log(line); // For debugging
            syncMouthWithSpeech(line, model);

            // Wait for a short period before processing the next line
            setTimeout(processLine, 3000); // Adjust delay as needed
        }
    }

    processLine();
}

function syncMouthWithSpeech(transcript, model) {
    // 根据文本生成嘴部动作和其他动作
    // 例如，根据不同的字母或音节选择相应的嘴部形状
    console.log(transcript);
    // 此处添加嘴部动作和肢体动作逻辑
}
