from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import csv, sys


class Browse(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.webpagetest.org"
        self.verificationErrors = []

    def getCSVData(fileName):
        rows = []
	datafile = open('test.csv', "rb")
        reader = csv.reader(dataFile)
        next(reader)
        for row in reader:
            rows.append(row)
        return rows

    def test_browse(self):

            driver = self.driver
            driver.get(self.base_url + "/")
            driver.find_element_by_link_text("WebPageTest").click()
            Select(driver.find_element_by_id("location")).select_by_visible_text("Paris, France (Chrome,Firefox,IE 11)")
            driver.find_element_by_css_selector("option[value=\"Paris_FR\"]").click()
            driver.find_element_by_id("url").clear()
            driver.find_element_by_id("url").send_keys(row[0])
            driver.find_element_by_id("number_of_tests").clear()
            driver.find_element_by_id("number_of_tests").send_keys("1")
            driver.find_element_by_name("submit").click()

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
