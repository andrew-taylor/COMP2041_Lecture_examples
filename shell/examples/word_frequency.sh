#!/bin/sh
# Count the number of time each different word occurs
# in the files given as arguments
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# e.g. word_frequency.sh dracula.txt

sed 's/ /\n/g' "$@"|      # convert to one word per line
tr A-Z a-z|               # map uppercase to lower case
sed "s/[^a-z']//g"|       # remove all characters except a-z and '  
grep -v '^$'|             # remove empty lines
sort|                     # place words in alphabetical order
uniq -c|                  # use uniq to count how many times each word occurs
sort -n                   # order words in frequency of occurrance