#!/usr/bin/python
# Written by andrewt@cse.unsw.edu.au  for COMP2041
# Simple cp implementation using line by line I/O

import sys,os
if len(sys.argv) != 3:
    print >>sys.stderr, "Usage: %s <infile> <outfile>" % sys.argv[0]
    sys.exit(1)
outfile = open(sys.argv[2], 'w')
for line in open(sys.argv[1]):
	outfile.write(line)