from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.126.com")

driver.find_element_by_class("idInput").clear()
driver.find_element_by_class("idInput").send_keys("username")

driver.find_element_by_class("pwdInput").clear()
driver.find_element_by_class("pwdInput").send_keys("password")
driver.find_element_by_id("lginBtn").click()
