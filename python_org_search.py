from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox() #Creating instance
driver.get("http://www.python.org") #onload event has fired
assert "Python" in driver.title
elem = driver.find_element_by_name("q")  #finding an element
elem.send_keys("selenium")	#Search for Selenium
elem.send_keys(Keys.RETURN)  #Enter Key is hit
assert "Google" in driver.title
driver.close()