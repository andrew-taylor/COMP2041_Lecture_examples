#!/usr/bin/python
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# fetch a web page remove HTML tags, constants,
# text between script blank lines
# and print non-empty lines

import sys, re, subprocess
# there are python libraries which provide a  better way to fetch web pages
for url in sys.argv[1:]:
    webpage = subprocess.Popen(["wget","-q","-O-",url], stdout=subprocess.PIPE).communicate()[0]
    webpage = re.sub(r'(?i)<script>.*?</script>', '', webpage)
    webpage = re.sub(r'(?i)<style>.*?</style>', '', webpage)
    webpage = re.sub(r'&\w+;', ' ', webpage)
    webpage = re.sub(r'<[^>]*>', '', webpage)
    webpage = re.sub(r'\n\s*\n', '\n', webpage)
    print webpage,
