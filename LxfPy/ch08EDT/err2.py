#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-03 17:12:03
 Description: Description
"""
__author__ = 'FengYang'

print '---------------ch08.03------------------'

class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

#foo('a') # ValueError: invalid literal for int() with base 10: 'a'
#foo('0')  # __main__.FooError: invalid value: 0
foo('1') 

# 只有在必要的时候才定义我们自己的错误类型。
# 如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），
# 尽量使用Python内置的错误类型。