# -*- coding:utf-8 -*-
from unittest import TestCase,TestSuite,TestLoader
import unittest
import HtmlTestRunner
import os
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))

reportPath = PATH('../report/chromereport')

class test_se(TestCase):
    def setUp(self):
        pass

    def test_01(self):
        self.assertEqual('selenium', 'appium')

    def test_02(self):
        self.assertEqual('tim', 'tim')

    def test_03(self):
        self.assertEqual('a', 'abc')

    def tearDown(self):
        pass


if __name__ == '__main__':
    # unittest.main()
    '''
    suite = TestSuite()
    suite.addTest(test_se('test_01'))
    suite.addTest(test_se('test_02'))
    suite.addTest(test_se('test_03'))
    '''
    test_dir = PATH('../test_scrips')
    print('test_dir is :' , test_dir)
    tests = unittest.defaultTestLoader.discover(test_dir,pattern='unit_*.py')
    print('report path is : ',reportPath)
    # fp = open(reportPath,'wb')
    runner = HtmlTestRunner.HTMLTestRunner(output=reportPath,report_title='automatically test report')
    '''
    runner.run(suite)
    '''
    runner.run(tests)
    # fp.close()


