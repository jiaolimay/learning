# _*_ coding:utf-8 _*_
from LoginPage import *
from selenium import webdriver

driver=webdriver.Firefox()
username='51zxw'
password='123456'

test_user_login(driver,username,password)
driver.find_element().get_attribute()
sleep(3)
driver.quit()