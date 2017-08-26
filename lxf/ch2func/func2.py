#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso
 DateTime:    2017-08-26 12:28:35
 Description: 可变参数
"""


print '------------可变参数1-----------'
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
mv = [1,2,3,4]
print mv
print calc(mv)
# print calc([for i in range(10)])

mv = [i for i in range(5)]  #列表推倒式，只支持list
print mv
print calc(mv)


mv = (1,2,3,4) #tuple
print mv
print calc(mv)

# print calc(1,2,3,4)   不可以直接调用，必须组装为list或者tuple，否则要用下面的方式

print '------------可变参数2-----------'
# 定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，
# 因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc()
print calc(1,2,3,4)

#如果已经有一个list或者tuple，要调用一个可变参数怎么办?用下面的方式，非常常见！
mv = [i for i in range(5)]  #
print calc(*mv)

#FY：没看出来有什么意义？