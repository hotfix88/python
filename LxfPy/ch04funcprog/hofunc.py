#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-08-26 18:36:06
 Description: 高阶函数  Higher-order function
"""



print '-----------1 变量可以指向函数-----------'
print abs(-10)
print abs

f = abs
print f(-10)
print f

print '-----------2 函数名也是变量-----------'
abs = 10
# print abs(10)
print abs
print '------------'
print f(10)
print f
abs = f
print abs(10)
print abs

# 注：由于abs函数实际上是定义在__builtin__模块中的，
# 所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10。


print '-----------3 传入函数-----------'
# 既然变量可以指向函数，函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)
def s(x):
	return x*x

print add(-5, 6, abs)
print add(-5, 6, s)

