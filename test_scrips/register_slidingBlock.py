# _*_ coding:utf_8 -*_
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Chrome()
driver.maximize_window()

driver.find_element_by_css_selector('#agr_pop > div.pop_footer > a.reg_btn.reg_agree').click()
time.sleep(2)
source = driver.find_element_by_css_selector('#slideCode > div.cpt-drop-box > div.cpt-drop-btn')
print(source.size)
'''size:{'height': 40, 'width': 40}'''
ele = driver.find_element_by_css_selector('#slideCode > div.cpt-drop-box > div.cpt-bg-bar')
print(ele.size)
'''size:{'height': 40, 'width': 300}'''
ActionChains(driver).drag_and_drop_by_offset(source,ele.size['width'],-source.size['height']).perform()



