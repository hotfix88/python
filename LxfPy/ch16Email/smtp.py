#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    2017-09-05 15:51:30
 Description: Description
"""
__author__ = 'FengYang'


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.text import MIMEText
import datetime



from_addr = 'fengyangsgs@js.chinamobile.com'
password = 'Fy955785'
smtp_server = '172.16.121.102'



# 输入收件人地址:
to_addr = 'fengyangsgs@js.chinamobile.com'

# 收件内容
NAME = '您好:\n'
ADDR = '数据分析平台新地址：http://10.32.111.51:8080/analyse/bin/analyse.html\n'
ID   = '账号:'
IDr  = 'fengyangsgs'
PWD  = '密码:'
PWDr = 'xw#86tP'
DATE = "%s"  %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"

msg = MIMEText(ADDR+ID+IDr+'\n'+PWD+PWDr+'\n'+DATE, 'plain', 'utf-8')

#标题
msg['Subject'] = Header(u'您好，您的电渠数据分析平台密码已经修改，请惠存！', 'utf-8').encode()

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

