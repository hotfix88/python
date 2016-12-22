# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 21:21:50 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

'''
Function:
Author  : FengYang
Remark  :
@create : 
@modify :
'''

# 《python 基础教程》 第一章：快速改造：基础知识
#安装，可以跳过了
#IDE使用winpython！
# 使用!python  ch01.py 可以在shell外执行程序！

#一些基本操作
print 3/3
print 3//5
print 3/5.0
print 3*2.0
print 3**3 #幂次方
print 5/4
print pow(3,2)
print pow(2,0.5)
print sqrt(2)
print abs(-4.1)
print round(1/2.0)
print round(1.499)
print round(1.499,3)
print ceil(4.5)
print floor(4.5)
print 3//4  #整除
print 3%4  #取余数

#复数
import cmath
print cmath.sqrt(-1)
print (1+3j)*(9+4j)
print (1+3j)**(9+4j)
print (1+3j) + (9+4j)
print (1+3j) - (9+4j)
print (1+3j)/(9+4j)
print (1+3j)//(9+4j)

print 1000000000000000000000000000000000000000000000000000000000000

x=4
print x**3

#输入函数
#x = input('x:')
#y = input ("y:")
#print 'x*y =', x*y
#除非有特别的需要，否则最好用raw_input

#字符串
x = 'hi'
y = 'judy'
print x + y



x = 3
print str(x)
print repr(x)