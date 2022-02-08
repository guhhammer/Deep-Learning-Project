<?php 

		
	$file = $_POST['file'];


	// Find a way to pass the image to the python file as a parameter.



	// echo shell_exec("python test.py 'parameter1'"); // execute python file with the model.
		
	echo 'User IP - '.$_SERVER['REMOTE_ADDR'];


/*  The python file get and receive image.

	import sys
	input=sys.argv[1] // get image argument in model.


	print(input) // return result to php.

*/


?>

