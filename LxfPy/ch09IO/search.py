#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-11 22:58:24
 Description: Description
"""
__author__ = 'FengYang'

import os
print '---------------ch 9.2 练习题------------------'
print '-----  -----'
# 练习：编写一个search(s)的函数，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径：

l = 'f'

# 要列出所有的 文件，也只需一行代码：
print [x for x in os.listdir('.') if os.path.isfile(x) and l in os.path.splitext(x)[0] ]

#FY：这题没搞定呢！先搁置！
#