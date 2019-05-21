# _*_ coding:utf-8 _*_
from selenium import webdriver

def browser():
    driver=webdriver.Firefox()
    # driver=webdriver.Chrome()
    # driver=webdriver.Ie()

    # driver.get('https://www.baidu.com/')

    return driver

if __name__ == '__main__':
    browser()