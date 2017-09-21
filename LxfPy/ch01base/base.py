#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 12:16:25 2017

@author: Administrator   fengyang  hotfix88@github.com
"""

"""
 Author:      fyso
 DateTime:    2017-08-25 15:39:34
 Description: modify！
"""

#sublime是一个神级的编辑工具，非常的好使啊！今天开始，重新学习python！参考廖雪峰的学习资料！


#数据类型和变量
a = 100
print a
if a > 100:
    print a
else:
    print -a

b = 0x10
print b

print 'I\'m ok.'
print 'I\'m \'ok\'.'

print '\\\t\\'
print r'\\\t\\'

#多行打印
print '''line1
line2
line3'''


a = 'ABC'
b = a
a = 'XYZ'
print a,b

print 20 / 3
print 20 / 3.0
print 20 % 3


#字符串和编码
t = 'z'
print t

print ord(t)
print chr(65)
print chr(0x41)

print u'中文'
print u'中文'.encode('utf-8')
print 'abc'.decode('utf-8')
#print u'中文'.encode('utf-8')
#print u'中文'.encode('utf-8')

#print u'以下在命令行中展示'
#print u'ABC'.encode('utf-8')
#print u'中文'.encode('utf-8')





"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    2017-09-14 16:22:15
 Description: Description
"""
print '------------我增加了一些东西-----------'

d = {'a':1,'b':2}
print d
print type(d)
print d['a']
d2 = d
print d is d2 #是一个对象
print d == d2 #内容相同
print type(d),type(d2)
#如果是dump和load之后，则内容相同，但是不是一个对象，见第9章 pickling.py

# chcp 65001



s = 'ABC\\-001' # Python的字符串
print s
s = r'ABC\-001'  #因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：
print s

