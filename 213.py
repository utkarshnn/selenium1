__author__ = "Mahesh"

from selenium import webdriver

'''
Simple gmail login using selenium with python
'''
driver=webdriver.Firefox


# Enter google home page
driver.get("https://www.google.com/?gws_rd=ssl")
driver.get_screenshot_as_file("/home/utkarsh/Desktopgooglehomepage.png")
# click on gmail button
driver.find_element_by_class_name("gb_P").click()
driver.get_screenshot_as_file("/home/utkarsh/Desktopgmailbutton.png")
# click on gmail email box
driver.find_element_by_xpath("//A[@class='gmail-nav__nav-link gmail-nav__nav-link__sign-in'][text()='Sign In']").click()
driver.get_screenshot_as_file("/home/utkarsh/Desktopsign-in.png")
# driver.find_element_by_xpath("//INPUT[@id='Email']")
# Enter emailid
driver.find_element_by_xpath("//INPUT[@id='Email']").send_keys("selenium")
driver.get_screenshot_as_file("/home/utkarsh/Desktopemail.png")
#click on next button
driver.find_element_by_xpath("//INPUT[@id='next']").click()
# enter password
driver.find_element_by_id("Passwd").send_keys("python")
driver.get_screenshot_as_file("/home/utkarsh/Desktoppassword.png")
# click on signin button
driver.find_element_by_id("signIn").click()
driver.get_screenshot_as_file("/home/utkarsh/Desktopclick.png")
driver.quit()

