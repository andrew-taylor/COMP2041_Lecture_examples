#!/usr/bin/perl
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Output some simple HTML and the input parameters
# the web server has passed on to the CGI script.

if ($ENV{REQUEST_METHOD} eq 'POST') {
	$parameters = <>;
} else {
	$parameters = $ENV{QUERY_STRING}
}

print "Content-type: text/html

<html>
<head></head>
<body>
<h2>Input Parameters</h2>
<hr>
<pre>
$parameters
</pre>
<hr>
</body>
</html>
";

