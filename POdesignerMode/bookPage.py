# _*_ coding:utf-8 _*_
from POdesignerMode.Base import base
import time


class book(base):
    def close(self):
        time.sleep(10)
        return self.by_css('#appd_wrap_close')

    def train(self, train_no):
        # return self.by_xpath('//div[contains(@id,"' + train_no + '")]/div[1]/div[6]/div[1]/a')
        return self.by_xpath('//div[contains(@id,%s)]/div[1]/div[6]/div[1]/a'%(train_no))

    def book_train(self,train_no):
        self.train(train_no).click()
