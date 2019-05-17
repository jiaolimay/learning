# _*_ coding:utf-8 _*_
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get('http://www.baidu.com')

# using id to locate
driver.find_element_by_css_selector("#kw").send_keys('Selenium 51zxw')

# using class to locate
driver.find_element_by_css_selector('.s_ipt').send_keys('Selenium 51zxw')

# using attribute to locate
driver.find_element_by_css_selector('[autocomplete="off"]').send_keys('Selenium 51zxw')

# 通过层级来定位
driver.find_element_by_css_selector('form#loginForm>ul>input').send_keys('51zxw')

sleep(2)
driver.find_element_by_id('su').click()