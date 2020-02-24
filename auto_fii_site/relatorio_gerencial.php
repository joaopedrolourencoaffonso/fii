<!DOCTYPE html>
<html>
<head>
<title>Relatórios</title>
<style>
	div.corpo {
	  text-align: center;
	}
	

</style>
</head>

<body>
<div align="center">
	<h1 style="border-style: solid; color: #0000ff; font-family:courier; width:360px; height:40px;">Seja bem vindo!</h1>

	<p style="border-style: solid; color: #0000ff; font-family:courier; width:550px; height:40px;"> Para checar os updates dos seus relatórios gerenciais, basta escrever os seus nomes abaixo e clicar ENTER!</p>
	<p style="border-style: solid; color: #ff0000; font-family:courier; width:505px; height:20px;">PS: Não esqueça dos: ";" entre os nomes dos fundos!</p>
	<form method="POST" action="relatorio.php">
			<input size="50" type="text" placeholder="ALZR11;ABCP11" name="fundos"/><br>
			<br>
			<input type="submit" style="background-color: #4CAF50; font-family:arial; font-size:15px; color: white; text-align: center; width:150px; height:40px" value="Ver"/>
	</form>

	<?php
	$myfile = fopen("historico.txt", "r") or die("Unable to open file!");
	$var = fread($myfile,filesize("historico.txt"));
	echo '<p style="border-style: solid; color: #003300; font-family:courier; width:300px; height:20px;">A sua última pesquisa foi:</p>';
	echo "<p>$var</p>";
	fclose($myfile);
	?>

<div>



</body>
</html>
