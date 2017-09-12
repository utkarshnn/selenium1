from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get("https://stage.raptorsupplies.com/index.php/customer/account/login/") 
time.sleep(30)
username = browser.find_element_by_xpath("//input[@id='email']")
password = browser.find_element_by_xpath("//input[@title='Password']")
username.send_keys("utkarsh@nextgenesolutions.com")
password.send_keys("Blue01roby")
login_attempt = browser.find_element_by_xpath("//button[@class='action login primary']")
login_attempt.submit()
