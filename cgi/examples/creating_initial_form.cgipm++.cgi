#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Outputs a form which will rerun the script
# The value entered last time is made the initial value
# of the text field

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('A Simple Example');
warningsToBrowser(1);

if (defined param("string")) {
	$string = param("string");
	param("string", ""); # clear the field
} else {
	param("string", "initial value");
}

print start_form;
print 'Enter a string: ';
print textfield('string');
print end_form;

if (defined $string) {
	print "Last time you entered: $string";
}
print end_html;
