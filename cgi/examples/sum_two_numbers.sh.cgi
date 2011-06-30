#!/bin/sh
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Sum two numbers and outputs a form which will rerun the script

read parameters

x=`echo $parameters|sed 's/.*x=//;s/&.*//'`
y=`echo $parameters|sed  's/.*y=//;s/&.*//'`

cat <<eof
Content-type: text/html

<html><head><title>Sum Two Numbers</title></head><body>
eof

if test "$x" -a "$y"
then
	echo "$x * $y =" `expr $x '*' $y`
fi

cat <<eof
<form method="post" action="$SCRIPT_URI">
Enter x: <input type=textfield name=x value=$x>
<p>
Enter y: <input type=textfield name=y value=$y>
<p>
<input type="submit">
</form>
</body>
</html>
eof

