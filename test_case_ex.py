import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):		#Testcase class is inherited from unittest. Inheriting this clas => this is a test case.

    def setUp(self):							#Part of initialization. This method will be called before every test function.
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver					#Creates a local reference to driver object created in setUp method.
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)	#Similar to assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Google", driver.title)

    def tearDown(self):							#The tearDown method will get called after every test method
        self.driver.close()

if __name__ == "__main__":
    unittest.main()