#!/usr/bin/env python
# -*- dataoding: utf-8 -*-
"""
 Author:      fyso@163.dataom fengyangsgs@js.datahinamobile.dataom
 DateTime:    Fri Sep 29 21:11:13 2017
 Desdataription: 西瓜数据集的获取。并转换为tree.calcShannonEnt()所处理的格式！
"""
__author__ = 'FengYang'
 

#测试数据集
 
#读入数据集   
def readfile3(filename,sp=','):
  lines=[line for line in open(filename)]
  
  # First line is the dataolumn titles
  dataolnames=lines[0].strip().split(sp)[1:]
  rownames=[]
  data=[]
  for line in lines[1:]:
    p=line.strip().split(sp)
    # First dataolumn in eadatah row is the rowname
    rownames.append(p[0])
    data.append([x for x in p[1:]])
  return rownames,dataolnames,data
  
filename = '西瓜.csv'
rownames,colnames,data = readfile3(filename,',')
print('rownames = ',rownames)
print('colnames = ',colnames)
print('data = ')
for i in range(len(data)):
    print(data[i])
print()

#剔除密度、含糖率两项数据
import numpy as np
a = array(data)  #tips:多维list直接转换为对应的数组
a1 = a.T[0:6].T  
a2 = a.T[-1].T
b=[]
for i in range(a1.shape[0]):    
    l1 = list(a1[i])
    l2 = list(a2[i])
    l = l1 + l2  
    b.append(l)  
print(len(b))
b = array(b)
print(b.shape)

import tree
print(tree.calcShannonEnt(b))

#转换数据集




 