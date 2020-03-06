#js DOM can access any elements on web page just like how selenium does
#selenium hav ea method to execute javascript code in it
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text)#- user entered value cant print
print(driver.find_element_by_name("name").get_attribute("value"))

print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton= driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();",shopButton)
#by default selenium does not have scroll method.we have to rely on javascript 
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
