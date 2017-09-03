#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-03 20:08:56
 Description: 文档测试！
"""
__author__ = 'FengYang'

print '---------------ch08.09------------------'

# 无疑更明确地告诉函数的调用者该函数的期望输入和输出。

# 并且，Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。

# doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。
# 只有测试异常的时候，可以用...表示中间一大段烦人的输出。

# 让我们用doctest来测试上次编写的Dict类：


print '--------1-----------'
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()



print '--------2-----------'

def myabs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> myabs(1)
    1
    >>> myabs(-1)
    1
    >>> myabs(0)
    0
    '''
    return n if n >= 0 else (-n)

if __name__=='__main__':
    import doctest
    doctest.testmod()