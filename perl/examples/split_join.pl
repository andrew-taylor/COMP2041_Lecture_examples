#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# implementations of Perl's split & join

sub my_join($@) {
	my ($separator, @list) = @_;
	return "" if !@list;
	my $string = shift @list;
	foreach $thing (@list) {
		$string .= $separator . $thing;
	}
	return $string;
}

sub my_split1($$) {
	my ($regexp, $string) = @_;
	my @list = ();
	while ($string =~ /(.*)$regexp(.*)/) {
		unshift @list, $2; 
		$string = $1;
	}
	unshift @list, $string;
	return @list;
}

sub my_split2($$) {
	my ($regexp, $string) = @_;
	my @list = ();
	while ($string =~ s/(.*?)$regexp//) {
		push @list, $1; 
	}
	push @list, $string;
	return @list;
}

$a = my_join("+", (1..10));
print "$a = ", eval $a, "\n";
@a = my_split1(",", "1,2,3,4,5,6,7,8,10");
print "@a\n"; 
@a = my_split2(",", "1,2,3,4,5,6,7,8,10");
print "@a\n"; 
