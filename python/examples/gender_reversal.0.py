#!/usr/bin/python
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# For each file given as argument replace occurrences of Hermione
# allowing for some misspellings with Harry and vice-versa.
# Relies on Zaphod not occurring in the text.

import re, sys,os
for filename in sys.argv[1:]:
    tmp_filename = filename + '.new'
    if os.path.exists(tmp_filename):
        print >>sys.stderr, "%s: %s already exists" % (sys.argv[0], tmp_filename)
        sys.exit(1)
    with open(filename) as f:
        with open(tmp_filename, 'w') as g:
            for line in f:
                line = re.sub(r'Herm[io]+ne', 'Zaphod', line)
                line = line.replace('Harry', 'Hermione')
                line = line.replace('Zaphod', 'Harry')
                g.write(line)
    os.rename(tmp_filename, filename)
