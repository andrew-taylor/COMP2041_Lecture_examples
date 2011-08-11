#!/usr/bin/python
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# create a string of size 2^n by concatenation
import sys
if len(sys.argv) != 2:
	print >>sys.stderr, "Usage: %s <n>" % sys.argv[0]
	sys.exit(1)
n = 0
string = '@'
while  n  < int(sys.argv[1]):
    string =  string + string
    n += 1
print "String of 2^%d = %d characters created\n" % (n, len(string));
