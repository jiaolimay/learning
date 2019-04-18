# -*- coding:utf-8 -*-
import time

def id(driver,ele):
    time.sleep(2)
    return driver.find_element_by_id(ele)

def css(driver,element):
    time.sleep(2)
    return driver.find_element_by_css_selector(element)

def xpath(driver,element):
    time.sleep(2)
    return driver.find_element_by_xpath(element)

def js(driver,value):
    # jsvalue = "document.getElementById('dateObj').value ="+"'"+value+"'"
    # print(jsvalue)
    jsvalue = "document.getElementById('dateObj').value ='%s'" %(value)
    driver.execute_script(jsvalue)

# def login(driver,user,passwd):
#     id(driver, 'nloginname').send_keys(user)
#     id(driver, 'npwd').send_keys(passwd)
#     id(driver, 'nsubmit').click()
#
# def search_car(driver,day,leave,arriver):
#     id(driver, 'notice01').clear()
#     id(driver, 'notice01').send_keys(leave)
#     id(driver, 'notice08').clear()
#     id(driver, 'notice08').send_keys(arriver)
#     xpath(driver,'//*[@id="searchtype"]/li[1]').click()
#     js(driver,day)
#     time.sleep(3)
#     id(driver,'searchbtn').click()

