#!/usr/bin/perl -w

use IO::Socket;
$server_host =  $ARGV[0] || 'localhost';
$server_port = 4242;
$c = IO::Socket::INET->new(PeerAddr => $server_host, PeerPort  => $server_port) or die;
print <$c>;
close $c;
