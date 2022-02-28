<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<link rel="stylesheet" type="text/css" href="style.css">
	<title>PCAP</title>
</head>
<body>
	<?php
		$file_names = array("./py_scripts/dict.py", "./py_scripts/def.py", "./py_scripts/tuple.py", "./py_scripts/list.py");
		for($i=0;$i<4;$i++){
			echo("<p class=\"singularo_scripto\">");
			$file = fopen($file_names[$i], "r")or die("no file !!");
			while(!feof($file)) {
				echo fgets($file) . "<br>";
			}
			fclose($file);
			echo("</p>");

		}


	?>



</body>