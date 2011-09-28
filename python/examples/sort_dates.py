#!/usr/bin/python
import re
from random import randint
def random_date():
	return "%02d/%02d/%04d"%(randint(1,28), randint(1,12), randint(2000,2020))

def compare_date(date1, date2):
	(day1,month1,year1) = re.split(r'\D+', date1)
	(day2,month2,year2) = re.split(r'\D+', date2)
	return cmp(year1,year2) or cmp(month1,month2) or cmp(day1,day2)

random_dates = [random_date() for x in xrange(0,5)]
print "random_dates=",",".join(random_dates)
sorted_dates = sorted(random_dates, cmp=compare_date)
print "sorted dates=",",".join(sorted_dates)