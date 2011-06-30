#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Output some simple HTML and the input parameters
# the web server has passed on to the CGI script.
# Only works for the POST method which passes parameters on STDIN

print "Content-type: text/html

<html>
<head></head>
<body>
<h2>Input Parameters</h2>
<hr>
<pre>
$ENV{QUERY_STRING}
</pre>
<hr>
</body>
</html>
";

