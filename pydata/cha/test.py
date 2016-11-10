# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:22:49 2015

@author: Administrator
"""

#关于新建对象
a = [1,2,3]
b = a
c = list(a)
a.append(4)
print(a)
print(b)
print(c)
b = 3
print(b)

#None
x = 1
x = None
x is None
y = 2
del y
#y is None #name 'y' is not defined



#isinstance
def append_ele(data,ele):
    data.append(ele)

append_ele(a,5)
print(a)

isinstance(a,(int,list))


# 常用的：列表、元组、ndarray 转换为list可迭代
def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

x = 1
if not isinstance(x,list) and isiterable(x):
    x = list(x)
    
    
#部分引入
from pandas import DataFrame as DF
df = DF(a)
a is b
a is df
b = df
b is df

#计算顺序
a = b = c =5
d = a+b*c

#python3自动转换long整数
a = 17239871
val = a**6
print(val)

#浮点64位
a = 1.22324234/98
print(a)

#虚数
a = 1 + 2j
a = a*(1-2j)
print(a)

#字符串，某一个元素如a[1]不可修改'str' object does not support item assignment
a ='你好'
b = "你也好"
c = '''
我们都很好
'''
d = a + b + ' -- ' + c

# __nonzero__  魔术方法
bool(1)
bool('')
bool(' ') 

#None 不是一个关键字，它是NoneType的一个实例（也是唯一的实例）
a = None
b = None
a is b

#time
from datetime import datetime,date,time
dt = datetime(2015,9,25,10,16,30)
dt.date()
dt.time()


#pass放点空代码行

pass




#抛异常
def attemp_float(f):
    try:
        return 9/f
    except:
        return f
attemp_float(9)
attemp_float(0)

#抛异常2
path = '2.txt'

f = open(path)

try:
#    write_to_file('kkk')
    f.readlines()
except:
    print('Failed!')
else:
    print('Succeed!')
finally:
    f.close()

#python3中，range始终返回迭代器
type(range(3))#range
for i in range(3):
    print(i)

x = range(10)
if isiterable(x):
    x = list(x)


#三元表达式
x = 1
y = ('hello' if x >= 2 else 'hi')

#tuple 元组
x = 1,2,3
x*3

x = [1,2,3]
y = x,3,2
y[0].append(2)
y[0].count(2)
y.count(2)


#list内置函数
x = [5,3,2,1,7,8,9,0]
y = x
z = list(x)#新建对象
x.sort()
x is y
y is z


#list切片，不赘述

#内置序列函数
#enumerate
x = ['foo','bar','baz']
for i,value in enumerate(x):
    print(i,value)
mapping = dict((v,i) for i,v in enumerate(x))

x = [3,4,12,5,78,0,3,3,2,1]
sorted(x)
set(x)
sorted(set(x))
list(reversed(sorted(set(x))))

sorted('a fox flow')

#字典
mapping = dict(zip(range(5),reversed(range(5))))

#字典键值的有效性
hash(1)
hash('very')

#集合：可以看做无键的字典
x = [1,2,2,3]
x = set(x)
x ={1,3,3,4}

#list dict set 的列表推倒式 ，，最受欢迎的python特性！
s = ['a','bat','ali','baidu','tecent','jd','sn','bat']

[x.upper() for x in s if len(x)>2]#list
{x:hash(x) for x in s if len(x)>2 }#dict
{x  for x in s if len(x)>2 }#set
{key:value for value,key in enumerate(s) if len(key)>2 }#dict


#函数，记住关键参数和位置参数！关键参数在后面，记住名字就行了、
#不赘述了。关键参数python里面用的很多！


#命名空间，作用域、局部函数
a = []
b = [1,2,3]
def func(b):
    a = []
    for i in range(5):
        a.append(i)
    print('in:',a)
    b = a
    #当出去的时候，内部的a已经被销毁
func(a)
c = func(b) #c is None!


def func(b):
    a = []
    for i in range(5):
        a.append(i)
    print('in:',a)
    b = a
    return b #这样才在a销毁前，返回值给b
    #还有个方法是global关键字，但是不建议这么使用。
b = func(b)



#返回多个值
#def f():
#    a = 2
#    b = 3
#    c = 4
#    return('a':a,'b':b,'c':c)
#f()



#函数亦对象
#re 正则表达式模块???



#匿名函数 lambda??? 
#通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，
#也就是指匿名函数。
a = 3
x = (lambda x:x*2)#<function __main__.<lambda>>
x2 =  (lambda x:x**2)
z=x2(a)
y=x(a)
#z=list(map(x,a))
x = (lambda x:x*2+100)(a)

l = ['foo', 'bar', 'far']
list(map(lambda x: x.upper(), l))
(lambda x: x.append('x'))(l)


#闭包
#返回函数的函数。。


#curring
#例如计算60日的移动平均

#生成器
some_dict = {'a':1,'b':2,'c':3}
for key in some_dict:
    print(key)
    

#基本文件操作：
path = '3.txt'
f = open(path,'w')
f.write('hello')
f.close()

f = open(path)
for l in f:
    print(l)
f.close()