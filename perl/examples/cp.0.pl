#!/usr/bin/perl -w
# Written by andrewt@cse.unsw.edu.au  for COMP2041
# Simple cp implementation using line by line I/O

die "Usage: $0 <infile> <outfile>\n" if @ARGV != 2;

$infile = shift @ARGV;
$outfile = shift @ARGV;

open(IN, "<$infile") || die("Cannot open $infile: $!");
open(OUT, ">$outfile") || die("Cannot open $outfile: $!");

while ($line = <IN>) {
    print OUT $line;
}

close(IN);
close(OUT);
exit 0;
