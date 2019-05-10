# _*_ coding:utf_8 -*_
from selenium import webdriver
from pywinauto.application import Application
'''
python 运行默认环境中是否加入了selenium
'''
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://mail.qq.com/cgi-bin/loginpage")

time.sleep(2)
driver.switch_to.frame('login_frame')
driver.find_element_by_id('u').send_keys('xxx')
driver.find_element_by_id('p').send_keys('xxxxx')
time.sleep(2)
driver.find_element_by_id('login_button').click()
time.sleep(2)
driver.find_element_by_id('composebtn').click()
'''
python 找不到元素注意是否在不同的frame
'''
driver.switch_to.frame('mainFrame')
driver.find_element_by_id('subject').send_keys('test')
'''
python 中文件路径注意写法，存在转义字符的问题
'''
'''下面3行为第1种附件上传'''
# driver.find_element_by_name('UploadFile').send_keys('C:/Users/ml980245/Desktop/jmeter_test/test.csv')
# driver.switch_to.default_content()
# driver.find_element_by_id('readmailbtn_link').click()

'''下面3行为第2种附件上传,需要生成exe文件'''
# driver.find_element_by_id('AttachFrame').click()
# os.system("C:/Users/ml980245/PycharmProjects/learning/appendix/qq_attach.exe")

'''下面为第3种附件上传'''
driver.find_element_by_id('AttachFrame').click()
time.sleep(3)
app = Application()
'''locate by title and class name'''
app = app.connect(title_re='Open',class_name='#32770')
app['Open']['Edit1'].type_keys("C:\\Users\\ml980245\\Desktop\\jmeter_test\\test.csv")
time.sleep(2)
app['Open']['Button1'].click()

