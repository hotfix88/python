#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso
 DateTime:    2017-08-26 14:19:42
 Description: 迭代
"""

# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

print '-----------迭代（Iteration）-----------'
# Python的for循环抽象程度要高于Java的for循环，
# 因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。


print '-----------dict迭代-----------'
# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，
# 但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：
d = {'a': 1, 'b': 2, 'c': 3}
print d

print '-----------key-----------'
for key in d:
	print key
# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

print '-----------value-----------'
# 默认情况下，dict迭代的是key。
# 如果要迭代value，可以用
for value in d.itervalues():
	print value

print '-----------key,value-----------'
# 如果要同时迭代key和value，可以用
for k, v in d.iteritems():
	print k,v

print '-----------字符串迭代-----------'
for ch in 'ABCDEFG':
	print ch


print '-----------判断是否可以迭代-----------'
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable
print isinstance('abc', Iterable) # str是否可迭代
print isinstance([1,2,3], Iterable) # list是否可迭代
print isinstance(123, Iterable) # 整数是否可迭代


print '-----------内置的enumerate函数-----------'
# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
	print i, value
print '----------------------'
# 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x, y


# 小结
# 任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
# 
# FY：至此，发现之前的学习了解太肤浅了，另外python普通教程里面说的还太浅显！
# 