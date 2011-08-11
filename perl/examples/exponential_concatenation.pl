#!/usr/bin/perl -w
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# create a string of size 2^n by concatenation

die "Usage: $0 <n>\n" if @ARGV != 1;
$n = 0;
$string = '@';
while ($n  < $ARGV[0]) {
    $string = "$string$string";
    $n++;
}
printf "String of 2^%d = %d characters created\n", $n, length $string;
