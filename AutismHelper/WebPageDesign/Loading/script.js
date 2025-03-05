
let loader = document.querySelector(".loader");
function finishLoad() {
	window.onload = function() {
		loader.style.display = "none";
	}
}