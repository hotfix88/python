#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Sat Oct 28 21:54:30 2017
 Description: 数组的基本情况
"""
__author__ = 'FengYang'

import numpy as np

print('\n------------数组-------------')
a = np.arange(5)
print(a,a.dtype,type(a),a.shape)

b = np.array([0,2,4,6,8])
print(b,b.dtype,type(b),b.shape)

print(a+b,a-b,a*b,2*a)

a[0] = 100
print(a)

print('\n------------列表list-------------')
l = list(range(5))
print(l,type(l))
print(l+l,3*l)

print('\n------------多维数组-------------')
m = np.array([np.arange(2),np.arange(2)])
print(m,m.dtype,type(m),m.shape)
m[0,1] = 100
print(m) 

n = np.array([np.arange(3),np.arange(3),np.arange(3)])
print(n,n.dtype,type(n),n.shape)

u = np.array([[1,2],[3,4]])
print(u,u.dtype,type(u),u.shape)


print('\n------------数据类型-------------')
v = np.arange(7,dtype='int64')
print(v,v.dtype,type(v),v.shape)

w = np.array([0,1,2,3,4,5,6],dtype='int64')
print(w,w.dtype,type(w),w.shape)

print(u.dtype.itemsize,v.dtype.itemsize)

print('\n------------改变数组维度reshape-------------')
x = np.arange(24).reshape(2,3,4)
print(x,x.dtype,type(x),x.shape)




