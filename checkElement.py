import selenium
from selenium import webdriver
import time
import os

#chromedriver = "C:\
#os.environ["PATH"] = chromedriver

#Take input from user or command line

#create browser instance for firefox
browser = webdriver.Firefox()	
browser.get("https://www.facebook.com/")	#open webpage

#email_element = browser.find_element_by_id("email")	#finds my element
#email_element.send_keys(input_id)	#input to pass

try: 
  assert  browser.find_element_by_id("email")
except:
  print "test Failed:Email Element Not loaded"
else:
  print "Element Found. test Passed"
