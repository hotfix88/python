#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso
 DateTime:    Thu May 10 14:49:33 2018
 Description: Description
"""
__author__ = 'Fyso'
from pandas import read_csv
# 使用Pandas导入CSV数据
filename = '1.csv'
names = ['Time of payment']
data = read_csv(filename, names=names)
print(type(data),data.shape)


import matplotlib.pyplot as plt
import numpy as np
plt.plot(data)

# 绘图
#plt.show()

data.hist()


#data.plot(kind='density', subplots=True, layout=(1,1), sharex=False)
#plt.show()

#data.plot(kind='box', subplots=True, layout=(1,1), sharex=False)
#plt.show()


print(data.min())
print(data.max())


