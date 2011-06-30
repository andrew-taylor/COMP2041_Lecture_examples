#!/usr/bin/perl
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Outputs a form which will rerun the script

use CGI qw/:all/;

print header,
      start_html('Self Replicating Form'),
      start_form,
      submit,
      end_form,
      end_html;

