#!/usr/bin/perl -w

# my declarations avois subtle bugs with global variables
# In this case of the use in $i in print_n_strings
# changes the (global) $i above
# 

sub print_n_strings($$);

print "Enter n: ";
$n = <>;
print ((("*" x $n)."\n") x $n);
