# _*_ coding:utf_8 -*_
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pytesseract
from PIL import Image,ImageEnhance
import time
import os
'''screenshot need pillow package'''

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://user.qunar.com/passport/login.jsp')

time.sleep(4)
driver.save_screenshot('qu.png')
print(driver.find_element_by_id('vcodeImg').get_attribute('src'))
imgcode = driver.find_element_by_id('vcodeImg')
print('imgcode: ', imgcode)
print('imgcode.location: ', imgcode.location)
print('imgcode.size: ', imgcode.size)
'''location: {'x': 1112, 'y': 312}'''

'''和电脑显示缩放比例有关系，例如我的电脑缩放比例是125%'''
left = imgcode.location['x']*1.25
top = imgcode.location['y']*1.25
right = left+imgcode.size['width']*1.25
bottom = top+imgcode.size['height']*1.25

print('left, top, right, bottom: ', left, top, right, bottom)
im = Image.open('qu.png')
'''def crop(self, box=None):'''
im = im.crop((left, top, right, bottom))
im.save('t.png')





