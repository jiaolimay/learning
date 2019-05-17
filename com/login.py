# _*_ coding:utf_8 -*_
from com.common import id,js,css,xpath

def login(driver,user,passwd):
    try:
        id(driver, 'nloginname').send_keys(user)


    except:
        print('no username')
    id(driver, 'npwd').send_keys(passwd)
    id(driver, 'nsubmit').click()

def search_car(driver,day,leave,arriver):
    id(driver, 'notice01').clear()
    id(driver, 'notice01').send_keys(leave)
    id(driver, 'notice08').clear()
    id(driver, 'notice08').send_keys(arriver)
    xpath(driver,'//*[@id="searchtype"]/li[1]').click()
    js(driver,day)
    id(driver,'searchbtn').click()

def train_type(driver,no):
    css(driver,'#resultFilters01 > dl:nth-child(1) > dd:nth-child('+no+') > label > span').click()

def train_book(driver,train_no):
    css(driver, '#appd_wrap_close').click()
    # xpath(drive,'//div[starts-with(@id,"tbody-01-G7358")]/div[1]/div[6]/div[1]/a').click()
    # xpath(driver, '//div[contains(@id,"G7358")]/div[1]/div[6]/div[1]/a').click()
    xpath(driver, '//div[contains(@id,"' + train_no + '")]/div[1]/div[6]/div[1]/a').click()
