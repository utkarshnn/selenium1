import unittest
import xlrd
from selenium import webdriver

class fblogin(unittest.TestCase):
  def setUp(self):
    self.driver=webdriver.Firefox()
    self.driver.get("https://stage.raptorsupplies.com/index.php/customer/account/login/")
    self.driver.maximize_window()
    
  def test_fblogin(self):
    driver=self.driver
    wb=xlrd.open_workbook("test.xls")
    sheetname = wb.sheet_names()
    sh1 = wb.sheet_by_index(0)
    i=0
    
    while (i<2):
      rownum=(i)
      rows = sh1.row_values(rownum)
      UserName = driver.find_element_by_xpath("//input[@title='Email']")
      driver.find_element_by_xpath("//input[@title='Email']").send_keys(rows[0, 1])
      driver.implicitly_wait(10)
      print("The Gbouser name [" + rows[0, 1] + "] is entered")
      Password = driver.find_element_by_xpath("//input[@title='Password']")
      driver.find_element_by_xpath("//input[@title='Password']").send_keys(rows[1, 1])
      print("The Password [" + rows[1, 1] + "] is entered")
      driver.implicitly_wait(10)
      driver.back()
      
      i=i+1
      Login = driver.find_element_by_xpath("//button[@id='send2']").click()
      driver.implicitly_wait(10)

  def tearDown(self):
    self.driver.quit()
    if __name__ == "__main__":
      unittest.main()
