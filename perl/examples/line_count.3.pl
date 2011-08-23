#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a COMP2041 lecture example
# Count the number of lines on standard input.
# read the input into an array and use the array size.

@lines = <STDIN>;
print $#lines+1, " lines\n";
