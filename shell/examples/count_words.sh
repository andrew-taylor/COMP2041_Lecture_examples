#!/bin/sh

# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# Count the number of time each different word occurs
# in the files given as arguments
# e.g count_words.sh dracula.txt

sed 's/ /\n/g' "$@"|      # convert to one word per line
tr A-Z a-z|               # map uppercase to lower case
sed "s/[^a-z']//g"|       # remove all characters except a-z and '  
grep -v '^$'|             # remove empty lines
sort|                     # place words in alphabetical order
uniq -c                   # use uniq to count how many times each word occurs