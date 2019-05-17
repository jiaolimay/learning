# _*_ coding:utf-8 _*_
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get('http://www.51zxw.net/')

driver.get_screenshot_as_file(r'C:\Users\ml980245\PycharmProjects\learning\Webdriver\51zxw.jpg')
sleep(2)

driver.get('http://www.baidu.com')
driver.get_screenshot_as_file(r'C:\Users\ml980245\PycharmProjects\learning\Webdriver\baidu.jpg')
sleep(2)

driver.quit()