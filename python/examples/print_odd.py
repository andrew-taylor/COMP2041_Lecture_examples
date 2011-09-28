#!/usr/bin/python
# written by andrewt@cse.unsw.edu.au
# 5 different ways to print the odd numbers in 
# a list - illustrating various aspects of Python

# simple for loop
def print_odd0(list):
    for element in list:
        if element % 2 :
            print element

# list comprehension
def print_odd1(list):
    odd = [x for x in list if x % 2]
    for element in odd:
        print element
    
def odd(x):
    return x % 2
    
# filter+helper function
def print_odd2(list):
    for element in filter(odd, list):
        print element
    
# filter+lambda expression
def print_odd3(list):
    for element in filter(lambda x:x % 2, list):
        print element
    
# join+map+filter+helper function
def print_odd4(list):
    print "\n".join(map(str, filter(odd, list)))
    
a = range(1, 10)
for version in range(0, 5):
    print "print_odd%s"%version
    eval("print_odd%s(a)"%version)
