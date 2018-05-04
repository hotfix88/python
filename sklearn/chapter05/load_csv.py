#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso
 DateTime:    Thu May  3 09:17:56 2018
 Description: Description
"""
__author__ = 'Fyso'

from csv import reader
import numpy as np
# 使用标准的Python类库导入CSV数据
filename = 'pima_data.csv'
with open(filename, 'rt') as raw_data:
    readers = reader(raw_data, delimiter=',')
    x = list(readers)
    data = np.array(x).astype('float')
    print(type(data),data.shape)
    
    
from numpy import loadtxt
# 使用numpy导入CSV数据
filename = 'pima_data.csv'
with open(filename, 'rt') as raw_data:
    data = loadtxt(raw_data, delimiter=',')
    print(type(data),data.shape)    
    
    
from pandas import read_csv
# 使用Pandas导入CSV数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
print(type(data),data.shape)
#推荐使用这个！


#X = array[0:3, 0:8] #前3行，前8列
#Y = array[0:3, 8]  #前3行，第9列


data1 = data[0:10]
print(type(data1),data1.shape)




