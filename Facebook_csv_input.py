import selenium
from selenium import webdriver
import time
import os

elements = []	#Declaring array

#create browser instance for firefox
browser = webdriver.Firefox()
browser.get("https://www.facebook.com")

def read_file():
	input_file = open("Facebook_elements_input.csv",'r') #Open the file
	#i=0	#increment the counter for array
	for line in input_file:
		line = line.rstrip()	
		elements.append(line)	#adding elements to array
	input_file.close()
	
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

def assert_name(name):
	assert browser.find_element_by_name(name)

def assert_class_name(class_name):
	assert browser.find_element_by_class_name(class_name)
	
def assert_link_text(text):
	assert browser.find_element_by_link_text(text)

#Function to read the output and create html code.
def generate_output(name):	
	try:
		output_file = open(name,'r')
		file_h = open("csv_input_html_output.html",'w')
		file_h.write("<html><body><table border=2 cellpadding = 2><th>Element Name</th><th>Element Type</th><th>Result</th>")
		for list_words in output_file:
			list_of_words = list_words.split(',')
			list_of_words[2] = list_of_words[2].rstrip()
			if list_of_words[2] == "Failed":
				file_h.write("<tr><td bgcolor='red'>"+list_of_words[0]+"</td><td bgcolor='red'>"+list_of_words[1]+"</td><td bgcolor='red'>"+list_of_words[2]+"</td></tr>")
			else:
				file_h.write("<tr><td>"+list_of_words[0]+"</td><td>"+list_of_words[1]+"</td><td>"+list_of_words[2]+"</td></tr>")
		file_h.write("</table></body></html>")
	except:
		print "HTML output can not be genenrated"
	else:		
		output_file.close()

read_file()
login()
file_name = raw_input("Enter the file name for printing output: ")
try:
	file_output = open(file_name+".txt",'w')
	
	for id_values in elements:
		i_words = id_values.split(',')
		try:
			if i_words[3]=="id":
				assert_id(i_words[4])
			elif i_words[3]=="link_text":
				assert_link_text(i_words[4])
			elif i_words[3]=="name":
				assert_name(i_words[4])
			elif i_words[3]=="class":
				assert_class_name(i_words[4])
			file_output.write(i_words[4]+","+i_words[3]+",Pass\n")
		except:
			file_output.write(i_words[4]+","+i_words[3]+",Failed\n")
except:
	print "File could not write"
else:
	file_output.close() #Close the file write

generate_output(file_name+".txt")
logout()
