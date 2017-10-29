#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Sun Oct 29 07:04:53 2017
 Description: 基本的读写文件操作，基本的统计操作
"""
__author__ = 'FengYang'

import numpy as np

print('\n-----------------读写文件------------------')
i = np.eye(2,dtype='int32')
print(i)
np.savetxt('eye.txt',i)

i2 = np.loadtxt('eye.txt')
print(i2)

print('\n-----------------读写csv文件------------------')
#AAPL	28-01-2011	 	344.17	344.4	333.53	336.1	21144800
#股票名称 日期  空格  开盘  最高 最低 收盘 成交量
#d = np.loadtxt('data.csv',delimiter=',',unpack=False)
c,v  = np.loadtxt('data.csv',delimiter=',',usecols=(6,7),unpack=True)
print(c,type(c),c.size,c.dtype,c.shape)
print(v)

print('\n-----------------统计操作------------------')
 
print(np.mean(c)) #算数平均值
print(np.average(c,weights=v)) #加权平均值


h,l = np.loadtxt('data.csv',delimiter=',',usecols=(4,5),unpack=True) 
print(np.max(h),np.min(l),np.ptp(h),np.ptp(l))
print('median = ',np.median(h))
N = len(h)


#max 最大，min最小，ptp极差，mean均值，average可计算加权均值，
#median中位值,当偶数个数值时，这个中位值是计算出来的
s = np.msort(h)
print('sorted = ',s)

print('var = ',np.var(h))
print('\n-----------------操作------------------')
