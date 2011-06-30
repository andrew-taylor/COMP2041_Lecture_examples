#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as COMP2041 exampl
# Pick a random image from a directory
# overlay the image with the filename using ImageMagick

$directory = "./images";
foreach $file (glob "$directory/*.jpg") {
	next if !-r $file;
	push @files, $file;
}

$random_file = $files[rand @files];
$name = $random_file;
$name =~ s/.jpg$//;
$name =~ s/.*\///;
$name =~ s/[\-_]/ /g;
$name =~ s/[^\w\s]//g;
$convert_options = "-gravity south -pointsize 72 -stroke '#0004' -strokewidth 2 -annotate 0 '$name' -stroke none -fill white -annotate 0 '$name'";
print "Content-type: image/jpeg\n\n";
system "convert '$random_file' $convert_options -"

