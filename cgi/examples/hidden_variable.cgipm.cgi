#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Outputs a form which will rerun the script
# An input field of type hidden is used to pass an integer
# to successive invocations

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('A Simple Example');
warningsToBrowser(1);

if (defined param('x')) {
	$hidden_variable = param("x") + 1;
} else {
	$hidden_variable = 0;
}

print "Script has been invoked $hidden_variable times\n";

print <<eof;
<form method="post" action="$ENV{SCRIPT_URI}">
<input type=hidden name="x" value="$hidden_variable">
<input type="submit">
</form>
<p>
eof


print end_html;
