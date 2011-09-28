#!/usr/bin/python
import random,operator
days = {'Sunday':0, 'Monday':1, 'Tuesday':2, 'Wednesday':3,
         'Thursday':4, 'Friday':5, 'Saturday':6}
         
def random_day():
	return str(random.choice(days.keys()))

def compare_day(day1, day2):
	return cmp(days[day1], days[day2])

random_days = [random_day() for x in xrange(0,5)]
print "random_days = ", ",".join(random_days)
sorted_days = sorted(random_days, cmp=compare_day)
print "sorted_days = ", ",".join(sorted_days)
