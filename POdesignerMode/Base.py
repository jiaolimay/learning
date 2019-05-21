# _*_ coding:utf_8 -*_
import time
class base():
    def __init__(self,driver):
        self.driver = driver
    #id
    def by_id(self,ele):
        return self.driver.find_element_by_id(ele)
    #name
    def by_name(self,ele):
        return self.driver.find_element_by_name(ele)
    #css
    def by_css(self,ele):
        return self.driver.find_element_by_css_selector(ele)
    #xpath
    def by_xpath(self,ele):
        return self.driver.find_element_by_xpath(ele)
    #url
    def driver_url(self):
        return self.driver.current_url
