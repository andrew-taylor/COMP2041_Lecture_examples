#!/usr/bin/perl -w
use Example_Module qw/max/;
# As max is specified in our import list it can be used without the package name
print max(42,3,5), "\n";
# We don't import min explicitly so it needs the package name
print Example_Module::min(42,3,5), "\n";
