#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    2017-09-05 15:51:30
 Description: Description
"""
__author__ = 'FengYang'

# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
# import smtplib


# 首先，我们来构造一个最简单的纯文本邮件：
from email.mime.text import MIMEText
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg = MIMEText('你好，你的密码已经修改 : xw#86tP', 'plain', 'utf-8')


# 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'，
# 最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。





# 然后，通过SMTP发出去：
# 输入Email地址和口令:
# from_addr = raw_input('From: ')
from_addr = 'fengyangsgs@js.chinamobile.com'
# password = raw_input('Password: ')
password = 'Fy955785'

# 输入SMTP服务器地址:
# smtp_server = raw_input('SMTP server: ')
smtp_server = '172.16.121.102'

# 输入收件人地址:
# to_addr = raw_input('To: ')
to_addr = 'fengyangsgs@js.chinamobile.com'

# msg['From'] = _format_addr(u'DZQD')
# msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
# msg['Subject'] = Header(u'你好，你的密码已经修改', 'utf-8').encode()

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

