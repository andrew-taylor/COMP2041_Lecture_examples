#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# with SQL injection security hole fixed

# This scripts expects parameters such as:
# user=andrewt
# password=secret

# it can be fooled by including SQL code in
# the password parameter for example:
# user=andrewt
# password=or 't'='t

# These command generate a suitable sqlite database for the script
# echo "create table passwd(user TEXT, password TEXT);"|sqlite3 user.db
# echo "insert into passwd(user,password) values('andrewt','secret');"|sqlite3 user.db

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
use DBI;

print header, start_html('SQL Injection - Avoided');
warningsToBrowser(1);  

if (!defined param('user')) {
	print start_form, 'User: ', textfield('user'),p, 'Password: ', textfield('password'),p,submit,end_form;
	print p,"Should only be to authenticate with user <font color=red>andrewt</font>, password <font color=red>secret</font>\n";
	print p,"Adding SQL will not help, e.g. try: <font color=red>' or '42'='42</font>\n",p,end_html;
	exit(0);
}

$dbh = DBI->connect( "dbi:SQLite:user.db" ) || die;

$user = param('user');
$user = substr $user, 0, 64;          # limit user name to 64 characters
$user =~ s/\W+//g;                    # remove all but expected characters
$user = $dbh->quote($user);            # should be unnessary
$password = param('password');
$password = substr $password, 0, 64;  # limit password to 64 characters
$password = $dbh->quote($password);    # quote SQL special characters

$res = $dbh->selectall_arrayref("SELECT * from passwd where user=$user and password=$password");
if (@$res) {
	print "Authenticated\n";
} else {
	print "Wrong password\n";
}

print "<p><tt><small>sql query = SELECT * from passwd where user=$user and password=$password\n",end_html;
