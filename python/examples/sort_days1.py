#!/usr/bin/python
import random,operator
day_names = "Sunday Monday Tuesday Wednesday Thursday Friday Saturday"
days = dict(zip(day_names.split(), range(0,7)))
random_days = [random.choice(days.keys()) for x in xrange(0,5)]
print "random_days = ", ",".join(random_days)
sorted_days = sorted(random_days, key=lambda x:days[x])
print "sorted_days = ", ",".join(sorted_days)
