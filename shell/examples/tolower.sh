#!/bin/sh
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# Change names of specified files to lower case
# Perl utility rename provides more general alternative.
# Note the use of test to check if the new filename differs from the old.

if test $# = 0
then
    echo "Usage $0: <files>" 1>&2
    exit 1
fi

for filename in "$@"
do
    new_filename=`echo "$filename" | tr A-Z a-z`
    test "$filename" = "$new_filename" && continue
    if test -r "$new_filename"
    then
        echo "$0: $new_filename exists" 1>&2
    elif test -e "$filename"
    then
        mv "$filename" "$new_filename"
    else
        echo "$0: $filename not found" 1>&2
    fi
done
