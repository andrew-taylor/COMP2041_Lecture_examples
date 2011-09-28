#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# print a HTML times table

sub html_times_table {
    my ($min_x, $max_x, $min_y, $max_y, $bgcolor, $border) = @_;
    my $html = "<table border=$border bgcolor=$bgcolor>\n";
    foreach $y ($min_y..$max_y) {
        $html .= "<tr>";
        foreach $x ($min_x..$max_x) {
            $html .= sprintf "<td align=right>%s</td>", $x * $y;
        }
        $html .=  "</tr>\n";
    }
    $html .=  "</table>\n";
    return $html;
}

print html_times_table(1, 12, 1, 12, "pink", 1);
