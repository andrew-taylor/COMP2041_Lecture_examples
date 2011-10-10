#!/usr/bin/perl
# Simple CGI script written by andrewt@cse.unsw.edu.au

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
use CGI::Cookie;

%cookies = CGI::Cookie->fetch;
$login = '';
if (defined param('login')) {
	$login =  param('login');
} elsif ($cookies{'myAddressBookLogin'}) {
	$login = $cookies{'myAddressBookLogin'}->value
}

$login =~ s/[^\w\s]//g;          # remove all but expected characters
$login = substr $login, 0, 64;   # limit login to 64 characters

if (!$login) {
	print	header,
			start_html('My addressbook'),
			start_form,
			'Enter your login: ', textfield('login'),
			end_form,
			end_html;
	exit 0;
}

my $cookie = CGI::Cookie->new(-name => 'myAddressBookLogin', -value => $login, -expires => '+3M');
print	header(-cookie=>$cookie),
		start_html('My addressbook'),
		h2("My Addressbook for $login");
warningsToBrowser(1);

$data_directory = "./addresses/";
mkdir $data_directory or die "Cannot create $data_directory: $!\n" if !-d $data_directory;
$user_directory = "$data_directory/$login/";
mkdir $user_directory or die "Cannot create $user_directory: $!\n" if !-d $user_directory;

if (param('add_name') && param('add_address')) {
	my $name = param('add_name');
	$name =~ s/[^\w\s-_]//g;        # remove all but expected characters
	$name = substr $name, 0, 256;   # limit name to 256 characters
	$address = param('add_address');
	$address =~ s/[^\w\s-_\/]//g;          # remove all but expected characters
	$address = substr $address, 0, 1024;   # limit address to 1024 characters
	open F, ">$user_directory/$name" or die "Cannot create $user_directory/$name: $!\n";
	print F $address;
	close F;
}

if (param('Delete')) {
	my $name = param('delete_name');
	$name =~ s/[^\w\s-_]//g;        # remove all but expected characters
	$name = substr $name, 0, 256;   # limit name to 256 characters
	unlink "$user_directory/$name" or die "Cannot unlink $user_directory/$name: $!\n";
}

@address_files = glob "$user_directory/*";

if (!@address_files) {
	print "Your addressbook is empty, $login.";
} else {
	print "<table border=1>";
	foreach $address_file (@address_files) {
		open F, $address_file or die "Cannot access $address_file: $!\n";
		my @address = <F>;
		close F;
		my $name = $address_file;
		$name =~ s/.*\///;
		print "<tr><td>$name<td>@address\n";
	}
	print "</table>";
}

print start_form,
	hr,
	h4('Add a new address'),
	'Name: ', textfield('add_name'),
	' Address: ', textfield('add_address'), ' ',
	hidden(login), # in case cookies are disbaled
	submit('Add'),
	end_form;
	
if (@address_files) {
	my @names = @address_files;
	s/.*\/// foreach @address_files;
	print start_form,
		hr,
		h4('Delete the address for:'),
		'Name: ',  	popup_menu('delete_name', \@names),
		hidden(login), # in case cookies are disbaled
		submit('Delete'),
		hr,
		end_form;
}
print end_html;
