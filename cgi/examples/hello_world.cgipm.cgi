#!/usr/bin/perl -w
# Output some simple HTML

use CGI qw/:all/;

print header,
      start_html('A Simple Example'),
      h2('Hello World'),
      end_html;
