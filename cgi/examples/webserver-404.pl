#!/usr/bin/perl -w

# print incoming http requests to port 2041
# andrewt@cse.unsw.edu.au
# access by http://localhost:2041/

use IO::Socket;
$server = IO::Socket::INET->new(LocalPort => 2041, ReuseAddr => 1, Listen => SOMAXCONN) or die;
 
while ($c = $server->accept()) {
  	print $c "HTTP/1.0 404 FILE NOT FOUND\n";
  	print $c "Content-Type: text/plain\n\n";
  	print $c "This web server always returns 404\n";
    close $c;
}
