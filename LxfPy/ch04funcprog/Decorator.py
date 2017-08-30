#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-08-27 09:44:16
 Description: “装饰器”（Decorator）
 练习1 待解决！

"""

print '-----------1 函数的真名 -----------'
# 函数对象有一个__name__属性，可以拿到函数的名字：
def now():
	print '2017-08-27'

f = now
print f
print now
print '---------'
print f()
print now()

print '---------'
# 函数对象有一个__name__属性，可以拿到函数的名字：
print f.__name__
print now.__name__



print '-----------2 装饰器实现 -----------'
# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，
# 称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

#观察上面的log，因为它是一个decorator，
#所以接受一个函数作为参数，并返回一个函数。
#我们要借助Python的@语法，把decorator置于函数的定义处：
#把@log放到now()函数的定义处，相当于执行了语句：
#now = log(now)
@log
def now():
	print '2017-08-27'

print now()
print now.__name__
# f = now
# print f()

# 由于log()是一个decorator，返回一个函数，
# 所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
# 于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

print '-----------3 装饰器带入参 -----------'
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
# 比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            # wrapper.__name__ = func.__name__   #经过此函数后，名称被修改！ 此语句可以复原！
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute~~')
def now():
    print '2013-12-25'


print now()
print now.__name__

# 首先执行log('execute')，返回的是decorator函数，
# 再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

print '-----------4 装饰器（解决改名问题） -----------'
# 因为我们讲了函数也是对象，它有__name__等属性，
# 但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
# 
# 不需要编写wrapper.__name__ = func.__name__这样的代码，
# Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
	print '2017-08-27'

print now()
print now.__name__

print '-----------5 装饰器带入参（解决改名问题） -----------'
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute~~')
def now():
	print '2017-08-27'

print now()
print now.__name__

# import functools是导入functools模块。
# 模块的概念稍候讲解。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。



# 小结
# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
# OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。
# Python的decorator可以用函数实现，也可以用类实现。
# decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
# FY：暂时还不能理解的太深！过！
# 


print '-----------6 练习1 待解决！-----------'
# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
# 

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            # wrapper.__name__ = func.__name__   #经过此函数后，名称被修改！ 此语句可以复原！
            return func(*args, **kw)
        print 'end call '  
        return wrapper

    return decorator

# def log(func):
#     def wrapper(*args, **kw):
#         print 'end call %s():' % func.__name__
#         return func(*args, **kw)    

#     print  'begin call %s():' % func.__name__
#     return wrapper

@log('begin')
def now():
	print '2017-08-27'

print now()
# print now.__name__
# 

print '-----------7 练习2 待解决！-----------'
# 再思考一下能否写出一个@log的decorator，使它既支持：

# @log
# def f():
#     pass

# @log('execute')
# def f():
#     pass