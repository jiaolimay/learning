# _*_ coding:utf-8 _*_
# _*_ coding:utf-8 _*_
import time, unittest
from selenium import webdriver
from POdesignerMode.LoginPage import loginPage
from POdesignerMode.searchPage import searchPage

class loginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://passport.ctrip.com/user/login?")

    def test_01(self):
        lo = loginPage(self.driver)
        url = lo.login('may', '123')
        print('lo.login() is : ',url)
        self.assertEqual(url,'https://my.ctrip.com/home/myinfo.aspx')

    def test_02(self):
        self.driver.get('https://trains.ctrip.com/TrainBooking/SearchTrain.aspx###')
        sp = searchPage(self.driver)
        sp.search('杭州','上海','20190531')


    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
