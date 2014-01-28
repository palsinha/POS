import selenium
from selenium import webdriver
import time
import os

#chromedriver = "C:\
#os.environ["PATH"] = chromedriver

#Take input from user or command line
input_id = raw_input("Enter your email id: ")	
input_pwd = raw_input("Enter your password: ")

#create browser instance for firefox
browser = webdriver.Firefox()	
browser.get("https://www.facebook.com/")	#open webpage

email_element = browser.find_element_by_id("email")	#finds my element
email_element.send_keys(input_id)	#input to pass
pass_element = browser.find_element_by_name("pass") 
pass_element.send_keys(input_pwd)
browser.find_element_by_id("loginbutton").click()
try:
	assert browser.title == "Facebook"
except:
	print "Invalid Credentials"
else:
	browser.find_element_by_link_text("Pallavi Sinha").click()
	browser.find_element_by_id("pageLogo").click()
	search_box = browser.find_element_by_xpath("//*[@id='u_0_9']/div[3]")
	search_box = search_box.send_keys("Priyanka Sinha")
	#browser.find_element_by_link_text("Priyanka Sinha").click()
	browser.find_element_by_name("mercurymessages").click()
	browser.back()
	browser.find_element_by_name("notifications").click()
	browser.find_element_by_link_text("Home").click()
	browser.find_element_by_id("navItem_app_4748854339").click()


