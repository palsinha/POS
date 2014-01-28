import selenium
from selenium import webdriver
import time
import os
#from selenium.webdriver.common.alert import Alert
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver import ActionChains

#create browser instance for firefox and Chrome
browser = webdriver.Firefox()
browser.get("https://www.facebook.com")

def login():
	email_element = browser.find_element_by_id("email")
	email_element.send_keys("pk158@hotmail.com")
	pwd_element = browser.find_element_by_id("pass")
	pwd_element.send_keys("satya_pav123")
	browser.find_element_by_id("loginbutton").click()
	
def logout():
	browser.find_element_by_id("userNavigationLabel").click()
	browser.find_element_by_id("logout_form").click()
	
def upload_photo():
	browser.find_element_by_id("pageLogo").click()
	#profile_name = browser.find_element_by_link_text("Satya Pavan").click()
	browser.find_element_by_link_text("Add Photos/Video").click()
	browser.implicitly_wait(10)
	browser.find_element_by_link_text("Upload Photos/Video").click()
	upload_file = browser.find_element_by_name("composer_unpublished_photo[]")
	upload_file.send_keys("C:\Python27\workspace\Tree.jpg")
	browser.implicitly_wait(20)
	browser.find_element_by_id("js_90").click() 
login()
upload_photo()
browser.implicitly_wait(30)
logout()

