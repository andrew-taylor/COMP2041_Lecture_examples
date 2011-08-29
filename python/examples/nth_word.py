#!/usr/bin/python
# written by andrewt@cse.unsw.edu.au as a 2041 lecture example
# Print the nth word on every line of input files/stdin
# output is piped through fmt to make reading easy

import fileinput, sys, subprocess

if len(sys.argv) < 2:
    print >>sys.stderr, "Usage: %s <n>" % sys.argv[0]
    sys.exit(1)
    
nth_word = int(sys.argv.pop(1))
p = subprocess.Popen(["fmt","-w","40"], stdin=subprocess.PIPE)
for line in fileinput.input():
    words = line.rstrip().split()
    if len(words) > nth_word:
        print >>p.stdin, words[nth_word]
p.stdin.close()
