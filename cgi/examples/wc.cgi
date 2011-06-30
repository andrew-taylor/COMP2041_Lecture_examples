#!/usr/bin/perl
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Count words in text area, file or URL.

sub wc($) { 
	my ($text) = @_;
	my ($words, $bytes, $lines);
	foreach $line (split "\n", $text) {
	    my @words = split /\s+/, $line;
	    $words += @words;
 		$bytes += length $line;
 		$lines++;
 	}
 	return ($lines, $words, $bytes);
}

# if their are arguments, program is being be run as an application for debugging
if (@ARGV) {
    printf "%d lines %d words %d bytes\n", wc(join("", <>));
    exit(0);
    
}

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);


print header;
print start_html('Word Count');

my $action = param('action') || '';
if (param('url') && $action eq 'Upload URL') {
	my $url = param('url');
    open U, "wget -q -O- '$url'|";
    my $data = join("", <U>);
    param('input', $data);
} elsif (param('filename') && $action eq 'Upload File') {
	my $filename = param('filename');
 	my $data = join("", <$filename>);
    param('input', $data);
} elsif ($action eq 'Clear') {
    param('input', '');
}

print start_form,
      hr, 'Enter text for wc: ', p,
      textarea(-name=>'input'), p,
      submit(-name => "action", -value=> 'Count Words'),
      submit(-name => "action", -value=> 'Clear'),
      p, hr,p,
      'Or upload a file for wc: ',
      filefield('filename'), p,
      submit(-name => "action", -value => 'Upload File'), p, hr,p,
      'Or enter a URL: ', textfield('url'), p,
      submit(-name => "action", -value => 'Upload URL'),p, hr;

if (defined param('input')) {
    printf "%d lines %d words %d bytes\n", wc param('input');
}

print end_form, end_html;
