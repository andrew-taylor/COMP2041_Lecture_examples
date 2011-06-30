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
	$hidden_variable = param('x') + 1;
} else {
	$hidden_variable = 0;
}
param('x', $hidden_variable);

print h2($hidden_variable);
print start_form;
print hidden('x');
print submit;
print end_form;
print end_html;
