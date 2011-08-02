<html>
<body>
<h2>GET</h2>
<?=dump($_GET)?>
<h2>POST</h2>
<?=dump($_POST)?>
</body>
</html>
<?
function dump($params)
{
	$html = "<table border='1' cellpadding='1'>\n";
	$html .= "<tr><th>Name</th><th>Value</th></tr>\n";
	foreach ($params as $pname => $pvalue)
		$html .= "<tr><td>$pname</td><td>$pvalue</td></tr>\n";
	$html .= "</table>\n";
	return $html;
}
?>
