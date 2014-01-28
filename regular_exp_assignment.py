#! /usr/bin/python

import re
import sys

input1 = raw_input("Enter number you want to test")

def find_tel_num_india(inp):
	pattern = re.compile("^91[1-9]\d\d\d\d\d\d\d\d\d$")
	try:
		assert pattern.match(inp)
	except:
		print "It is not an Indian Number"
	else:
		print "Indian number"
		
def find_tel_num_germany(inp):
	pattern = re.compile("^0\d\d\d\d\d\d\d\d\d\d$")
	try:
		assert pattern.match(inp)
	except:
		print "It is not an German Number"
	else:
		print "German number"
		
def find_toll_free(inp):
	pattern = re.compile("^1-800-\d\d\d\d\d\d\d$")
	try:
		assert pattern.match(inp)
	except:
		print "It is not an Toll free Number"
	else:
		print "Toll free number"
		
find_tel_num_india(input1)
find_tel_num_germany(input1)
find_toll_free(input1)