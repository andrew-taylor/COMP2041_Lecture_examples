#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a 2041 lecture example
# for each courses specified as arguments
# print a summary of the other courses taken by students in this course

$enrollment_file = shift @ARGV or die;
$debug = 0;

open C, "course_codes" or die "$0: can not open course_codes: $!";
while (<C>) {
    ($code, $name) = /\s*(\S+)\s+(.*)/ or die "$0: invalid course codes line: $_";
    $course_name{$code} = $name;
    print STDERR "code='$code' -> name='$name'\n" if $debug;
}

open F, "<$enrollment_file" or die;
while (<F>) {
    ($course,$upi,$name) = split /\s*\|\s*/;
    push @{$course{$upi}}, $course;
    $name =~ s/(.*), (.*)/$2 $1/;
    $name =~ s/ .* / /;
    $name{$upi} = $name;
}

foreach $course (@ARGV) {
    %n_taking = ();
    $n_students = 0;
    foreach $upi (keys %course) {
        @courses = @{$course{$upi}};
        next if !grep(/$course/, @courses);
        foreach $c (@courses) {
            $n_taking{$c}++;
        }
        $n_students++;
    }
    foreach $c (sort {$n_taking{$a} <=> $n_taking{$b}} keys %n_taking) {
        printf "%5.1f%% of %s students take %s %s\n",
            100*$n_taking{$c}/$n_students, $course, $c, $course_name{$c};
    }
}
