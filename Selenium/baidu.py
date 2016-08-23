#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome("F:\python\chromedriver.exe")

first_url = "http://www.baidu.com"
print("first accees %s") %first_url
driver.get(first_url)

second_url = "http://news.baidu.com"
print("second access %s") %second_url
driver.get(second_url)

print "back to %s" %(first_url)
driver.back()

print "forward to"
driver.forward()