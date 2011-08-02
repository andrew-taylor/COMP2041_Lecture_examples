#!/bin/sh
# A simple shell script which demonstrating access to arguments.
# written by andrewt@cse.unsw.edu.au as a COMP2041 example

echo My name is $0
echo My process number is $$
echo I have $# arguments
echo My arguments separately are $*
echo My arguments together are "$@"
echo My 5th argument is "'$5'"
