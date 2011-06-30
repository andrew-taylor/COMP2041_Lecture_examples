#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Allow users to change a file

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('A Simple Example');
warningsToBrowser(1);

if (param('Save') && defined param('contents')) {
	open FILE, ">editfile.data" or die "Can not open editfile.data: $!";
	print FILE param('contents');
	close FILE;
	print h2('Saved'),end_html;
	exit 0;
}
if (!defined param('contents') && -r "editfile.data") {
	param('contents', `cat editfile.data`);
}

print	h2('File contents are:'),
		start_form,
		textarea(-name=>'contents', -rows=>10,-cols=>60),
		p, submit('Save'),
		end_form,
		end_html;
