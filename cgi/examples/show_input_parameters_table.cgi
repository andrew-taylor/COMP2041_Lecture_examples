#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Output some simple HTML and a table of the input parameters
# the web server has passed on to the CGI script.

print "Content-type: text/html

<html>
<head></head>
<body>
<h2>Input Parameters</h2>
<hr>
<table border=1>
";

if ($ENV{REQUEST_METHOD} eq 'POST') {
	$parameters = <>;
} else {
	$parameters = $ENV{QUERY_STRING}
}

foreach (split(/\&/, $parameters)) {
	/([^=]*)=(.*)/;
	print "<tr><td>$1<td>$2\n";
}

print "
</table>
<hr>
</body>
</html>
";

