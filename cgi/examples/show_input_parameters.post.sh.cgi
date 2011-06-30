#!/bin/sh
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Output some simple HTML and the input parameters
# the web server has passed on to the CGI script.
# Only works for the POST method which passes parameters on STDIN

cat <<eof
Content-type: text/html

<html>
<head></head>
<body>
<h2>Input Parameters</h2>
<pre>
`cat`
</pre>
</body>
</html>
eof


