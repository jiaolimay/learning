# _*_ coding:utf-8 _*_
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get('http://www.51zxw.net/')
sleep(3)

# 通过option标签定位
driver.find_elements_by_tag_name('option')[1].click()

# 通过CSS属性来定位
driver.find_element_by_css_selector('[value="3"]').click()

# 通过Select定位
# 定位到整个大的选项框
select=Select(driver.find_element_by_css_selector('[name="CookieDate"]'))
select.select_by_index(1)
sleep(2)
select.select_by_visible_text('第二条')
select.select_by_value('2')