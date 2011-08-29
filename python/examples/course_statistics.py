#!/usr/bin/python
# written by andrewt@cse.unsw.edu.au as a 2041 lecture example
# for each courses specified as arguments
# print a summary of the other courses taken by students in this course

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
        courses[upi].append(course)
    else:
        courses[upi] = [course]
    names[upi] = name.rstrip()
    

for course in sys.argv[1:]:
    n_taking = {}
    n_students = 0
    for upi in courses.keys():
        if course not in courses[upi]:
            continue
        n_students += 1
        for c in courses[upi]:
            if c in n_taking:
                n_taking[c] += 1
            else:
                n_taking[c] = 1
    for c in sorted(n_taking.keys(), key=lambda x: n_taking[x]):
        print "%5.1f%% of %s students take %s %s"%(100*n_taking[c]/n_students, course, c, course_names[c])
