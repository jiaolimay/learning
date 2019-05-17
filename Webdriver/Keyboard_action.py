# _*_ coding:utf-8 _*_
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get('https://www.baidu.com')

driver.find_element_by_css_selector('#kw').send_keys('Python')
sleep(2)
# 全选
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'a')

# 复制或者剪切
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'c')
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'x')

driver.get('https://www.sogou.com')
sleep(2)
# 粘贴
driver.find_element_by_css_selector('.sec-input').send_keys(Keys.CONTROL,'v')
sleep(2)

sleep(3)
driver.quit()
