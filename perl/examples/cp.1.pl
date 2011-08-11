#!/usr/bin/perl -w
# Written by andrewt@cse.unsw.edu.au  for COMP2041
# Simple cp implementation using line by line I/O
# relying on the default variable $_

die "Usage: $0 <infile> <outfile>\n" if @ARGV != 2;

$infile = shift @ARGV;
$outfile = shift @ARGV;

open(IN, "<$infile") || die("Cannot open $infile: $!");
open(OUT, ">$outfile") || die("Cannot open $outfile: $!");

# loop could also be written in one line:
# print OUT while <IN>;

while (<IN>) {
    print OUT;
}

close(IN);
close(OUT);
exit 0;
