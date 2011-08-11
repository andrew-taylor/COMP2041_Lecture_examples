#!/usr/bin/perl -w -i
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# For each file given as argument replace occurrences of Hermione
# allowing for some misspellings with Harry and vice-versa.
# Relies on Zaphod not occurring in the text.
# The unix filter-like behaviour of  <> is used to read files
# Perl's -i option is used to replace file with output from the script.
# Perl's default variable $_ is used

while (<>) {
	s/Herm[io]+ne/Zaphod/g;
	s/Harry/Hermione/g;
	s/Zaphod/Harry/g;
}
