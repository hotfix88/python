#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso
 DateTime:    2017-08-26 13:59:39
 Description: Description
"""

print '-----------切片（Slice）-----------'
# Python提供了切片（Slice）操作符，能大大简化这种操作。

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L
print L[0:3]
print L[-1]

L = range(100)
print L[:10]
print L[-10:]
print L[::5]#所有数，每5个取一个：
print L[:]#甚至什么都不写，只写[:]就可以原样复制一个list


print '-----------tuple切片（Slice）-----------'
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
L = ('Michael', 'Sarah', 'Tracy', 'Bob', 'Jack')
print L[1:3]
L = tuple(range(10))
print L[:]


print '-----------字符串切片（Slice）-----------'
# Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。
print 'ABCDE'[:]
print 'ABCDE'[1:4]
print 'ABCDE'[::2]





# 小结
# 有了切片操作，很多地方循环就不再需要了。Python的切片非常灵活，一行代码就可以实现很多行循环才能完成的操作。