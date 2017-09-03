#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-03 17:02:46
 Description: 调用堆栈   记录错误
"""
__author__ = 'FengYang'
print '---------------ch08.02------------------'
import logging
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
# 

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()

print 'END'

# 但程序打印完错误信息后会继续执行，并正常退出：
'''
D:\Git\python\LxfPy\ch08EDT>python err.py
---------------ch08.02------------------
ERROR:root:integer division or modulo by zero
Traceback (most recent call last):
  File "err.py", line 20, in main
    bar('0')
  File "err.py", line 16, in bar
    return foo(s) * 2
  File "err.py", line 13, in foo
    return 10 / int(s)
ZeroDivisionError: integer division or modulo by zero
END
'''

