#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Wed Sep 27 22:07:32 2017
 Description: tree.py test
"""
__author__ = 'FengYang'

import tree

print('-----------------------------------')

myDat,labels = tree.createDataSet()
print (myDat) 
print (labels) 

print( tree.calcShannonEnt(myDat)) 

print('----------------修改某个值-----------------') 
myDat[0][-1]='maybe'
print( myDat) 
print (tree.calcShannonEnt(myDat)) 

print( '---------------最小熵------------------') 
myDat = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'yes'],
               [0, 1, 'yes'],
               [0, 1, 'yes']]
print ( myDat) 
print ( tree.calcShannonEnt(myDat)   ) 

myDat = [[1, 1, 'no'],
               [1, 1, 'no'],
               [1, 1, 'no'],
               [1, 1, 'no'],
               [1, 1, 'no']]
print( myDat) 
print( tree.calcShannonEnt(myDat) )  


print( '---------------最大熵------------------') 

myDat = [[1, 1, 'yes'],
               [1, 1, 'no'],
               [1, 0, 'yee'],
               [0, 1, 'sss'],
               [0, 1, 'OK']]
print( myDat) 
print( tree.calcShannonEnt(myDat)  ) 


myDat = [[1, 0, 'yes'],
               [1, 1, 'no'],
               [0, 0, 'yee'],
               [0, 1, 'sss'],
               [0, 1, 'OK']]
print( myDat) 
print( tree.calcShannonEnt(myDat)  ) 

#熵值最后只和第三个值--即分类标示有关！

print( '----------------tips ：append 和 extend 区别-----------------') 
a = [1,2,3]
b = [4,5,6]
print( a,b) 
a.append(b)
print( a,'\n') 

a = [1,2,3]
b = [4,5,6]
print( a,b) 
a.extend(b)
print( a) 

print( '---------------测试函数：------------------') 

myDat,labels = tree.createDataSet()
print (myDat)
print( '(myDat,0,1) = ',tree.splitDataSet(myDat,0,1)) 
print( '(myDat,0,0) = ',tree.splitDataSet(myDat,0,0)) 
print( '(myDat,1,0) = ',tree.splitDataSet(myDat,1,0)) 
print( '(myDat,1,1) = ',tree.splitDataSet(myDat,1,1)) 


print( '-----------------选择最好的数据集划分方式----------------') 

myDat,labels = tree.createDataSet()
print ('The best Feature is : ',tree.chooseBestFeatureToSplit(myDat)) 

print( '-----------------熵值验证----------------') 
myDat,labels = tree.createDataSet()
print( myDat) 
print( tree.calcShannonEnt(myDat)   ) 
















