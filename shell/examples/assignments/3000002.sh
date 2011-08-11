#!/bin/sh

if test $# -ne 1
then
	echo "Usage: $0 <number>"
	exit 1
fi
number=$1

counter=2
while test $counter -lt $number
do
	mod=`expr $number % $counter`
	if test $mod -eq 0
	then
		echo "$number is not prime"
		exit 0
	fi
	counter=`expr $counter + 1`
done
echo "$number is prime"
exit 0

