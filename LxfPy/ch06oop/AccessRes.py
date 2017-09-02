#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-02 07:51:36
 Description: Description
"""
__author__ = 'FengYang'

print '---------------ch06.03------------------'

print '---------------1   ------------------'
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问，所以，我们把Student类改一改
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        self.test = 1

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Tom',99)
bart.print_score()
# print bart.__name #不可调用
print bart.test
print bart.set_score(80) #会打印一个None出来！
print bart.get_score()
print bart.get_name()
# print bart.set_score(-80) #这里会抛出异常！


# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

# 比如_name，这样的实例变量外部是可以访问的，但是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

#  仍然可以通过_Student__name来访问__name变量
#  但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名
print bart._Student__name

