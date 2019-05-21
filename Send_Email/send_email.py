# _*_ coding:utf-8 _*_
import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver='smtp.163.com'

user='xxxxxx.com'
password='xxxxxx'

sender='xxxxxx.com'
receiver='xxxxxx.com'

subject='Web Selenium 自动化测试报告'
content='<html><h1 style="color:red">我要自学网，自学成才</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']='xxxxxx@163.com'
msg['To']='xxxxxx.com'

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print('Start send Email...')
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
print('Send Email end!')
