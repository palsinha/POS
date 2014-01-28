from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox() #Creating instance
driver.get("https://login.yahoo.com/") #onload event has fired
new_account = driver.find_element_by_id("signUpBtn")  #finding an element
new_account.click()
f_name = driver.find_element_by_id("first-name")
f_name.send_keys("Pallavi")
l_name = driver.find_element_by_id("last-name")
l_name.send_keys("Sinha")
yid = driver.find_element_by_name("yahooid")
yid.send_keys("palsinha")
pwd = driver.find_element_by_name("password")
pwd.send_keys("halloween")
mobile = driver.find_element_by_name("mobile")
mobile.send_keys("(408)442-7656")
month = Select(driver.find_element_by_name("mm"))
month.select_by_value("8")
date = Select(driver.find_element_by_name("dd"))
date.select_by_value("10")
year = Select(driver.find_element_by_name("yyyy"))
year.select_by_value("1987")
radio=driver.find_element_by_id("female")
radio.click()
submit = driver.find_element_by_name("yui_3_7_3_2_1389427267508_5486")
submit.click()