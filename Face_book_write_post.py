import selenium
from selenium import webdriver
import time
import os
#from selenium.webdriver.common.alert import Alert

browser = webdriver.Firefox()
browser.get("https://www.facebook.com")

def login():
	email_element = browser.find_element_by_id("email")
	email_element.send_keys("pk158@hotmail.com")
	pwd_element = browser.find_element_by_id("pass")
	pwd_element.send_keys("satya_pav123")
	browser.find_element_by_id("loginbutton").click()

def write_post():
	browser.find_element_by_id("pageLogo").click()
	#profile_name = browser.find_element_by_link_text("Satya Pavan").click()
	#browser.find_element_by_class_name("_9lb").click()
	#text = browser.find_element_by_id("u_jsonp_2_a")
	#text.send_keys("This is a sample post")	
	#browser.find_element_by_class_name("_42ft _42fu _11b selected _42g-").click()
login()
write_post()
