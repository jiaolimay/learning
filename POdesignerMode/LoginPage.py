# _*_ coding:utf_8 -*_
from POdesignerMode.Base import base
import time

class loginPage(base):
    def username(self):
        return self.by_id('nloginname')

    def passwd(self):
        return self.by_id('npwd')

    def btn(self):
        return self.by_id('nsubmit')

    def login(self,user,passwd):
        self.username().send_keys(user)
        self.passwd().send_keys(passwd)
        self.btn().click()
        time.sleep(5)
        print(self.driver_url())
        return self.driver_url()


