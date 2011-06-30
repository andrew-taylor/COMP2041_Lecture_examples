#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Print some HTML plus information about the environment
# in which the CGI script has been run
 
print "Content-type: text/html

<html>
<head></head>
<body>
<h2>Execution Environment</h2>
<pre>
";

for $command ("pwd","id","hostname","uname -a") {
	print " $command: ",` $command`;
}

print "
</pre>
</body>
</html>
";

