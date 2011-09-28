#!/usr/bin/python
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# simple implementations of re.split & str.join
# to exhibit various python features
import re
def my_join1(separator, list):
	if not list:
	 	return ""
	string = str(list.pop(0))
	for element in list:
		string += separator + str(element)
	return string
	
def my_join2(separator, list):
	return reduce(lambda x, y:x+separator+y, map(str, list))

# using (tail) recursion
def my_split1(regexp, string):
	m = re.match(r'(.*?)%s(.*)'%regexp, string)
	if m:
		return [m.group(1)] + my_split1(regexp, m.group(2))
	else:
		return [string]

# more concise but perhaps less reable version using Python' ternary operator
def my_split2(regexp, string):
	m = re.match(r'(.*?)%s(.*)'%regexp, string)
	return [m.group(1)] + my_split1(regexp, m.group(2)) if m else [string]
	
# iterative form 
def my_split3(regexp, string):
	list = []
	pattern = re.compile(r'(.*?)%s(.*)'%regexp)
	while 1:
		m = pattern.match(string)
		if m:
			list.append(m.group(1))
			string = m.group(2)
		else:
			list.append(string)
			return list

a = my_join1("+", range(1,11))
print a, "=", eval(a)
a = my_join2("+", range(1,11))
print a, "=", eval(a)
print my_split1(",", "1,2,3,4,5,6,7,8,9,10");
print my_split2(",", "1,2,3,4,5,6,7,8,9,10");
print my_split3(",", "1,2,3,4,5,6,7,8,9,10");

