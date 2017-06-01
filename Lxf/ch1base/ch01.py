# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 12:16:25 2017

@author: Administrator   fengyang  hotfix88@github.com
"""


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
#print u'中文'.encode('utf-8')
#print u'中文'.encode('utf-8')

#print u'以下在命令行中展示'
'''
print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')
'''
