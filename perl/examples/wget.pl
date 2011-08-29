#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a 2041 lecture example
# Fetch a web page removing HTML tags and constants
# Lines between script or style tags are skipped.
# Non-blank lines are printed

foreach $url (@ARGV) {
    open F, "wget -q -O- '$url'|" or die;
    while ($line = <F>) {
        if ($line =~ /^\s*<(script|style)/i) {
            while ($line = <F>) {
                last if $line =~ /^\s*<\/(script|style)/i;
            }
        }
        $line =~ s/&\w+;/ /g;
        $line =~ s/<[^>]*>//g;
        print $line if $line =~ /\S/;
    }
}
