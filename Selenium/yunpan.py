from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("F:\python\chromedriver.exe")
driver.get("http://yunpan.360.cn")

driver.maximize_window()
right_click = driver.find_element_by_id("xx")

ActionChains(driver).context_click(right_click).perform()

above = driver.find_element_by_id("id")

ActionChains(driver).move_to_element(above).perform()