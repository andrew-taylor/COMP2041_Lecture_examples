#!/usr/bin/perl
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Sum two numbers and outputs a form which will rerun the script

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('Sum Two Numbers');
warningsToBrowser(1);

if (defined param("x") && defined param("y")) {
	printf "%s * %s = %s\n", param('x'), param('y'), param('x')*param('y');
}

print start_form;
print 'Enter x: ', textfield('x');
print p;
print 'Enter x: ', textfield('y');
print p;
print submit;
print end_form;
print end_html;
