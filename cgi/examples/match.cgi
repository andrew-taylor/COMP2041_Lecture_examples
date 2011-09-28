#!/usr/bin/perl
# CGI script written by andrewt@cse.unsw.edu.au
# See match.html, match.js

use CGI qw/:all/;
print header;
if (param('string') =~ param('regex')) {
	print b('Match succeeded, this substring matched: '), tt(escapeHTML($&));
} else {
	print b('Match failed');
}
