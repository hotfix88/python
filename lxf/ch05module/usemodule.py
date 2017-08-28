#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-08-28 13:59:12
 Description: Description
"""

' a test module '

__author__ = 'FengYang'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'



if __name__=='__main__':
    test()

''' 测试结果
D:\git\python\lxf\ch05module>python usemodule.py
Hello, world!

D:\git\python\lxf\ch05module>python usemodule.py nihao
Hello, nihao!

D:\git\python\lxf\ch05module>python usemodule.py nihao 22
Too many arguments!
'''