#!/usr/bin/perl -w

# Simple CGI script written by andrewt@cse.unsw.edu.au
# Output some simple HTML and a table of the
# data  has passed to the CGI script.

use CGI qw/:all/;

print header,
      start_html('Input Parameters'),
      h2('Input Parameters'),
      "<table border=1>";
foreach $p (param()) {
	printf "<tr><td>%s<td>%s\n", $p, param($p);
}
print "</table>",hr,end_html;

