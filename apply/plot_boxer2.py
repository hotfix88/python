#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    Mon Mar 12 16:42:29 2018
 Description: 用于电渠客户数质态分析
"""
__author__ = 'FengYang'

from matplotlib import pyplot as plt
#import numpy as np


f2 = 'plot_boxer2.csv' #行为月份，列为 网/掌/短/电渠/
fr = open(f2)
L = [line.strip().split(',') for line in fr.readlines()] #一行搞定！
#去除第一列
L2=[]
for i in L:
    L2.append(i[1:])
    
#转置    
L3=[]
for i in range(len(L2)):
    A = []
    for j in range(len(L2[i])):
        A.append(int(L2[i][j]))
    L3.append(A)


fig = plt.figure(figsize=(10,4))
plt.boxplot((L3),whis=10) #whis 表示异常值判断范围
plt.xticks([y+1 for y in range(len(L3))], ['NET','APP','SMS','DQ'])

for i in range(len(L3)):
    name = ['NET','APP','SMS','DQ']
    fig = plt.figure(figsize=(4,4))
    plt.boxplot((L3[i]),whis=10) #whis 表示异常值判断范围
    plt.xticks([y+1 for y in range(len(L3))],name[i] )





            
#['网厅','掌厅','短厅','电渠']
#  ['Sep', 'Oct', 'Nov','Dec','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep']
#['16-09', '16-10', '16-11','16-12','17-01','17-02', '17-03','17-04','17-05','17-06','17-07','17-08','17-09']


plt.show()
fr.close()