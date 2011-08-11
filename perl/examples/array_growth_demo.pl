#!/usr/bin/perl -w

while (1) {
    print "Enter array index: ";
    $n = <STDIN>;
    if (!$n) {
    	last;
    }
    chomp $n;
    $a[$n] = 42;
    print "Array elelent $n now contains $a[$n]\n";
    printf "Array size is now %d\n", $#a+1;
}
