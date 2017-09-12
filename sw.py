import unittest
from selenium import webdriver
 
class MyScreenshot(unittest.TestCase):
 
    def setUp(self):
 
        self.driver = webdriver.Firefox()
    
    def test_takescreenshot(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://stage.raptorsupplies.com/')
 
        driver.save_screenshot('/home/utkarsh/firefoximage.png')
 
 
    def tearDown(self):
        self.driver.quit()
 
 
if __name__ == '__main__':
    unittest.main()
