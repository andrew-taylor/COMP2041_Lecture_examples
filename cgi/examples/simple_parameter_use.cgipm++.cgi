#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Outputs a form which will rerun the script

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('A Simple Example');
warningsToBrowser(1);

print start_form;
print 'Enter a string: ';
print textfield('string');
print end_form;

if (param("string")) {
	print "Last time you entered: ";
	print param("string");
}
print end_html;
