#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso
 DateTime:    2017-08-26 14:37:03
 Description: 列表生成式or列表推导式
"""


# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

print '-----------列表生成式即List Comprehensions-----------'
L = range(1, 11)
print L

print [x * x for x in range(1, 11)]

print [x * x for x in range(1, 11) if x % 2 == 0] #仅偶数的平方

# 还可以使用两层循环，可以生成全排列：
print [m + n for m in 'ABC' for n in 'XYZ']


# 运用列表生成式，可以写出非常简洁的代码。
# 例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os # 导入os模块，模块的概念后面讲到
print [d for d in os.listdir('.')] # os.listdir可以列出文件和目录


# for循环其实可以同时使用两个甚至多个变量，比如dict的iteritems()可以同时迭代key和value：
# 因此，列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k, v in d.iteritems()]


# 最后把一个list中所有的字符串变成小写：

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]


# 使用内建的isinstance函数可以判断一个变量类型：
x = 'abc'
y = 123
print isinstance(x, str)
print isinstance(y, str)
print isinstance(x, int)
print isinstance(y, int)

# 小结
# 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。

