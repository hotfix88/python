# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 21:25:04 2017  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

class A:
    def hello(self):
        print "hello,I'm A"

class B(A):
    pass

class B2(A):
    def hello(self):
        print "hello,I'm B" #重写方法


a = A()
b = B()
b2 = B2()
a.hello()
b.hello()
b2.hello()


#python的析构方法__del__要尽量避免使用，由于它要在对象被垃圾回收之前调用但是
#垃圾回收的时间不可知，所以避免使用吧。


