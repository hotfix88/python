#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    2017-09-05 16:10:23
 Description: Description
"""
__author__ = 'FengYang'




from email.mime.text import MIMEText

msg = MIMEText('您好，电渠数据分析平台账号密码已经修改 : xw#86tP', 'plain', 'utf-8')



from_addr = 'fengyangsgs@js.chinamobile.com'

password = 'Fy955785'


smtp_server = '172.16.121.102'

# 输入收件人地址:
to_addr = 'fengyangsgs@js.chinamobile.com'


# msg['Subject'] = Header(u'你好，你的密码已经修改', 'utf-8').encode()

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
