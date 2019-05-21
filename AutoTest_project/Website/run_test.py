import unittest
from model.funtion import  *
from venv_learn.Lib import HTMLTestRunner
import time

report_dir='./test_report'
test_dir='./test_case'

print('start to run test case ')
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_Login.py')
print('discover is ', discover)
now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+'result.html'

print('start to write report')
with open(report_name,'wb') as f:
    runner=HTMLTestRunner.HTMLTestRunner(stream=f, title='Test Report',description='localhost login test',verbosity=2)
    runner.run(discover)
    f.close()

print('find the latest report')
latest_report=latest_report(report_dir)

print('send email report..')
send_mail(latest_report)

print('Test end!')