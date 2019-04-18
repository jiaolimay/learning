# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Chrome()
driver.maximize_window()

'''login'''
driver.get("https://passport.ctrip.com/user/login?")
def id(element):
    return driver.find_element_by_id(element)

def css(element):
    return driver.find_element_by_css_selector(element)

def xpath(element):
    return driver.find_element_by_xpath(element)

def js(value):
    # jsvalue = "document.getElementById('dateObj').value ="+"'"+value+"'"
    # print(jsvalue)
    jsvalue = "document.getElementById('dateObj').value ='%s'" %(value)
    driver.execute_script(jsvalue)

id('nloginname').send_keys('11111111111')
id('npwd').send_keys('11111111111a')
id('nsubmit').click()
time.sleep(4)
driver.get('https://trains.ctrip.com/TrainBooking/SearchTrain.aspx###')
time.sleep(2)
id('notice01').clear()
time.sleep(2)
id('notice01').send_keys(u'杭州')
time.sleep(2)
id('notice08').clear()
time.sleep(2)
id('notice08').send_keys(u'上海')
time.sleep(2)
xpath('//*[@id="searchtype"]/li[1]').click()
js('2019-4-30')
time.sleep(3)
id('searchbtn').click()
time.sleep(7)
css('#appd_wrap_close').click()
time.sleep(2)
css('#tbody-01-K5260 > div.railway_list > div.w6 > div:nth-child(1) > a').click()
time.sleep(4)
css('#pasglistdiv > div:nth-child(1) > ul > li:nth-child(2) > input').clear()
time.sleep(4)
css('#pasglistdiv > div > ul > li:nth-child(2) > input').send_keys(u'11111111111')
time.sleep(2)
css('#pasglistdiv > div > ul > li:nth-child(3) > input').clear()
time.sleep(2)
css('#pasglistdiv > div > ul > li:nth-child(3) > input').send_keys('11111111111')
time.sleep(2)
driver.quit()


