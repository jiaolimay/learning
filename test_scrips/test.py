# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# driverF = webdriver.Firefox()
# driverF.get('https://www.baidu.com')
#
# driverE = webdriver.Ie()
# driverE.get('https://www.baidu.com')

'''鼠标悬停'''
ActionChains(driver).move_to_element(driver.find_element_by_link_text('设置')).perform()
time.sleep(2)
driver.find_element_by_class_name('setpref').click()
time.sleep(2)
'''dropdown box'''
# driver.find_element_by_css_selector('#nr > option:nth-child(2)').click()
# Select(driver.find_element_by_name('NR')).select_by_index(2)
# Select(driver.find_element_by_name('NR')).select_by_value('20')
# Select(driver.find_element_by_name('NR')).select_by_visible_text('每页显示50条')
print(Select(driver.find_element_by_name('NR')).options)
'''依次点击'''
for len in range(len(Select(driver.find_element_by_name('NR')).options)):
    time.sleep(2)
    Select(driver.find_element_by_name('NR')).select_by_index(len)
