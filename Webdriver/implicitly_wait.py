# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep,ctime

# r加上绝对路径
path=r"C:\Users\ml980245\PycharmProjects\learning\POdesignerMode\test.py"

driver=webdriver.Firefox()
driver.get('https://www.baidu.com')
sleep(2)

driver.implicitly_wait(5)

try:
    print(ctime())
    driver.find_element_by_css_selector('#kw11').send_keys('Python')
    driver.find_element_by_css_selector('#su').click()
except NoSuchElementException as msg:
    print(msg)
finally:
    print(ctime())

sleep(3)
driver.quit()