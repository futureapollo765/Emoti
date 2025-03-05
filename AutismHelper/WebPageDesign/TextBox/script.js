// script.js
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM fully loaded and parsed');
    loadText('leftText.txt', 'leftDialog');
    loadText('rightText.txt', 'rightDialog');
});

function loadText(file, elementId) {
    console.log(`Loading text from ${file}`);
    fetch(file)
        .then(response => {
            console.log(`Fetch response status: ${response.status}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            console.log(`Loaded text for ${elementId}`);
            document.getElementById(elementId).innerText = data;
        })
        .catch(error => {
            console.error('Error loading text file:', error);
        });
}
