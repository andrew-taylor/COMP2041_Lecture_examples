#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a 2041 lecture example
# Print the nth word on every line of input files/stdin
# output is piped through fmt to make reading easy

die "Usage: $0 <n> <files>\n" if !@ARGV;
$nth_word = shift @ARGV;
open F, "|fmt -w 40" or die "Can nor run fmt";
while ($line = <>) {
    chomp $line;
    @words = split(/ /, $line);
    print F "$words[$nth_word]\n" if $words[$nth_word];
}
close F;
