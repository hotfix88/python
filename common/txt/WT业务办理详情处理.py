#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Fri Nov 17 11:18:38 2017
 Description: Description
"""
__author__ = 'FengYang'

filename = 'D:/0.工作记录/重点工作/20171020-号卡漏斗分析/Webtrends数据/在线选号成型数据1111-1115/1111-1115数据清洗结果/out.xls'
file = open(filename, 'r')

data = [line for line in file]
print('data len is : ',len(data))


#找到空值
for i in range(10000):
    if data[i].split('\t')[3] == '' :
        print(i,data[i]);