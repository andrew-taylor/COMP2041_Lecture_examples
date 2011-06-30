#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# to demonstrate a possible CGI security hole

sub change_mark();
sub authenticate_password();
sub admin_screen();
sub login_screen();

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);


print header, start_html('Insecure 2041 admin script');
warningsToBrowser(1);

# insecure: user may set this parameter directly
if (param('password_checked')) {
	change_mark();
} else {
	if (authenticate_password()) {
		param('password_checked', 1);
		admin_screen();
	} else {
		login_screen();
	}
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
		hidden('password_checked'),
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

