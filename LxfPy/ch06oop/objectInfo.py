#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-02 08:46:24
 Description: Description
"""
__author__ = 'FengYang'

print '---------------ch06.05------------------'

print '---------------1 type------------------'
# 基本类型都可以用type()判断：
print type(list)
print type([1,2,3]) 
print type((1,2,3) )
print type(123) 
print type('123')
print type(None)

# 如果一个变量指向函数或者类，也可以用type()判断：
print type(abs)

class Student(object):  
    pass
bart = Student()
print type(bart)

print '---------------2 isinstance()------------------'
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
class Animal(object):
	pass
class Dog(Animal):
	pass
class Huskey(Dog):
	pass
ani = Animal()
dog = Dog()
hus = Huskey()

print isinstance(hus, Huskey)
print isinstance(hus, Dog)
print isinstance(hus, Animal)
print isinstance(hus, object)

print '---------------3 dir()------------------'
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，
# 它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print dir(hus)
print dir('ABC')

print '-----------------'
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，
# 所以，下面的代码是等价的：
print len('ABC')
print 'ABC'.__len__()

print '-----------------'
# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyObject(object):
    def __len__(self):
        return 100
obj = MyObject()
print len(obj)


print '-----------------'
# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

print  hasattr(obj, 'x') 
print  obj.x
print  hasattr(obj, 'y')
print setattr(obj, 'y', 19) #可以增加一个原来不存在的变量。
print  hasattr(obj, 'y')
print obj.y
print getattr(obj, 'y')#如果试图获取不存在的属性，会抛出AttributeError的错误：


# 可以传入一个default参数，如果属性不存在，就返回默认值：
print getattr(obj, 'z', 404)



print '-----------------'
# 小结
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
# 要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：

class A(object):
    x = 3
    y = 6

a = A()
print a.x + a.y
print getattr(a,'x') + getattr(a,'y')


def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None