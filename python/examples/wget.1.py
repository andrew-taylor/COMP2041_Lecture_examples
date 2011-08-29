#!/usr/bin/python
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# fetch a web page remove HTML tags and constants
# and print non-empty lines

import sys, re, subprocess
# there are python libraries which provide a  better way to fetch web pages
for url in sys.argv[1:]:
    p = subprocess.Popen(["wget","-q","-O-",url], stdout=subprocess.PIPE)
    for line in iter(p.stdout.readline, ""):
        line = re.sub(r'&\w+;', ' ', line)
        line = re.sub(r'<[^>]*>', '', line)
        if not re.match(r'^\s+$', line):
            print line,
