#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Sun Oct 29 08:21:44 2017
 Description: 收益率计算
"""
__author__ = 'FengYang'
import numpy as np

print('\n-----------------收益率计算------------------')
#AAPL	28-01-2011	 	344.17	344.4	333.53	336.1	21144800
#股票名称 日期  空格  开盘  最高 最低 收盘 成交量
c  = np.loadtxt('data.csv',delimiter=',',usecols=(6,),unpack=True)
arr = np.diff(c)
print(c)
print(arr)
returns = arr/c[:-1]
print(returns)
print(np.var(returns))
print(np.std(returns))
print(np.diff(np.log(c)))


print('\n-----------------日期处理及自定义格式------------------')
from datetime import datetime
def datestr2num(s):
   return datetime.strptime(s.decode('ascii'), "%d-%m-%Y").date().weekday()

#第二列值是日期格式字符串，但因为我们是以二进制编码的格式打开第二列值是，
#返回的值字节字符串bytes，所以需要把它便会string，则对字符串解码用函数decode('asii')，
#变成string格式。
dates,close  = np.loadtxt('data.csv',delimiter=',',usecols=(1,6),unpack=True,
                          converters={1:datestr2num})