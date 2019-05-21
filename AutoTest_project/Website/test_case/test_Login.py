import unittest
from model import funtion,myunit
from page_object.LoginPage import *
from time import sleep

class LoginTest(myunit.StartEnd):
    def test_login1_normal(self):
        '''username and password are normal'''
        print('test_login1_normal is start test...')
        po=LoginPage(self.driver)
        po.Login_action('51zxw','123456')
        sleep(3)
        self.assertEqual(po.type_loginPass_hint(),'我的空间')
        funtion.insert_img(self.driver,'51zxw_login1_normal.png')
        print('test_login1_normal test end!')

    def test_login2_PasswdError(self):
        '''username is ok, password error'''
        print('test_login2_PasswdError is start test...')
        po=LoginPage(self.driver)
        po.Login_action('51zxw','11111')
        sleep(3)
        self.assertEqual(po.type_loginFail_hint(),'')
        funtion.insert_img(self.driver,'test_login2_PasswdError.png')

    def test_login3_empty(self):
        '''username and password are empty'''
        print('test_login3_empty is start test...')
        po=LoginPage(self.driver)
        po.Login_action('','')
        sleep(3)
        self.assertEqual(po.type_loginFail_hint(),'')
        funtion.insert_img(self.driver,'test_login3_empty.png')
        print('test_login3_empty end!')

    if __name__ == '__main__':
        unittest.main()