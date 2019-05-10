# _*_ coding:utf-8 _*_
import time, unittest,HtmlTestRunner,os
from selenium import webdriver
from POdesignerMode.LoginPage import loginPage
from POdesignerMode.searchPage import searchPage
from POdesignerMode.bookPage import book

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
    filepath = os.getcwd()+'\\'+'report.html'
    print(filepath)
    fp = open(filepath, 'w')
    runner = HtmlTestRunner.HTMLTestRunner(stream=fp, output=os.getcwd(),report_title=u'自动化测试报告',report_name='report_name',descriptions=u'第一个python unittest')
    runner.run(suite)
    fp.close()




