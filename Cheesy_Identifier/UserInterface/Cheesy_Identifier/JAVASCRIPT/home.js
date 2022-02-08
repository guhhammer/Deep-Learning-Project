$(document).ready(function(){

	// Grab elements, create settings, etc.
	var video = document.getElementById('video');

	// Elements for taking the snapshot
	var canvas = document.getElementById('canvas');
	var context = canvas.getContext('2d');
	var video = document.getElementById('video');

	$(document).click(function(e){

		if(e.target.closest(".pop_up_overlay") != null){  return;  }

		if(e.target == document.getElementById("b_webcam")){  return;  }

	  	$(".pop_up_overlay, .popup_content").removeClass("active");

	});

	$("#b_webcam").click(function() {
	
	  	$(".pop_up_overlay, .popup_content").addClass("active");
	  	$("body").addClass("unscrollable");

	  	var $target = $('html,body');
		$target.animate({scrollTop: 0}, 400);
		
		// Get access to the camera!
		if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
		    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
		        video.srcObject = stream; video.play();
		    });
		}

	});

	$(".close, .popup_overlay").click(function() {
	  	$(".pop_up_overlay, .popup_content").removeClass("active");
		if($("body").hasClass("unscrollable")){ $("body").removeClass("unscrollable"); }
	});

	$(".second_button, .popup_overlay").click(function(){

		
	    var image = context.drawImage(video, 0, 0, 320, 240);
        
	    $.ajax({

			type: "POST",
			dataType: "json",
			url: "../PHP/home.php",
			data: {
				'file' : image
			},
			success: function(){

			}
		});

	
		window.open("../HTML/identification.html", "_self");

		$(".pop_up_overlay, .popup_content").removeClass("active");
		if($("body").hasClass("unscrollable")){ $("body").removeClass("unscrollable"); }

	});	

	$("#file_input").on("change",function(event) {

   		var file = event.target.files[0];
		
		var filename = $('input[type=file]').val().split('\\').pop();

		$.ajax({

			type: "POST",
			dataType: "json",
			url: "../PHP/home.php",
			data: {
				'file' : $("input[type=file]").val()
			},
			success: function(){

			}
		});

		$(".pop_up_overlay, .popup_content").removeClass("active");
		if($("body").hasClass("unscrollable")){ $("body").removeClass("unscrollable"); }

   		window.open("../HTML/identification.html", "_self");

	});


})