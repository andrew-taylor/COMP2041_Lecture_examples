#!/usr/bin/python
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# Python implementation of /bin/echo
# always writes a trailing space
import sys
for arg in sys.argv[1:]:
	print arg, " ",
print 
