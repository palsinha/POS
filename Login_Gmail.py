from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox() #Creating instance
driver.get("http://mail.google.com") #onload event has fired
uname = driver.find_element_by_id("Email")  #finding an element
uname.send_keys("palsinha2006")
pwd = driver.find_element_by_id("Passwd")
pwd.send_keys("GoodWill1987")
driver.find_element_by_id("signIn").click()
driver.find_element_by_xpath("//*[@id=':57']/div/div").click() #give css path instead of xpath
to_address	= driver.find_element_by_name("to")
to_address.send_keys("amanmohla@gmail.com")
subject	= driver.find_element_by_name("subjectbox")
subject.send_keys("Regarding Test Script")
subject.send_keys(Keys.TAB)
compose_mail = driver.find_element_by_class_name("Am Al editable LW-avf")	
compose_mail.send_keys("This is a test mail sent through Automation Script. Please reply if you receive it.")
#driver.close()
