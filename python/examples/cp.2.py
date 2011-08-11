#!/usr/bin/python
# Written by andrewt@cse.unsw.edu.au  for COMP2041
# Simple cp implementation reading file into a list

import sys
if len(sys.argv) != 3:
    print >>sys.stderr, "Usage: %s <infile> <outfile>" % sys.argv[0]
    sys.exit(1)
lines = open(sys.argv[1]).readlines()
open(sys.argv[2], 'w').writelines(lines)
