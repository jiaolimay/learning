# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Firefox()
driver.get('https://www.baidu.com')
sleep(2)
driver.find_element_by_css_selector('#kw').send_keys('Selenium 自学网')
# 显示等待
element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'su')))
element.click()
# 显示等待 异常raise TimeoutException(message, screen, stacktrace)
element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'su123')))
element.click()

sleep(3)
driver.quit()


