import selenium
from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
def open_browser():	
	browser.get("https://www.freecharge.in/")

def recharge_without_login():
	mobile_number = browser.find_element_by_id("serviceNumber")
	mobile_number.send_keys("9538439908")
	amount = browser.find_element_by_id("amount")
	amount.send_keys("350")
	browser.find_element_by_id("operatorSelectBoxIt").click()
	#operator = Select(browser.find_element_by_id("operator"))
	#operator.select_by_visible_text("Airtel").click()
	browser.find_element_by_id("rechargeFormSubmit").click()
	
def select_coupons():
	browser.find_element_by_xpath("//*[@id='couponContinue']").click()
	
open_browser()
recharge_without_login()
select_coupons()