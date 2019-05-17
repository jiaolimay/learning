# _*_ coding:utf-8 _*_
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get('https://www.51zxw.net/list.aspx?page=3&cid=615')

# 获取句柄，句柄可以识别窗口
selenium_index=driver.current_window_handle
sleep(2)

driver.find_element_by_partial_link_text('4-3').click()
sleep(4)

driver.switch_to.window(selenium_index)
sleep(3)
driver.find_element_by_partial_link_text('4-21').click()
sleep(3)

driver.quit()