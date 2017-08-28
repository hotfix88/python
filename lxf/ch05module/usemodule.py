#!/usr/bin/env python
# -*- coding: utf-8 -*-
' a test module '
"""
 Author:      fyso@163.com
 DateTime:    2017-08-28 13:59:12
 Description: 模块
"""



' a test module '
print '-----------1/模块导入-----------'
__author__ = 'FengYang'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello, world! '
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

# >>> import usemodule
# -----------1/妯″潡瀵煎叆-----------
# >>> usermodule.test()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'usermodule' is not defined
# >>> usemodule.test()
# Hello, world!
# >>> usemodule.__name__
# 'usemodule'
# >>> usemodule.__author__
# 'FengYang'
# >>> usemodule.__doc__
# '\n Author:      fyso@163.com\n DateTime:    2017-08-28 13:59:12\n Description: \xe6\xa8\xa1\xe5\x9d\x97\n'