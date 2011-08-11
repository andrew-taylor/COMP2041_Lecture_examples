#!/usr/bin/perl -w -i
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# For each file given as argument replace occurrences of Hermione
# allowing for some misspellings with Harry and vice-versa.
# Relies on Zaphod not occurring in the text.
# Perl's -p option is used to produce unix filter-like behaviour.
# Perl's -i option is used to replace file with output from the script.

s/Herm[io]+ne/Zaphod/g;
s/Harry/Hermione/g;
s/Zaphod/Harry/g;
