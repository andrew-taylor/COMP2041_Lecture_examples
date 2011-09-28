#!/usr/bin/perl -w
%days = (Sunday => 0, Monday => 1, Tuesday => 2, Wednesday => 3,
         Thursday => 4, Friday => 5, Saturday => 6);
         
sub random_day {
	my @days = keys %days;
	return $days[rand @days];
}

sub compare_day {
	return $days{$a} <=> $days{$b};
}

push @random_days, random_day() foreach 1..5;
print "random_days=@random_days\n";
@sorted_days = sort compare_day @random_days;
print "sorted days=@sorted_days\n";
