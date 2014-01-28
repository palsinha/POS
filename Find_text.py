import selenium
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://www.gmail.com")
try:
	element = browser.find_element_by_tag_name("H1")
	#assert browser.pagesource.contains("One account. All of Google.")
	assert element.text == ("One account. All of Google.")
	#print element.text
except:
	print "Text not found"
else:
	print "Text found"