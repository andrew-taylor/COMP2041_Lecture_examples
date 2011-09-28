#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au
# 8 different ways to print the odd numbers in 
# a list - illustrating various aspects of Perl

# simple for loop
sub print_odd0(@) {
    my (@list) = @_;
    foreach $element (@list) {
        print "$element\n" if $element % 2;
    }
}

# simple for loop using index
sub print_odd1(@) {
    my (@list) = @_;
    foreach $i (0..$#list) {
        print "$list[$i]\n" if $list[$i] % 2;
    }
}

# set $_ in turn to each item in list
# evaluate supplied expression
# print item if the expression evaluates to true
sub print_list0(&@) {
    my ($select_expression, @list) = @_;
    foreach $_ (@list) {
        print "$_\n" if &$select_expression;
    }
}

# calling helper function which prints 
# items selected by an expression
sub print_odd2(@) {
    print_list0(sub {$_ % 2}, @_);
}

sub odd($) {
    return $_[0] % 2;
} 

# more concise version of print_list0
sub print_list1(&@) {
   &{$_[0]} && print "$_\n" foreach @_[1..$#_];
}

# calling helper function which prints 
# items selected by an expression
sub print_odd3(@) {
    print_list1(sub {odd $_}, @_);
}

# set $_ in turn to each item in list
# evaluate supplied expression
# return a list of items for which the expression evaluated to true
sub my_grep0(&@) {
    my $select_expression = $_[0];
    my @matching_elements;
    foreach $_ (@_[1..$#_]) {
        push @matching_elements, $_ if &$select_expression;
    }
    return @matching_elements;
}

# calling helper function which returns 
# list items selected by an expression
sub print_odd4(@) {
    foreach $x (my_grep0 {$_ % 2} @_) {
        print "$x\n";
    }
}


# more concise version of my_grep0
sub my_grep1(&@) {
    my $select_expression = shift;
    my @matching_elements;
    &$select_expression && push @matching_elements, $_ foreach @_;
    return @matching_elements;
}

# calling helper function which returns 
# list items selected by an expression
sub print_odd5(@) {
    my_grep1 {odd $_ && print "$_\n"} @_;
}

# using built-in grep and combining print
sub print_odd6(@) {
    grep {$_ % 2 && print "$_\n"} @_;
}

# using built-in grep and join
sub print_odd7(@) {
    print join("\n", grep {$_ % 2} @_), "\n";
}


@a = (1..10);
foreach $version (0..7) {
    print "print_odd$version\n";
    &{"print_odd$version"}(@a);
}