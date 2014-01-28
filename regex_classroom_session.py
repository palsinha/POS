#! /usr/bin/python

import re
import sys

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
d = sys.argv[4]
e = sys.argv[5]
f = d+e

pattern = re.compile("^www\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.gov$")
#Pattern for matching email address
#pattern2 = re.compile("[a-zA-Z0-9]+(\.{0,1}|_{0,1})[a-zA-Z0-9]*@[a-zA-Z]+\.com$") #Similar to the regex below.
pattern2 = re.compile("[a-zA-Z0-9]+(\.|_)?[a-zA-Z0-9]*@[a-zA-Z]+\.com$")
pattern3 = re.compile("^[1-9]\d\d\d\d$")	#Matches five digit postal code only.	What other validations?
pattern4 = re.compile("^1\([2-9]\d\d\)\\s?\d\d\d-\d\d\d\d$")


result = pattern.match(a)
result2 = pattern2.match(b)
result3 = pattern3.match(c)
result4 = pattern4.match(f)
#result5 = pattern5.match(b)

print result
print result2
print result3
print result4
