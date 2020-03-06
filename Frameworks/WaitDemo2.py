import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

list =[]
list2=[]
driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count=len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count==3

buttons=driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print((list))
#//div[@class='product-action']/button/parent::div/parent::div/h4

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait= WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))

veggies=driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    list2.append(veg.text)
print(list2)
assert list2==list2

originalAmt=driver.find_element_by_css_selector(".discountAmt").text

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))

discountlAmt=driver.find_element_by_css_selector(".discountAmt").text
#assert int(discountlAmt)< int(originalAmt)

print(driver.find_element_by_css_selector("span.promoInfo").text)

sum = 0
amounts= driver.find_elements_by_xpath("//tr/td[5]/p")
for amount in amounts:
   sum=sum+ int(amount.text)
print(sum)

totalAmt=int(driver.find_element_by_css_selector(".totAmt").text)
assert sum==totalAmt






