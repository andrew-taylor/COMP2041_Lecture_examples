#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Outputs a form which will rerun the script
# An input field of type hidden is used to pass an integer
# to successive invocations

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html(-bgcolor=>'white','A Simple Example');
warningsToBrowser(1);

$x = param('state');
$x = 0 if !defined $x;
$x++;
param("state", $x);

print start_form;

if ($x % 2 == 0) {
	print   "$x) What's your name?\n", textfield('name');
} else {
	print   "$x) What's your height?\n", textfield('height');
}

print hidden('state');
print end_form;
print end_html;
