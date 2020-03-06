from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
#iframe,frameset, frame

#frameid or frame name or index value
driver.switch_to.frame("mce_0_ifr")

driver.find_element_by_css_selector("body[id='tinymce']").clear()
driver.find_element_by_css_selector("body[id='tinymce']").send_keys("I am able to automate it")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
