# _*_ coding:utf-8 _*_
from unittest_t.Test_Project.calculator import *
from unittest_t.Test_Project.StartEnd import *

class Test_sub(Setup_tearDown):
    def test_sub(self):
        j=Math(5,3)
        self.assertEqual(j.sub(),2)
    def test_sub1(self):
        j=Math(8,8)
        self.assertEqual(j.sub(),0)