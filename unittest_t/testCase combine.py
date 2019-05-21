# _*_ coding:utf-8 _*_
from unittest_t.calculator import *
import unittest

class Test_StratEnd(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

@unittest.skip("skip Testadd")
class Testadd(Test_StratEnd):
    def test_add(self):
        j=Math(5,5)
        self.assertEqual(j.add(),10)

@unittest.skipIf(4>3,"skip Testsub")
class Testsub(Test_StratEnd):
    def test_sub(self):
        i=Math(10,5)
        self.assertEqual(i.sub(),5)


if __name__ == '__main__':
    unittest.main()


