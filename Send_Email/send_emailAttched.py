# _*_ coding:utf-8 _*_
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtpserver='smtp.163.com'

user='xxxxx@163.com'
password='xxxxxx'

sender='xxxxx@163.com'
receivers=['xxxxxx.com','xxxxxx@qq.com']

subject='Web Selenium 自动化测试报告'
content='<html><h1 style="color:red">我要自学网，自学成才</h1></html>'

send_file=open(r'D:\photo\PIC_4307.JPG','rb').read()
att=MIMEText(send_file,'base64','utf-8')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']='attachment;filename="PIC_4307.JPG"'

msgRoot=MIMEMultipart()
msgRoot.attach(MIMEText(content,'html','utf-8'))
msgRoot['Subject']=subject
msgRoot['From']=sender
msgRoot['To']=','.join(receivers)
msgRoot.attach(att)

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print('Start send Email...')
smtp.sendmail(sender,receivers,msgRoot.as_string())
smtp.quit()
print('Send Email end!')
