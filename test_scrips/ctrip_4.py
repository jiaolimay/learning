# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from com.login import login,search_car,train_type,train_book

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://passport.ctrip.com/user/login?")
# com.common.id(driver,'nloginname').send_keys('11111111111')
# com.common.id(driver,'npwd').send_keys('11111111111')
# com.common.id(driver,'nsubmit').click()
login(driver,'11111111111','1234123412a')
time.sleep(4)
# driver.get('https://trains.ctrip.com/TrainBooking/SearchTrain.aspx###')

'''改用search_car'''
# time.sleep(2)
# id('notice01').clear()
# time.sleep(2)
# id('notice01').send_keys(u'杭州')
# time.sleep(2)
# id('notice08').clear()
# time.sleep(2)
# id('notice08').send_keys(u'上海')
# time.sleep(2)
# xpath(driver,'//*[@id="searchtype"]/li[1]').click()
# js(driver,'2019-4-30')
# time.sleep(5)
# id(driver,'searchbtn').click()

# time.sleep(2)
# search_car(driver,'2019-4-30',u'杭州',u'上海')
#
# time.sleep(5)
# train_type(driver,'3')
#
# time.sleep(3)
# train_book(driver,"G7358")


# css(driver,'#appd_wrap_close').click()
# css(driver,'#tbody-01-K5260 > div.railway_list > div.w6 > div:nth-child(1) > a').click()
# time.sleep(4)
# css(driver,'#pasglistdiv > div:nth-child(1) > ul > li:nth-child(2) > input').clear()
# time.sleep(4)
# css(driver,'#pasglistdiv > div > ul > li:nth-child(2) > input').send_keys(u'张三')
# time.sleep(2)
# css(driver,'#pasglistdiv > div > ul > li:nth-child(3) > input').clear()
# time.sleep(2)
# css(driver,'#pasglistdiv > div > ul > li:nth-child(3) > input').send_keys('111111111111111111')
# time.sleep(4)
# driver.quit()