#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-03 17:35:26
 Description: Description
"""
__author__ = 'FengYang'
print '---------------ch08.05------------------'
# 程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需要修正。
# 因此，需要一整套调试程序的手段来修复bug。

# 第一种方法简单直接粗暴有效，就是用print把可能有问题的变量打印出来看看：
# 用print最大的坏处是将来还得删掉它，想想程序里到处都是print，运行结果也会包含很多垃圾信息。

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

main()
# assert的意思是，表达式n != 0应该是True，否则，后面的代码就会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError：
# AssertionError: n is zero!
# 否则就是抛异常
# ZeroDivisionError: integer division or modulo by zero

# 不过，启动Python解释器时可以用-O参数来关闭assert：
# $ python -O err.py
