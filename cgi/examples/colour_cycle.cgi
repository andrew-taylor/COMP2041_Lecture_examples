#!/usr/bin/perl
#
# Parameters:
# colr = index into the array of colour names
#
# This script makes the assumption that the colour names are valid as
# attribute values for 'bgcolor'
# If we didn't want to assume this, we could define an auxiliary parallel
# array that held the RGB codes for the colours, e.g.
#
# @codes = ('#FF0000', '#FF9900", '#FFFF00', '#00FF00', ...)
                    
use CGI ':all';
         
@colours = ("red", "orange", "yellow", "green", "blue", "indigo", "violet");
$colr = (param("colr") || 0) % @colours; 
print header, start_html(-bgcolor=>"$colours[$colr]");
param('colr', ($colr + 1) % @colours);
print start_form,
	hidden('colr'),
	submit("Next colour"),
	end_form,
	end_html;
