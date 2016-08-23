from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.qq.com")

driver.maximize_window()
driver.quit()

