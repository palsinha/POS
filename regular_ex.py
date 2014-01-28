#! /usr/bin/python

import re
import sys

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
d = sys.argv[4]
e = sys.argv[5]
#Pattern for matching email address
pattern = re.compile("[a-zA-Z0-9]+@[a-zA-Z]+\.[com]+") 	#Matches one single email id. how to restrict single com??
#Pattern for identifying a number in US
pattern2 = re.compile("1\-\d\d\d\-\d\d\d\-\d\d\d\d")	#Matches one US number only. 
#Pattern for identifying a US pincode 
pattern3 = re.compile("9\d\d\d\d$")	#Matches five digit postal code only.	What other validations?
#Pattern for identifying website with .co.in domain
pattern4 = re.compile("[www]+\.[a-z]+\.[co]+\.[in]+")
#Pattern for identifying website with .gov domain
pattern5 = re.compile("[www]+\.[a-z]+\.[gov]+")
#Results
result = pattern.match(a)
result2 = pattern2.match(b)
result3 = pattern3.match(c)
result4 = pattern4.match(d)
result5 = pattern5.match(e)

print result
print result2
print result3
print result4
print result5