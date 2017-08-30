#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-08-26 19:52:08
 Description: 高阶函数之  filter， Python内建的filter()函数用于过滤序列。
"""

print '-----------1 filter -----------'
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的时，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])


print '-----------2 filter -----------'
# 把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['A', '', 'B     ', None, '   C', '  '])


print '-----------3 练习 -----------'

# 请尝试用filter()删除1~100的素数。
# for i in range(int(np.sqrt(x)))[1:]:
import numpy as np

def  not_prim(x):
	for i in range(x)[2:int(np.sqrt(x))+1]:
		if x%i == 0:
			return True
	return False

print filter(not_prim,range(101)[1:])
