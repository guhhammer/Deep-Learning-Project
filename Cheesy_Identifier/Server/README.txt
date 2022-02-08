$.ajax({
	url: 'http://localhost:5000/api/v1/predict/sample',
	type: 'POST',
	dataType: 'json',
	contentType: 'application/json',
	data: '{"pregnant":6,"glucose": 148, "bp":72 ,"skin": 35, "insulin":3 , "bmi": 33.6, "pedigree": 0.627,"age": 47 }',
	success: function (data) {
		console.log(data)
	}
});