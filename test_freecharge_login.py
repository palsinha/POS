import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://www.freecharge.com")
login = driver.find_element_by_id("navbarLoginBtn")
login.click()
#elem.send_keys("9538439916")
emailId = driver.find_element_by_id("emailId")
emailId.send_keys("palsinha@gmail.com")
pwd = driver.find_element_by_id("loginPassword")
pwd.send_keys("GoodWill1987")
driver.implicitly_wait(60)
sign_in = driver.find_element_by_id("loginButton")
sign_in.click()
