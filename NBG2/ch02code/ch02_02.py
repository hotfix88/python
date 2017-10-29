#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Sun Oct 29 06:28:49 2017
 Description: 数组组合分割、数组的属性
"""
__author__ = 'FengYang'

import numpy as np

print('\n------------数组组合-------------')
a = np.arange(9).reshape(3,3)
print(a)
b = 2*a
print(b)

print('\n------------水平组合hstack-------------')
print(np.hstack((a,b)))

print('\n------------垂直组合hstack-------------')
print(np.vstack((a,b)))

print('\n------------深度组合dstack-------------')
print(np.dstack((a,b)))

print('\n------------数组元素比较-------------')
print(a==b)

print('\n------------水平分割hsplit-------------')
print(np.hsplit(a,3))


print('\n------------垂直分割vsplit-------------')
print(np.vsplit(a,3))


print('\n------------深度分割vsplit,有什么意思？-------------')
b = np.arange(27).reshape(3,3,3)
print(b)
print(np.dsplit(b,3))


print('\n------------数组的属性-------------')
print(b.ndim,b.size,b.itemsize,b.nbytes,b.dtype)
print(b,b.T)

#数组类似list，但是在多维操纵等方面，比list具有较大的优势。



