#!/usr/bin/perl -w

# Written by andrewt@cse.unsw.edu.au for COMP2041
# run as course_first_names.pl enrollments
# report cases where there are multiple people
# same first name enrolled in acourse

while ($line = <>) {
	@fields = split /\|/, $line;
	$course = $fields[0];
	$full_name = $fields[2];
	$full_name =~ /.*,\s+(\S+)/ or next;
	$first_name = $1;
	$cfn{$course}{$first_name}++;
}

foreach $course (sort keys %cfn) {
	foreach $first_name (sort keys %{$cfn{$course}}) {
		next if $cfn{$course}{$first_name} < 2;
		printf "In $course there are %d people with the first name $first_name\n", $cfn{$course}{$first_name};
	}
}

	
