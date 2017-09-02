#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-02 22:55:50
 Description: metaclass 元类 : hello !
"""
__author__ = 'FengYang'

print '---------------ch07.05.01------------------'


# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
# 比方说我们要定义一个Hello的class，就写一个hello.py模块：
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

# >>> from hello import Hello
# ---------------ch07.05.01------------------
# >>> h = Hello()
# >>> h.Hello()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Hello' object has no attribute 'Hello'
# >>> h.hello()
# Hello, world.
# >>> print(type(Hello))
# <type 'type'>
# >>> print(type(h))
# <class 'hello.Hello'>

print '------------- -----------'
# type()函数可以查看一个类型或变量的类型，
# Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
# type()函数既可以返回一个对象的类型，又可以创建出新的类型
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
print h.hello()
print(type(Hello))
print(type(h))


# 要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。


# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
# 仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，
# 也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，
# 要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，
# 或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

#FY；奇技淫巧？ 深刻理解吧！