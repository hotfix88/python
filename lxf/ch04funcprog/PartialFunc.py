#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-08-27 22:20:26
 Description: 偏函数（Partial function）
"""

# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。
# 要注意，这里的偏函数和数学意义上的偏函数不一样。
# 在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。

print '-----------1 偏函数  -----------'
# 而偏函数也可以做到这一点。举例如下：
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
print '12345',type('12345')
print int('12345'),type(int('12345'))
print int('12345', base=8)
print int('12345', 16)


print '-------- ------'
def int2(x, base=2):
    return int(x, base)

print int2('1000000')
print int2('1010101')


 
print '-----------2 偏函数  -----------'
import functools
int22 = functools.partial(int, base=2)
print int22('1000000')
print int22('1010101')
# 所以，简单总结functools.partial的作用就是，
# 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
#FY 只是更加简单而已？



print '-----------3 偏函数  -----------'
# 最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：
# int2 = functools.partial(int, base=2)
# 实际上固定了int()函数的关键字参数base，也就是  int2('10010')
# 相当于：
# kw = { base: 2 }
# int('10010', **kw)

# 当传入：max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是： max2(5, 6, 7)
# 相当于：
# args = (10, 5, 6, 7)
# max(*args)
# 结果为10。


# 小结
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
#FY 只是更加简单而已？
