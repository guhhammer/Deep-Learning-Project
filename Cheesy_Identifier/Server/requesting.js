function submit(){
	var data = new FormData();
	var file = document.getElementById("file").files[0];
	var splitted = file.name.split(".");
	var extension = splitted[splitted.length-1];
	if(extension != "jpg" && extension != "png" && extension != "jpeg" && extension != "bmp"){
		alert("Sorry, your file format is not supported!");
		console.log(extension);
		return;
	}
	data.append('file', file);
	$.ajax({
		url: 'http://localhost:5000/api/v1/predict/sample',
		type: 'POST',
		contentType: false,
		cache: false,
		processData: false,
		data: data,
		success: function (data) {
			window.location.href = "answer.html?answer=" + data;
		}
	});
}