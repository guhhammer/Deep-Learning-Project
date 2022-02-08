function pageLoaded(){
	var params = new URLSearchParams(window.location.search);
	document.getElementById("answer").innerHTML = params.get("answer");
}

function goBack(){
	window.location.href = "index.html";
}
window.onload = pageLoaded;