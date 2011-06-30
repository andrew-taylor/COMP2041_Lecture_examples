#!/bin/sh
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Outputs a form which will rerun the script

cat <<eof
Content-type: text/html

<html><head>Self replicating Form</head><body>
<form method="post" action="$SCRIPT_URI">
<input type="submit">
</form>
</body>
</html>
eof

