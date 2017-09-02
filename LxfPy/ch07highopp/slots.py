#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-02 09:28:31
 Description: slot 限定增加属性
"""
__author__ = 'FengYang'


# 数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。
# 在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。
# 我们会讨论多重继承、定制类、元类等概念

print '---------------ch07.01------------------'
print '-------------------'
# 正常情况下，当我们定义了一个class，创建了一个class的实例后，
# 我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student(object):
	pass

# 然后，尝试给实例绑定一个属性：
s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print s.name 

# 还可以尝试给实例绑定一个方法：
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s, Student) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print s.age # 测试结果

print '-------------------'

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student() # 创建新的实例
#s2.set_age(25) # 尝试调用方法

# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score
Student.set_score = MethodType(set_score, None, Student)
s.set_score(100)
s2.set_score(99)
print s.score
print s2.score


print '-------------------'
# 但是，如果我们想要限制class的属性怎么办？比如，只允许对Student实例添加name和age属性。
class Student(object):
	__slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称


s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# s.score = 99 # 绑定属性'score'  由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。


# 使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：

class GraduateStudent(Student):
	pass
g = GraduateStudent()
g.score = 9999

# 除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。
# 