import selenium
from selenium import webdriver
import time
import os

elements = []	#Declaring array
#create browser instance for firefox
browser = webdriver.Firefox()
browser.get("https://www.facebook.com")

def read_file():
	input_file = open("id_elements_facebook.txt",'r') #Open the file
	i=0	#increment the counter for array
	for line in input_file:
		line = line.rstrip()	
		elements.append(line)	#adding elements to array
	#input_file.close()
	
def login():
	email_element = browser.find_element_by_id("email")
	email_element.send_keys("pk158@hotmail.com")
	pwd_element = browser.find_element_by_id("pass")
	pwd_element.send_keys("satya_pav123")
	browser.find_element_by_id("loginbutton").click()
	
def logout():
	browser.find_element_by_id("userNavigationLabel").click()
	browser.find_element_by_id("logout_form").click()
	
def assert_id(id):
	assert browser.find_element_by_id(id)

#Function to read the output and create html code.
def generate_output(name):	
	try:
		output_file = open(name,'r')
		file_h = open("assertion_webpage.html",'w')
		for list_words in output_file:
			list_of_words = list_words.split(',')
			file_h.write("<html><body><table border=2 cellpadding = 2><tr>list_of_words[0]<td></td><td>list_of_words[1]</td></tr></table></body></html>")	
	except:
		print "HTML output can not be genenrated"
read_file()
login()
file_name = raw_input("Enter the file name for printing output: ")
try:
	file_output = open(file_name,'w')
	for id_values in elements:
		try:
			assert_id(id_values)
			file_output.write("Pass,"+id_values+"\n")
		except:
			file_output.write("Failed,"+id_values+"\n")
except:
	print "The file is unable to write"
else:
	file_output.close() #Close the file write
	generate_output(file_name)
#logout()
#Reading the output file
	
	
	


	
