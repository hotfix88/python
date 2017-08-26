#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-08-26 18:51:35
 Description: 高阶函数之  map reduce
"""

# 如果你读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，
# 你就能大概明白map/reduce的概念。

print '-----------1/map-----------'
# 我们先看map。map()函数接收两个参数，一个是函数，一个是序列，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
def f(x):
    return x * x

print map
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# 所以，map()作为高阶函数，事实上它把运算规则抽象了，
# 因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，
# 比如，把这个list所有数字转为字符串：
print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print '-----------2/reduce-----------'
# reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是
def add(x, y):
    return x + y
print reduce
print reduce(add, [1, 3, 5, 7, 9])   #求和运算可以直接用Python内建函数sum()，没必要动用reduce。



# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场
def fn(x, y):
    return x * 10 + y
print reduce(fn, [1, 3, 5, 7, 9]) 

print '-----------3 map/reduce-----------'
# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print reduce(fn,map(char2num,'13579'))

#整理成一个str2int的函数就是：
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
print str2int('13579')

#还可以用lambda函数进一步简化成：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))
print  str2int('13579')


print '-----------4 练习题-----------'
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。

def f(s):
	return s.capitalize()
L = ['adam', 'LISA', 'barT']
print map(f,L) #map是一个函数一个序列

print '-----------5 练习题-----------'
# Python提供的sum()函数可以接受一个list并求和，
L = [1,2,3,4,5]
print sum(L)
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积。
def prod(x,y):  #注意reduce函数是两个入参
	return x*y
print reduce(prod,L)

