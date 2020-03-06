from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.travelxite.de/")

#driver.maximize_window()
#ActionChains
action= ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Destinations')]")).perform()
action.move_to_element(driver.find_element_by_xpath("//li[@class='ng-scope']//a[@class='ng-binding'][contains(text(),'Oceania')]")).click().perform()

