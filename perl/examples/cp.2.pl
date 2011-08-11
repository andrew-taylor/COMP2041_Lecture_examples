#!/usr/bin/perl -w
# Written by andrewt@cse.unsw.edu.au for COMP2041
# Simple cp implementation reading entire file into array
# note that <> returns an array of lines
# in a list context (in a scalar context it returns a single line)

die "Usage: $0 <infile> <outfile>\n" if @ARGV != 2;

$infile = shift @ARGV;
$outfile = shift @ARGV;

open(IN, "<$infile") || die("Cannot open $infile: $!");
@lines = <IN>;
close(IN);

open(OUT, ">$outfile") || die("Cannot open $outfile: $!");
print OUT @lines;
close(OUT);

exit 0;
