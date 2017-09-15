#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    2017-09-14 16:59:52
 Description: Description
"""
__author__ = 'FengYang'


print '---------------ch 9.4------------------'
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
# 但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
# JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。


# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
# JSON类型	Python类型
# {}	dict
# []	list
# "string"	'str'或u'unicode'
# 1234.56	int或float
# true/false	True/False
# null	None
print True
print None

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
import json
d = dict(name='Bob', age=20, score=88)
print json.dumps(d)


# dumps()方法返回一个str，内容就是标准的JSON。
# 类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
str = json.loads(json_str)
print str

# 有一点需要注意，就是反序列化得到的所有字符串对象默认都是unicode而不是str。
# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。
#FY:WTF  不懂！

print '-----------JSON进阶------------'
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
#print(json.dumps(s)) #错误的原因是Student对象不是一个可序列化为JSON的对象。 ===》下面是改正的代码
# dumps()方法还提供了一大堆的可选参数：https://docs.python.org/2/library/json.html#json.dumps
# 我们只需要为Student专门写一个转换函数，再把函数传进去即可：
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=student2dict))

#因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print(json.dumps(s, default=lambda obj: obj.__dict__))



print '-------- -----------'
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

# 小结
# Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。

