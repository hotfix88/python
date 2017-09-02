#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-02 21:08:39
 Description: MixIn
"""
__author__ = 'FengYang'

print '---------------ch07.03.02------------------'
# 让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为Mixin。
# 回忆一下Animal类层次的设计，假设我们要实现以下4种动物：
# Dog - 狗狗；
# Bat - 蝙蝠；
# Parrot - 鹦鹉；
# Ostrich - 鸵鸟。
# 大类:

class Animal(object):
    pass

class Mammal(Animal):
	def suck(self):
		print ('sucking...')
	def suck2(self):
		print ('sucking...')

class RunnableMixin(object):
    def run(self):
        print('Running...')

class FlyableMixin(object):
    def fly(self):
        print('Flying...')

class CarnivorousMixin():#肉食动物
	def eat(self):
		print('Eatting Meat...')

# Mixin的目的就是给一个类增加多个功能，这样，在设计类的时候，
# 我们优先考虑通过多重继承来组合多个Mixin的功能，而不是设计多层次的复杂的继承关系。

class Dog(Mammal, RunnableMixin, FlyableMixin,CarnivorousMixin):
    pass

d = Dog()
print dir(d)
d.eat()
d.fly()
d.run()
d.suck()
d.suck2()


print '--------------- ------------------'
# Python自带的很多库也使用了Mixin。
# 举个例子，Python自带了TCPServer和UDPServer这两类网络服务，
# 而要同时服务多个用户就必须使用多进程或多线程模型，
# 这两种模型由ForkingMixin和ThreadingMixin提供。通过组合，我们就可以创造出合适的服务来。

from SocketServer import TCPServer, UDPServer

# 如果你打算搞一个更先进的协程模型，可以编写一个 CoroutineMixin：
class CoroutineMixin(object):
	pass
#进程
class ForkingMixin(object):
	pass
#线程
class ThreadingMixin(object):
	pass


# 比如，编写一个多进程模式的TCP服务，定义如下：
class MyTCPServer(TCPServer, ForkingMixin):
    pass

# 编写一个多线程模式的UDP服务，定义如下：
class MyUDPServer(UDPServer, ThreadingMixin):
    pass

# 编写一个协程模式的UDP服务，定义如下：
class MyTCPServer(TCPServer, CoroutineMixin):
    pass

# 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。

# 小结
# 由于Python允许使用多重继承，因此，Mixin就是一种常见的设计。
# 只允许单一继承的语言（如Java）不能使用Mixin的设计。
# FY：python允许多重继承，动态的增加属性和方法！