#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso
 DateTime:    2017-08-25 22:45:40
 Description: Description
"""

print '-----------基本函数-----------'
PI = 3.1415926
def area_of_circle(x):
	return PI*x*x

print area_of_circle(100)


print '-----------默认参数------------'
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(3)
print power(3,3)

print '------------默认参数-----------'
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

enroll('Sarah', 'F',5,'NanJing')

print '------------默认参数-----------'
def add_end(L=[]):
    L.append('END')
    return L

print add_end([1, 2, 3])
print add_end()
print add_end()
print add_end()
#原因解释如下：
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print add_end2([1, 2, 3])
print add_end2()
print add_end2()
print add_end2()
# 现在，无论调用多少次，都不会有问题：
# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，
# 如果可以设计一个不变对象，那就尽量设计成不变对象。

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

#