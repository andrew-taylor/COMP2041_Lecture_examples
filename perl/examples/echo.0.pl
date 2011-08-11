#!/usr/bin/perl -w
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# Perl implementation of /bin/echo
# always writes a trailing space

foreach $arg (@ARGV) {
	print $arg, " ";
}
print "\n";
