#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-02 11:08:08
 Description: Description
"""
__author__ = 'FengYang'

print '---------------ch07.03------------------'
# 回忆一下Animal类层次的设计，假设我们要实现以下4种动物：
# Dog - 狗狗；
# Bat - 蝙蝠；
# Parrot - 鹦鹉；
# Ostrich - 鸵鸟。
# 如果按照哺乳动物和鸟类归类，如果要再增加“宠物类”和“非宠物类”， 如果按照“能跑”和“能飞”来归类
# 正确的做法是采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计：
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
	def suck(self):
		print ('sucking...')
	def suck2():
		print ('sucking...')


class Bird(Animal):
	def dick(self):
		print ('dicking...')


# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass


#现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Pet(object):
    def hug(self):
        print('hugging...')

class NonPet(object):
    def bite(self):
        print('biting...')

# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
class Dog(Mammal, Runnable,Pet):
    pass

# 对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：
class Bat(Mammal, Flyable,NonPet):
    pass

d = Dog()
print dir(d)
d.hug()
d.run()
d.suck()

b = Bat()
print dir(b)
b.suck()
b.fly()
b.bite()
