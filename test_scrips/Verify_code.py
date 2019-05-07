# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://pan.baidu.com/')
time.sleep(20)
cookies = driver.get_cookies()
print(cookies)

coo = [{'domain': '.baidu.com', 'expiry': 1588663771.163165, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': '73EE4FFE9B89391407EB8EAD18CC8EB5:FG=1'}]
for cookie in coo:
    driver.add_cookie(cookie)
time.sleep(5)
driver.get('https://pan.baidu.com/')