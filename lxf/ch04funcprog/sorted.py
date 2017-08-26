#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-08-26 20:27:45
 Description: sorted排序！
"""

print '-----------1 默认排序 -----------'
print sorted([36, 5, 12, 9, 21])
print sorted(['bob', 'about', 'Zoo', 'Credit'])

print '-----------2 倒序排序 -----------'
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print sorted([36, 5, 12, 9, 21],reversed_cmp)

print '-----------3 忽视大小写字母排序 -----------'
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ignore_case)

# 从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。