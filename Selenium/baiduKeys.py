from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("F:\python\chromedriver.exe")
driver.get("http://www.baidu.com")

keywords = driver.find_element_by_id("kw")
keywords.send_keys("seleniumm")

keywords.send_keys(Keys.BACK_SPACE)
keywords.send_keys(Keys.SPACE)
keywords.send_keys("教程".decode())

print "test"
keywords.send_keys(Keys.CONTROL,"a")
keywords.send_keys(Keys.CONTROL, "x")

keywords.send_keys(Keys.CONTROL, "v")
keywords.send_keys(Keys.ENTER)


