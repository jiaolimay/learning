# _*_ coding:utf-8 _*_
from POdesignerMode.Base import base
import time

class searchPage(base):
    def leave(self):
        return self.by_id('notice01')

    def arrive(self):
        return self.by_id('notice08')

    def date(self):
        return self.by_id('dateObj')

    def btn(self):
        return self.by_id('searchbtn')

    def click_blank(self):
        return self.by_xpath('//*[@id="searchtype"]/li[1]')

    def search_js(self,value):
        js = "document.getElementById('dateObj').value ='%s'" % (value)
        return self.driver.execute_script(js)

    def search(self,leave,arrive,leave_date):
        self.leave().clear()
        self.leave().send_keys(leave)
        self.arrive().clear()
        self.arrive().send_keys(arrive)
        self.search_js(leave_date)
        self.click_blank().click()
        self.btn().click()
        time.sleep(5)
        print(self.driver_url())
        return self.driver_url()



