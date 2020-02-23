<?php

set_time_limit(900);

echo '<!DOCTYPE html>
<html>
<head>
	<title>Resultados</title>
	<style>
		table, th, td {
		  border: 1px solid black;
		  border-collapse: collapse;
		  font-family: century gothic
		}
		th, td {
		  padding: 5px;
		  text-align: center;
		}
		table#t01 tr:nth-child(even) {
		  background-color: #eee;
		}
		table#t01 tr:nth-child(odd) {
		 background-color: #fff;
		}
		table#t01 th {
		  background-color: black;
		  color: white;
		}
	</style>
</head>

<body>
<div align="center">
	<h1 style="border-style: solid; color: #0000ff; font-family:courier; width:360px; height:40px;">Fundos!</h1>
	<p style="border-style: solid; color: #33cc33; font-family:courier; width:550px; height:40px;">Abaixo, seguem algumas informações interessantes sobre cada fundo!</p>

	<table id="t01" style="width:100%">
	  <tr>
	    <th>Nome do fundo</th>
	    <th>Preço</th>
	    <th>Dividendo Yield</th>
	    <th>Último Rendimento</th>
	    <th>Patrimônio Líquido</th>
	    <th>Valor Patrimonial</th>
	    <th>p/vp</th>
	  </tr>';


echo exec("fundos.py");


echo "
	</table>
</div>
</body>
</html>";

#print($space);

#print($fundos);

?>