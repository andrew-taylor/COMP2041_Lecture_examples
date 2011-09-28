#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# print a HTML times table

sub html_times_table {
    my %defaults = (min_x=>1, max_x=>10, min_y=>1, max_y=>10, bgcolor=>'white', border=>0);
    my %arguments = @_;
    my %parameters = (%defaults,%arguments);
    my $html = "<table border=$parameters{border} bgcolor=$parameters{bgcolor}>\n";
    foreach $y ($parameters{min_y}..$parameters{max_y}) {
        $html .= "<tr>";
        foreach $x ($parameters{min_x}..$parameters{max_y}) {
            $html .= sprintf "<td align=right>%s</td>", $x * $y;
        }
        $html .=  "</tr>\n";
    }
    $html .=  "</table>\n";
    return $html;
}

print html_times_table(max_y=>12, max_x=>12, bgcolor=>'pink');
