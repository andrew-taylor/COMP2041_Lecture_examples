#!/usr/bin/perl -w
@days = (Sunday , Monday, Tuesday, Wednesday, Thursday, Friday, Saturday);
@days{@days} = 0..6;
         
push @random_days, $days[rand @days] foreach 1..5;
print "random_days=@random_days\n";
@sorted_days = sort {$days{$a} <=> $days{$b}} @random_days;
print "sorted days=@sorted_days\n";
