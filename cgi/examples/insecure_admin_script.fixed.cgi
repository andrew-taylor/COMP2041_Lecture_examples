#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# to demonstrate fixing a CGI security hole
# note login&password are passed as hidden fields
# by admin screen and authenticated again before changing a mark

sub change_mark();
sub authenticate_password();
sub admin_screen();
sub login_screen();

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);


print header, start_html('2041 admin script with Security Hole Fixed');
warningsToBrowser(1);

if (authenticate_password()) {
	if (param('student number')) {
		change_mark();
	} else {
		admin_screen();
	}
} else {
	login_screen();
}
exit 0;

sub change_mark() {
	my $student_number = param('student_number');
	my $new_mark = param('new_mark');
	print  "Mark for $student_number set to $new_mark\n", end_html;
}

sub authenticate_password() {
	my $login = param('login');
	my $password = param('password');
	return $login && $password && $login eq "andrewt" && $password eq "secret";
}

sub admin_screen() {
	print start_form,
		'Enter 2041 student number: ', textfield('student_number'), "<br>\n",
		'Enter new mark: ', textfield('new_mark'), "<br>\n",
		submit('Change mark'),
		hidden('login'),
		hidden('password'),
		end_form,
		end_html;
}


sub login_screen() {
	print start_form,
		'Enter login: ', textfield('login'), "<br>\n",
		' Enter password: ', password_field('password'),, "<br>\n",
		submit('Login'),
		end_form,
		end_html;
}

