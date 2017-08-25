'''
Created on 2017年8月25日

@author: thomas
'''
from sys import exit
from urllib.request import urlopen
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def ip():
    url='http://1212.ip138.com/ic.asp'
    code=urlopen(url).read().decode('gbk')
    pattern = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    ip=re.findall(pattern, str(code))
    return ip
    
mail_host='smtp.126.com'
mail_user='ztonearth'
mail_pass='1234qwer'
sender = 'ztonearth@126.com'
receivers = ['ztonearth@126.com']
message=MIMEText(ip()[0],'plain','utf-8')
message['From'] = Header("ztonearth",'utf-8')
message["To"] = Header("ztonearth",'utf-8')
subject='IP地址更新'
message['Subject']=Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error:邮件发送失败")

