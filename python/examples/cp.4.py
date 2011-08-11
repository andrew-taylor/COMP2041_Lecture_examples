#!/usr/bin/python
# Written by andrewt@cse.unsw.edu.au  for COMP2041
# Simple cp implementation using shutil.copyfile

import sys,shutil
if len(sys.argv) != 3:
    print >>sys.stderr, "Usage: %s <infile> <outfile>" % sys.argv[0]
    sys.exit(1)
shutil.copyfile(sys.argv[1], sys.argv[2])