#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso
 DateTime:    Thu May  3 09:35:09 2018
 Description: Description
"""
__author__ = 'Fyso'

from pandas import read_csv
# 显示数据最初10行
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)

print('--------------shape & head------------')
peek = data.head(10)
print(peek)
print(type(peek),peek.shape)
print(type(data),data.shape)

#
print('--------------dtypes------------')
print(data.dtypes)

#
print('------------describe--------------')
from pandas import set_option
set_option('display.width', 80)
# 设置数据的精确度
set_option('precision', 2)
print(data.describe())

#
print('--------------dtypes------------')
print(data.dtypes)

#
print('--------------groupby------------')
print(data.groupby('class').size())

#相关度在-1和1之间。
print('--------------correlations------------')
print(data.corr(method='pearson'))
corr_pearson = data.corr(method='pearson')
corr_kendall = data.corr(method='kendall')
corr_spearman = data.corr(method='spearman')
set_option('precision', 2)
print('corr_pearson = %.2f'%corr_pearson['plas']['preg'])
print('corr_kendall = %.2f'%corr_kendall['plas']['preg'])
print('corr_spearman = %.2f'%corr_spearman['plas']['preg'])
#当相关性较高的时候，会影响liner、logistic的性能，应该进行降维处理。

#负数为左偏，正数为右偏
print('--------------skew------------')
print(data.skew())