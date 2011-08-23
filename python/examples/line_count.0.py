#!/usr/bin/python
# written by andrewt@cse.unsw.edu.au as a COMP2041 lecture example
# Count the number of lines on standard input.

import sys

line_count = 0
for line in sys.stdin:
	line_count += 1
print "%d lines" % line_count
