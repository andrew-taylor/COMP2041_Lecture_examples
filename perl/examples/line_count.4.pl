#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a COMP2041 lecture example
# Count the number of lines on standard input.
# Assignment to () forces a list context and hence reading all lines of input.
# The special variable $. contains the current line number

() = <STDIN>;
print "$. lines\n";
