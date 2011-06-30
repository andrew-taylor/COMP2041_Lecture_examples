#!/usr/bin/perl -w

# Simple CGI script written by andrewt@cse.unsw.edu.au
# Print some HTML plus the environment
# passed to CGI script by the web server

print "Content-type: text/html

<html>
<head></head>
<body>
<h2>Environment Variables</h2>
<pre>
";

system "env";

print "
</pre>
</body>
</html>
";

