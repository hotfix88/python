#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-02 10:34:11
 Description: property装饰器
"""
__author__ = 'FengYang'

print '---------------ch07.02------------------'
print '----------1---------'

class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s._score = 6
print s._score


print '---------2----------'
# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
# 对于追求完美的Python程序员来说，这是必须要做到的！
# 还记得装饰器（decorator）可以给函数动态加上功能吗？
# 对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# @property的实现比较复杂，我们先考察如何使用。
# 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，
# 负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
print s.score
# s.score = 9999  ValueError: score must between 0 ~ 100!


print '---------3----------'
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

s = Student()
s.birth = 2011
print s.birth
print s.age

# 小结

# @property广泛应用在类的定义中，可以让调用者写出简短的代码，
# 同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。