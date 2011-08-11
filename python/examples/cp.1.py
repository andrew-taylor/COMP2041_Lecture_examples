#!/usr/bin/python
# Written by andrewt@cse.unsw.edu.au  for COMP2041
# Simple cp implementation using line by line I/O
# and with statement

import sys,os
if len(sys.argv) != 3:
    print >>sys.stderr, "Usage: %s <infile> <outfile>" % sys.argv[0]
    sys.exit(1)
with open(sys.argv[1]) as infile:
    with open(sys.argv[2], 'w') as outfile:
        for line in infile:
            outfile.write(line)
