#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Sat Dec 03 13:02:03 2016  : Administrator

"""

"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
  DateTime:    Sat Sep 30 10:02:16 2017
 Description: 扩展显示任意月份，并改进显示算法
"""


__author__ = 'FengYang'

from matplotlib import pyplot as plt
#import numpy as np


f2 = 'plot_boxer_data_v.csv' #行为月份，列为日期
fr = open(f2)
L = [line.strip().split(',') for line in fr.readlines()] #一行搞定！
#去除第一列
L2=[]
for i in L:
    L2.append(i[1:])
    
L3=[]
for i in range(len(L2)):
    A = []
    for j in range(len(L2[i])):
        A.append(int(L2[i][j]))
    L3.append(A)


fig = plt.figure(figsize=(10,4.2))
plt.boxplot((L3),whis=1)
plt.xticks([y+1 for y in range(len(L3))], 
#  ['Sep', 'Oct', 'Nov','Dec','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep']
['16-09', '16-10', '16-11','16-12','17-01','17-02',
 '17-03','17-04','17-05','17-06','17-07','17-08','17-09']
            )

plt.show()
fr.close()




#后续问题：
##转换为数值型：数组不支持空值转换。
#s = np.array(L,dtype=np.int32)#转数组
#print(s2.dtype)
#s2 = s2.astype(np.int32) #转换为整形，注意！当为空的时候转换会错误！但是置为0会影响数据分布结果。
#print(s2.dtype)





'''
调试区

print(s2.shape)
print(np.median(a0))
data1 = ['1','2','3']
array1 = np.array(data1)
array2 = array1.astype(np.int32)

a=range(1,10)
b=range(2,12)
c=range(3,8)
plt.boxplot((a,b,c))
plt.xlabel('measurement x')

colors = [ 'lightblue', 'lightgreen', 'tan']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
'''

'''
#V1版本
f2 = 'plot_boxer_data.csv'
fr = open(f2)
s = [line.strip().split(',') for line in fr.readlines()] #一行搞定！
a0 = [int(s[i][0]) for i in range(len(s)) if i > 0 and s[i][0] != '']
a1 = [int(s[i][1]) for i in range(len(s)) if i > 0 and s[i][0] != '']
a2 = [int(s[i][2]) for i in range(len(s)) if i > 0 and s[i][0] != '']


fig = plt.figure(figsize=(4,2.2))
plt.boxplot((a0,a1,a2),whis=10)
plt.xticks([y+1 for y in range(3)], ['Sep', 'Oct', 'Nov'])

plt.show()
fr.close()
'''

'''

#----------------------------------
dataMat = mat(kMeans.loadDataSet('testSet.txt'))
#箱子图
plt.boxplot((dataMat[:,0],dataMat[:,1]),whis=10)
plt.show()
plt.boxplot((dataMat[0],dataMat[1],dataMat[2],dataMat[3]),whis=10)
plt.show()
#线图
plot(dataMat)
plt.show()
#散点图
plt.scatter(list(dataMat[:,0]),list(dataMat[:,1]),c='blue',s=25,alpha=0.4,marker='o')
plt.show()



import matplotlib.pyplot as plt
import numpy as np

all_data = [np.random.normal(0, std, 100) for std in range(1, 4)]

fig = plt.figure(figsize=(8,6))

plt.boxplot(all_data,
            notch=False, # box instead of notch shape
            sym='rs',    # red squares for outliers
            vert=True)   # vertical box aligmnent

plt.xticks([y+1 for y in range(len(all_data))], ['x1', 'x2', 'x3'])
plt.xlabel('measurement x')
t = plt.title('Box plot')
plt.show()
'''