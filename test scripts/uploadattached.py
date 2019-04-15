from selenium import webdriver
'''
python 运行默认环境中是否加入了selenium
'''
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
driver.get("https://mail.qq.com/cgi-bin/loginpage")
driver.maximize_window()
time.sleep(2)
driver.switch_to.frame('login_frame')
driver.find_element_by_id('u').send_keys('1069712644')
driver.find_element_by_id('p').send_keys('13679125394A')
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

'''下面3行为第2种附件上传'''
driver.find_element_by_id('AttachFrame').click()
os.system("C:/Users/ml980245/Desktop/jmeter_test/qq_attach.exe")
