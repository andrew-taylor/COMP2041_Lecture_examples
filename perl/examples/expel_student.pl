#!/usr/bin/perl -w

while ($line = <>) {
    chomp $line;
    $line =~ s/^"//;
    $line =~ s/"$//;
    my ($name,$offence,$date,$penalty);
    ($name,$offence,$date,$penalty) = split /"\s*,\s*"/, $line;
    $penalty =~ s/[^0-9]//g;
    $deduction{$name} += $penalty;
}

$worst = 0;
foreach $student (keys %deduction) {
    $penalty = $deduction{$student};
    if ($penalty > $worst) {
        $worst_student = $student;
        $worst = $penalty;
    }
}
print "Expel $worst_student who had $worst marks deducted\n";
