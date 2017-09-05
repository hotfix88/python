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
import time





#载入收件人信息
def loadDataSet(fileName,sp=','):      #general function to parse tab -delimited floats
    data = []
    id=[]
    pwd=[]
    name=[]
    addr=[]
    num = 0
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split(sp)
        data.append(curLine)
        id.append(curLine[0])
        pwd.append(curLine[1])
        name.append(curLine[2])
        addr.append(curLine[3])    
        num +=1     
    return data,id,pwd,name,addr,num
#格式
# xuran	PV52K#nF	徐然	xuran@js.chinamobile.com
# fengyang	OS83U#JU	冯杨	fengyangsgs@js.chinamobile.com
# xuyuwei	9PRAC#WS	许毓玮	xuyuwei@js.chinamobile.com
# yuanpeng	SSX33#ks	袁鹏	yuanpengsgs@js.chinamobile.com


data,id,pwd,name,addr,num = loadDataSet('all.csv',',')

#发件人和服务器
from_addr = 'fengyangsgs@js.chinamobile.com'
password = 'Fy955785'
smtp_server = '172.16.121.102'
count = 0

for i in range(num):

	# 输入收件人地址:
	to_addr = addr[i] #'fengyangsgs@js.chinamobile.com'

	# 收件内容

	NAME = '您好:\n\n'
	NOTICE = '    因安全管理检查需要，暂将您的账号密码修改为强密码，并临时关闭密码修改功能，开放时间另行通知。\n 数据分析平台新地址：http://10.32.111.51:8080/analyse/bin/analyse.html\n'
	ID   = '账号:'
	idr  =  id[i]#'fengyangsgs'
	PWD  = '密码:'
	pwdr =  pwd[i]
	DATE = "\n------------------------------\n电渠数据分析组 %s \n"  %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"

	msg = MIMEText(NAME+NOTICE+ID+idr+'\n'+PWD+pwdr+'\n'+DATE, 'plain', 'utf-8')

	#标题
	msg['Subject'] = Header(u'您好，您的电渠数据分析平台密码已经更新，请惠存！', 'utf-8').encode()

	import smtplib
	server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()

	time.sleep(0.5)
	count+=1

print '-------------------'
print count
print 'send!'
