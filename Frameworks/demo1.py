from selenium import webdriver
#browser exposes an executable file
#through selenium test we need to invoke the executable file which will then invoke actual browser
driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:\\geckodriver.exe")
#driver=webdriver.Ie(executable_path="C:\\IEDriverServer")
driver.maximize_window()
driver.get("https://www.travelxite.de/")
#get method to hit url on browser

print(driver.title)
print(driver.current_url)
#driver.close()#current window  will get closed
#driver.quit() # all the windows gets closed

driver.get("https://www.travelxite.de/Dashboard/Index")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
