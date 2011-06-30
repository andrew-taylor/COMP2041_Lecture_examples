#!/usr/bin/perl

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('My addressbook');
warningsToBrowser(1);
print h2('My Addressbook');

$data_directory = "./addresses/";
mkdir $data_directory or die "Cannot create $data_directory: $!\n" if !-d $data_directory;

$login = param('login');

if (!$login) {
	print start_form, 'Enter your login: ', textfield('login'), end_form, end_html;
	exit 0;
} 

$login =~ s/[^\w\s]//g;          # remove all but expected characters
$login = substr $login, 0, 64;   # limit login to 64 characters
$user_directory = "$data_directory/$login/";

mkdir $user_directory or die "Cannot create $user_directory: $!\n" if !-d $user_directory;

if (param('add_name') && param('add_address')) {
	my $name = param('add_name');
	$name =~ s/[^\w\s-_]//g;        # remove all but expected characters
	$name = substr $name, 0, 256;   # limit name to 256 characters
	open F, ">$user_directory/$name" or die "Cannot create $user_directory/$name: $!\n";
	print F param('add_address');
	close F;
}

if (param('Delete')) {
	my $name = param('delete_name');
	$name =~ s/[^\w\s-_]//g;        # remove all but expected characters
	$name = substr $name, 0, 256;   # limit name to 256 characters
	unlink "$user_directory/$name" or die "Cannot unlink $user_directory/$name: $!\n";
}

opendir DIR, $user_directory or die "Cannot access $user_directory: $!\n";
while ($name = readdir DIR) {
	next if $name =~ /^\./;  # skip filenames like ., ..
	push @names, $name;
}
close DIR;

if (!@names) {
	print "Your addressbook is empty.";
} else {
	print "<table border=1>";
	foreach $name (@names) {
		open F, "$user_directory/$name" or die "Cannot access $user_directory/$name: $!\n";
		my @address = <F>;
		close F;
		print "<tr><td>$name<td>@address\n";
	}
	print "</table>";
}

print start_form,
	hr,
	h4('Add a new address'),
	'Name: ', textfield('add_name'),
	' Address: ', textfield('add_address'), ' ',
	hidden(login),
	submit('Add'),
	end_form;
	
if (@names) {
	print start_form,
		hr,
		h4('Delete the address for:'),
		'Name: ',  	popup_menu('delete_name', \@names),
		hidden(login),
		submit('Delete'),
		hr,
		end_form;
}
print end_html;
