from selenium import webdriver

validateText="option3"
driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("option3")
driver.find_element_by_id("alertbtn").click()
alert= driver.switch_to.alert
alertText=alert.text
assert validateText in alertText
alert.accept()

#alert.dismiss()

