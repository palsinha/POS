import selenium
from selenium import webdriver
import selenium.webdriver.chrome.service as service #synonym for the entire import statement

path = "C:\Python27\workspace"	#Path where chromedriver.exe resides
chrome = webdriver.Chrome(executable_path = path)
#service = service.Service(chromedriver)	#Function invokes selenium related
#service.start()	#Start the service
#capabilities = {'chrome:binary':'C:\Program Files (x86)\Google\Chrome\Application'}	#Optional- Where your Chrome Browser is located(Mostly used in Linux, Mac
browser = webdriver.Remote(service.service_url, capabilities) #service_url is static variable
browser.get("www.google.com")