# _*_ coding:utf_8 -*_
from ddt import ddt,data,unpack
import unittest
import os

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

reportPath = PATH('../report/chromereport')

'''setup and teardown 是每个testcase 都会运行一次'''
@ddt
class TestSe(unittest.TestCase):
    def setUp(self):
        print('This is the setup')

    @data(2, 3)
    def test_01(self, value):
        print('test_01 value is ', value)
        self.assertEqual('selenium', 'appium')

    @data(4, 5)
    def test_02(self, value):
        print('test_02 value is ', value)
        self.assertEqual('tim', 'tim')

    @data([6, 7], [8, 9])
    @unpack
    def test_03(self, first, second):
        print('test_03 first value', first)
        print('test_03 second value', second)
        self.assertEqual('a', 'abc')

    def tearDown(self):
        print('This is the teardown')


if __name__ == '__main__':
    unittest.main()
