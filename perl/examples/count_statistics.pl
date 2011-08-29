#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a 2041 lecture example
# print the courses being taken by each students enrolled in the specified courses

$enrollment_file = shift @ARGV or die;
$debug = 0;

open C, "course_codes" or die "$0: can not open course_codes: $!";
while ($line = <C>) {
    chomp $line;
    $line =~ s/^\s+//;
    $code = substr($line, 0, 8);
    $name = substr($line, 9);
    $course_name{$code} = $name;
    print STDERR "code='$code' -> name='$name'\n" if $debug;
}

open F, "<$enrollment_file" or die;
while (<F>) {
    ($course,$upi,$name,$program,$gender,$lab) = split /\s*\|\s*/;
    $course{$upi} .=  " $course";
    $name =~ s/(.*), (.*)/$2 $1/;
    $name =~ s/ .* / /;
    $name{$upi} = $name;
    $program{$upi} = $program;
    $gender{$upi} = $gender;
    $lab{$upi} = $lab;
}

foreach $course (@ARGV) {
    foreach $upi (keys %course) {
        $courses = $course{$upi};
        next if $courses !~ /$course/;
        print "$name{$upi} is taking:\n";
        $courses =~ s/^ //;
        @courses = split / /, $courses;
        foreach $course (@courses) {
            print "$course $course_name{$course}\n";
        }
    }
}
