#!/usr/bin/perl -w
# fetch files via http from the webservers at the specified URLs
# see HTTP::Request::Common for a more general solution
# andrewt@cse.unsw.edu.au
use IO::Socket;
%urls_visited = ();
sub fetch_page {
	my ($url) = @_;
	print STDERR "fetch_page($url)\n";
	sleep(1);
	return if $urls_visited{$url}++;
	my ($host, $junk, $port, $path) = $url =~ /http:\/\/([^\/]+)(:(\d+))?(.*)/ or die;
	$c = IO::Socket::INET->new(PeerAddr => $host, PeerPort  => $port || 80) or die;
	print STDERR "path='$path'\n";
	print $c "GET $path HTTP/1.0\n\n";
	my @page = <$c>;
	my @urls = grep {s/.*<a\s+href=\s*"([^"]+)"\s*>.*/$1/i} @page;
	chomp @urls;
	foreach $u (@urls) {
		$u =~ /^\w+:/ && next;
		$u =~ s/^/$url\//;
		$u =~ s/[?#].*//;
		$u =~ s/([^:])\/+/$1\//g;
	}
	@urls = grep /^http:/, @urls;
	print "urls=@urls\n";
	
	fetch_page($_) foreach @urls;
	print "returning\n";
}

fetch_page($_) foreach @ARGV;
