import selenium
from selenium import webdriver
import time
import os

browser = webdriver.Firefox() #Creating browser instance
file_values = []	#Creating an array

#Open the browser
def open_browser():	
	browser.get("https://www.gmail.com/")

#Open the file to read the test inputs
def open_file():
	input_file = open("input_values.csv",'r')
	for line in input_file:
		line = line.rstrip()
		file_values.append(line)
		#print file_values
	input_file.close()
	
def username(uname):
	username = browser.find_element_by_id("Email")
	username.send_keys(uname)

def passwd(pwd):
	password = browser.find_element_by_id("Passwd")	
	password.send_keys(pwd)
	
def stay_signed_in(inp):
	stay_signed_in = browser.find_element_by_id("PersistentCookie")
	if inp == "uncheck":
		stay_signed_in.click()

def login():
	browser.find_element_by_id("signIn").click()

def logout():
	browser.find_element_by_class_name("gb_J").click()
	browser.find_element_by_id("gb_71").click()	
	browser.get("https://www.gmail.com/")
	
open_file()
open_browser()
for id_values in file_values:
	words = id_values.split(',')
	try:
		browser.implicitly_wait(5)
		username(words[0])
		passwd(words[1])
		stay_signed_in(words[2])
		login()
		assert browser.find_element_by_link_text("+Pallavi")	#Text of the person's name (To assert whether it has logged into to next page or not)	
	except:
		print "Login Failed for following values: "+words[0]+","+words[1]+","+words[2]
		browser.get("https://www.gmail.com/")
	else:
		print "Login Passed for following values: "+words[0]+","+words[1]+","+words[2]
		logout()
		
	
	
