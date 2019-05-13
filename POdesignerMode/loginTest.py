# _*_ coding:utf-8 _*_
import time, unittest
from venv_learn.Lib import HTMLTestRunner
from selenium import webdriver
import POdesignerMode
from POdesignerMode.LoginPage import loginPage
from POdesignerMode.searchPage import searchPage
from POdesignerMode.bookPage import book
import sys
import os

print('sys,path: ',sys.path)
sys.path.append('C:\\Users\\ml980245\\PycharmProjects\\learning\\POdesignerMode')
sys.path.append('C:\\Users\\ml980245\\PycharmProjects\\learning')


'''用classmethod装饰过，改写setUp 为 setUpClass tearDownClass 在所有case执行前后只执行一次setup和teardown '''
class loginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://passport.ctrip.com/user/login?")

    def test_01(self):
        lo = loginPage(self.driver)
        url = lo.login('111', '111111111')
        print('lo.login() is : ', url)
        self.assertEqual(url, 'https://my.ctrip.com/home/myinfo.aspx')

    def test_02(self):
        time.sleep(2)
        self.driver.get('https://trains.ctrip.com/TrainBooking/SearchTrain.aspx###')
        sp = searchPage(self.driver)
        sp.search('杭州', '上海', '2019-05-31')

    def test_03(self):
        time.sleep(3)
        bk = book(self.driver)
        bk.book_train('K526')
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(loginTest('test_01'))
    suite.addTest(loginTest('test_02'))
    suite.addTest(loginTest('test_03'))
    print('current path is :', os.getcwd())
    # filepath = os.getcwd()[:-14]
    # filename = filepath+'report\\'+'report.html'
    # print(filename)
    fp = open('C:/Users/ml980245/PycharmProjects/learning/report/report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告',description=u'第一个python unittest',verbosity=2)
    runner.run(suite)
    fp.close()





