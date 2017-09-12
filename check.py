from selenium import webdriver

firefox = webdriver.Firefox()
firefox.get("https://stage.raptorsupplies.com/index.php/catalog/product/view/id/797104/s/grainger-approved-bin-storage-cabinet-797104/category/1093/");
transactionElements = firefox.find_elements_by_css_selector("#inputattribute");
for element in transactionElements:
    element.click()

