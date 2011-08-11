#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# For each file given as argument replace occurrences of Hermione
# allowing for some misspellings with Harry and vice-versa.
# Relies on Zaphod not occurring in the text.

foreach $filename (@ARGV) {
	$tmp_filename = "$filename.new";
	die "$0: $tmp_filename already exists" if -e "$tmp_filename";
    open F, "<$filename" or die "$0: Can not open $filename: $!";
    open G, ">$tmp_filename" or die "$0: Can not open $tmp_filename : $!";
    while ($line = <F>) {
        chomp $line;
        $line =~ s/Herm[io]+ne/Zaphod/g;
        $line =~ s/Harry/Hermione/g;
        $line =~ s/Zaphod/Harry/g;
        print G "$line\n";
    }
    rename("$tmp_filename", $filename) or die "$0: Can not rename file";
}
