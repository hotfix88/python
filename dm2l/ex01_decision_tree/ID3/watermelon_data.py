#!/usr/bin/env python
# -*- dataoding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Fri Sep 29 21:11:13 2017
 Desdataription: 西瓜数据集的获取。并转换为tree.calcShannonEnt()所能处理的格式！
"""
__author__ = 'FengYang'
print(__file__) 
print(__doc__)


#测试数据集
 
#读入数据集   
def readfile(filename,sp=','):
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
rownames,colnames,data = readfile(filename,',')


#剔除密度、含糖率两项数据
import numpy as np
a = np.array(data)  #tips:多维list直接转换为对应的数组
a1 = a.T[0:6].T  
a2 = a.T[-1].T
data=[]
for i in range(a1.shape[0]):    
    l1 = list(a1[i])
    l2 = list(a2[i])
    l = l1 + l2  
    data.append(l)  
    
#剔除密度、含糖率两项colnames
c = colnames[0:6]
c.append(colnames[-1])
colnames = c


#明细数据打印
#print('rownames = ',rownames)
#print('colnames = ',colnames)
#print('data = ')
#for i in range(len(data)):
#    print(data[i])
    
    
waterMenlon = data
waterMenlonArray = np.array(data) #转换为数组
waterMenlonLabels = colnames[:-1]
waterMenlonLabelsArray = np.array(waterMenlonLabels)

print('data len = ',len(waterMenlon))
print('data dim = ',len(waterMenlon[0]))
print('--------------------------------------')
print('数据：标签 = waterMenlonLabels')
print('数据：数据 = waterMenlon')
print('数据：数组格式标签 = waterMenlonLabelsArray')
print('数据：数组格式数据 = waterMenlonArray')


#import tree
#print('结果熵 = ',tree.calcShannonEnt(data))
#我误以为这个是最后的熵，其实不是。
#for i in range(1,len(data.T)+1):
#    print(colnames[-i],tree.calcShannonEnt(data.T[-i]))
 





 