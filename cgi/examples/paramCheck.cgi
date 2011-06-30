#!/usr/bin/perl -wT

use CGI qw/:all -debug/;

$checker = <<xxJSxx
function check(form) {
	if (form.mystring.value.length > 6) {
		alert("String too long")
		return false;
	}
	return true;
}
xxJSxx
;

$mystring = param("mystring");

print header, start_html(-script=>$checker),
	h3("Type a string"),
	start_form(-onsubmit=>"return check(this);"),
	textfield("mystring","",10,8),
	submit("Send"),
	end_form;

if (defined $mystring) {
	$nc = length($mystring);
	print p("String: '$mystring' has $nc chars");
}
print end_html;
