#!/usr/bin/python
# written by andrewt@cse.unsw.edu.au as a 2041 lecture example
# print the courses being taken by each student enrolled in the specified courses

import sys,re
if len(sys.argv) < 3:
    print >>sys.stderr, "Usage: %s <enrollment_file> <course_codes>" % sys.argv[0]
    sys.exit(1)
enrollment_file = sys.argv.pop(1)

course_names = {}
for line in open("course_codes"):
    line = line.rstrip()
    code = line[0:8]
    name = line[9:]
    course_names[code] = name

courses = {}
names = {}
for line in open(enrollment_file):
    (course,upi,name) = line.split("|")[0:3]
    m = re.match(r'(.*),\s+(.*\S)', name)
    if m:
    	name = m.group(2) + " " + m.group(1)
    if upi in courses:
        courses[upi] += " " + course
    else:
        courses[upi] = course
    names[upi] = name.rstrip()
    

for course in sys.argv[1:]:
    for upi in courses.keys():
        student_courses = courses[upi].split()
        if course not in student_courses:
            continue
        print "%s is taking"%(names[upi])
        for course in student_courses:
            print "%s %s"%(course, course_names[course])
