#!/usr/bin/env python
# -*- dataoding: utf-8 -*-
"""
 Author:      fyso@163.dataom fengyangsgs@js.datahinamobile.dataom
 DateTime:    Fri Sep 29 21:11:13 2017
 Desdataription: 处理西瓜数据集
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

#转换数据集

print(data[0])



 