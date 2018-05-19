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
filename = 'load_csv_180518_wxts.csv'
names = ['Store to User']
data = read_csv(filename, names=names)
print(type(data),data.shape,data.min(),data.max(),data.sum()/data.count())
print(data.describe())
data.hist()



filename = 'load_csv_180518_wxtq.csv'
names = ['User to Store']
data = read_csv(filename, names=names)
print(type(data),data.shape,data.min(),data.max(),data.sum()/data.count())
print(data.describe())
data.hist()


