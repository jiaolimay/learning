# _*_ coding:utf-8 _*_
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get('http://www.51zxw.net/')

cookie=driver.get_cookies()
print(cookie)
print(cookie[0])

driver.add_cookie({'name':'51zxw','value':'www.51zxw.net'})
for cookie in driver.get_cookies():
    print('%s--%s' %(cookie['name'],cookie['value']))


driver.quit()