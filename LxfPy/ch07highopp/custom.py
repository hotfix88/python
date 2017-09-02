#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-02 21:31:32
 Description: custom class 定制类
"""
__author__ = 'FengYang'

print '---------------ch07.04------------------'
# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

print '------------------1 、 __str__ 显示调试信息或者print的优化------------------'
class Student(object):
    def __init__(self, name):
        self.name = name

print Student('Michael')
s = Student('Tom')
print s

print '------------------'
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
    	return 'Student object (name: %s)' % self.name
print Student('Michael')
s = Student('Tom')
print s

# >>> print s
# Student object (name: Tom)
# >>> s
# <__main__.Student object at 0x0000000002AB52B0>
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，
# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
# 也就是说，__repr__()是为调试服务的。

print '------------------'
# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__
s = Student('Tom')
print s


print '------------------2 、 __iter__ 用fib数列举例！------------------'
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。

# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

for n in Fib():
    print n,
print ''

print '------------------3 、 __getitem__  下标和切片通例 ------------------'
# Fib实例虽然能作用于for循环，看起来和list有点像，
# 但是，把它当成list来使用还是不行，比如，取第5个元素：   Fib()[5]   
# 这样是不行的！
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

    #要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

for n in Fib():
	print n,
print ''

f = Fib()
print f
print f[0],type(f),dir(f)

print '------------支持slice切片------------'
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    print n,
print ''

f = Fib()
print f[0:5],type(f),type(f[:10])
print f[:10:2]#但是没有对step参数作处理

# 扩展：
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
# 最后，还有一个__delitem__()方法，用于删除某个元素。
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，
# 这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。


print '------------------4 、 __getattr__  属性和方法的动态化------------------'
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
class Student(object):
    def __init__(self):
        self.name = 'Michael'

s = Student()
print s.name
# print s.score  #AttributeError: 'Student' object has no attribute 'score'

print '--------------- --------'
# 要避免这个错误，除了可以加上一个score属性外，
# Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 999
        elif attr=='age':  #也可以返回函数！
            return lambda: 25
        elif attr == 'kk':
            raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr) #要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：

s = Student()
print s.name
print s.score
print s.test  #定义的__getattr__默认返回就是None
print s.age
print s.age()
#print s.kk #报异常！
# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
# 
print '--------------- --------'
#这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。！！
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。

# 举个例子：
# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
# 利用完全动态的__getattr__，我们可以写出一个链式调用：

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list

# 这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
# 
# 
# 还有些REST API会把参数放到URL中，比如GitHub的API：
# GET /users/:user/repos
# 调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：
# print Chain().users('michael').repos
# 就可以非常方便地调用API了。有兴趣的童鞋可以试试写出来。



print '------------------5 、 __call__  可调用的方法！------------------'

# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
# 能不能直接在实例本身上调用呢？类似instance()？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
        return ''

s = Student('Michael')
print s()

print '--------------- --------'
# 怎么判断一个变量是对象还是函数呢？
# 能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call()__的类实例：

s = Student('Michael') #可以调用的实例
c = Chain()  #不可以调用的实例
print callable(s)
print callable(c)
print callable(abs)
print callable([1, 2, 3])
print callable(None)
print callable('string')  
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。



# 小结
# Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。
# 本节介绍的是最常用的几个定制方法，还有很多可定制的方法，请参考Python的官方文档。