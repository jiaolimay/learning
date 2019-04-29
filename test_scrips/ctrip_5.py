# -*- coding:utf-8 -*-
from selenium import webdriver
import time,os
from com.login import login,search_car,train_type,train_book
from com.excel_opera import read_excel
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))

excelpath = PATH('../appendix/testdata.xls')

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://passport.ctrip.com/user/login?")
username = read_excel(excelpath,0,0)[1]
password = read_excel(excelpath,0,1)[1]
leave = read_excel(excelpath,0,2)[1]
arrive = read_excel(excelpath,0,3)[1]
day = read_excel(excelpath,0,4)[1]

print(username,password)
login(driver,username,password)
time.sleep(4)
driver.get('https://trains.ctrip.com/TrainBooking/SearchTrain.aspx###')
search_car(driver,day,leave,arrive)