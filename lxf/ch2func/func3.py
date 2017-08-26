#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso
 DateTime:    2017-08-26 12:13:42
 Description: 关键字参数  
"""

print '-----------关键字参数-----------'
#keyword parameter;
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer') 

#关键字参数有什么用？它可以扩展函数的功能。
#比如，在person函数里，我们保证能接收到name和age这两个参数，
#但是，如果调用者愿意提供更多的参数，我们也能收到。
#试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，
#利用关键字参数来定义这个函数就能满足注册的需求。
#

print '-----------关键字参数：对dict的调用-----------'
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
person('Jack', 24, **kw)

#FY：没看出来有什么意义？过！