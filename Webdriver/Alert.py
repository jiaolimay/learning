# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Firefox()
driver.get('https://www.baidu.com')

driver.find_element_by_link_text('设置').click()
sleep(5)
driver.find_element_by_link_text('搜索设置').click()
sleep(2)

driver.find_element_by_link_text('保存设置').click()
alert=driver.switch_to.alert()
sleep(2)
alert.accept()
sleep(2)

driver.quit()