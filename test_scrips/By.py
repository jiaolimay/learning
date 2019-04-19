# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
driver = webdriver.Chrome()

'''隐性等待，隐性等待对整个driver的周期都起作用，所以只要设置一次即可，等到了就立即执行，等不到就等到最大时间，不行就抛出异常 '''
driver.implicitly_wait(10)

driver.get('https://www.baidu.com/')
# time.sleep(2)
driver.find_element(By.ID,'kw').send_keys('test'+Keys.ENTER)
time.sleep(5)
driver.quit()

'''获取当前工作目录,C:/Users/ml980245/PycharmProjects/learning/test_scrips/By.py'''
os.getcwd()