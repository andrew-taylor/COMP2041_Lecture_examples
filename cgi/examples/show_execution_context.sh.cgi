#!/bin/sh
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Print some HTML plus information about the environment
# in which the CGI script has been run
 
cat <<eof
Content-type: text/html

<html>
<head></head>
<body>
<h2>Execution Environment</h2>
<pre>
eof

for command in pwd id hostname 'uname -a'
do
	echo "$command: `$command`"
done

cat <<eof
</pre>
</body>
</html>
eof

