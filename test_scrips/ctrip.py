# _*_ coding:utf_8 -*_
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Chrome()
driver.maximize_window()

'''login'''
# driver.get("https://passport.ctrip.com/user/login?")
# driver.find_element_by_id('nloginname').send_keys('11111111111')
# driver.find_element_by_id('npwd').send_keys('11111111111')
# driver.find_element_by_id('nsubmit').click()
# time.sleep(5)
driver.get('https://trains.ctrip.com/TrainBooking/SearchTrain.aspx###')

'''中文前要加u'''
time.sleep(2)
driver.find_element_by_id('notice01').clear()
time.sleep(2)
driver.find_element_by_id('notice01').send_keys('杭州')
time.sleep(2)
driver.find_element_by_id('notice08').clear()
time.sleep(2)
driver.find_element_by_id('notice08').send_keys('上海')
time.sleep(2)
'''用JS 把readonly 属性移除'''
driver.execute_script("document.getElementById('dateObj').removeAttribute('readonly')")
driver.find_element_by_id('dateObj').clear()
driver.find_element_by_id('dateObj').send_keys('2019-4-30')
time.sleep(2)
'''输入完日期，搜索按钮被遮挡了，需要额外点击 单程 来显示搜索按钮'''
driver.find_element_by_xpath('//*[@id="searchtype"]/li[1]').click()
time.sleep(5)

driver.find_element_by_id('searchbtn').click()

time.sleep(10)
driver.find_element_by_css_selector('#appd_wrap_close').click()
time.sleep(2)
driver.find_element_by_css_selector('#tbody-01-K5260 > div.railway_list > div.w6 > div:nth-child(1) > a').click()
print(driver.find_element_by_css_selector('#tbody-01-K5260 > div.railway_list > div.w6 > div:nth-child(1) > a').text)
print(driver.find_element_by_css_selector('#tbody-01-K5260 > div.railway_list > div.w1 > div:nth-child(1) > strong').text)
time.sleep(4)
driver.find_element_by_css_selector('#pasglistdiv > div:nth-child(1) > ul > li:nth-child(2) > input').clear()
time.sleep(4)
driver.find_element_by_css_selector('#pasglistdiv > div > ul > li:nth-child(2) > input').send_keys(u'张三')
time.sleep(2)
driver.find_element_by_css_selector('#pasglistdiv > div > ul > li:nth-child(3) > input').clear()
time.sleep(2)
driver.find_element_by_css_selector('#pasglistdiv > div > ul > li:nth-child(3) > input').send_keys('11111111111111111')
time.sleep(2)
driver.find_element_by_css_selector('#contact-mobile').send_keys('11111111111')
time.sleep(2)
driver.find_element_by_css_selector('#UpdatePanel1 > div:nth-child(2) > div > button.btn-pay.big').click()
time.sleep(3)
driver.find_element_by_css_selector('#main_area > div:nth-child(6) > div.tab_area > div.tab_titl > ul > li:nth-child(4)').click()
time.sleep(3)
driver.find_element_by_css_selector('#main_area > div:nth-child(6) > div.tab_area > div.btn_area > a:nth-child(1)').click()
time.sleep(8)
driver.find_element_by_css_selector('#J_tip_qr > a').click()
time.sleep(3)
driver.find_element_by_css_selector('#J_tLoginId').send_keys('3333')
# driver.quit()

def id(element,value):
    return driver.find_element_by_id(element)
id('nloginname').send_keys('11111111111')
id('npwd').send_keys('11111111222')
id('nsubmit').click()
