# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:44:57 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

def fibs(num):
    'this is a function  input some'
    result = [0,1]
    for i in range(num-2):
        result.append(result[-1]+result[-2])
    return result
        
#防止多次输入      
n = 2        
if n==2 :
    pass
else:       
    n = raw_input('How many Fibonacci numbers do you want?')
    n = int(n)
    
print fibs(n)
print callable(n)
print callable(fibs)
print fibs.__doc__
help(fibs)


#函数 局部作用域local scope,值的改变
print '---------------------------'
print n
def try_change_v(n):
    n = 99
    print n
    return
try_change_v(n)
print n


#函数 局部作用域local scope,值的改变
def try_change_l(m):
    m[0] = 99
    return
print '---------------------------'
mv = [32,56]
print mv
try_change_l(mv)
print mv
print '-----指针指向------'
mv = [32,56]
nv = mv
print nv == mv
print nv is mv
try_change_l(nv)
print mv
print nv
print '-----完全复制------'
mv = [32,56]
nv2 = mv[:]
print nv2 == mv #值 相等
print nv2 is mv #对象 等同
try_change_l(nv2)
print mv
print nv2

print '-------------指定参数--------------'
def multi_name(greetings,name):
    print greetings,name
    
multi_name('hello','world')
multi_name('world','hello')
multi_name(name='world',greetings='hello')



print '-------------作用域--------------'
x = 1
scope = vars()
print type(scope)
print scope['x']
scope['x'] += 1
print scope['x']

print '-------------全局变量--------------'
gl  = 100
def change_gl():
    global gl
    gl += 1
change_gl()
print gl

print '-------------闭包 closure --------------'
def multiplier(factor):
    def mb(number):
        return number*factor
    return mb
double = multiplier(2)
triple = multiplier(3)
print double(5)
print triple(5)
print multiplier(5)(5)

print '-------------递归 recursion ：函数调用自己--------------'
#要有结束条件
print '------阶乘----------'
def recursion(n = 4):  
    if n == 1:
        return 1
    else:
        return n*recursion(n-1)
print recursion()
print recursion(8)
print '------幂----------'
def pw(x=3,n=2):
    if n == 0:
        return 1
    else:
        return x*pw(x,n-1)
print pw()
print pw(4,3)
print '------二分法查找----------'
def bisearch(seq,number,lower,upper):
    if lower == upper:
        assert number == seq[upper]
        return upper
    else:
        middle = (lower + upper) //2
        if number > seq[middle]:
            return bisearch(seq,number,middle+1,upper)
        else:
            return bisearch(seq,number,lower,middle)

seq = [34,67,8,123,4,100,95]
seq.sort()
print seq
print bisearch(seq,34,0,len(seq))
print bisearch(seq,100,0,len(seq))
#找不到会assert，糟糕！
#from math import bisect
#bisect(seq,67)



print '-------------python以对象编程为主--------------'
print '-------------python的函数式编程也很牛B--------------' 
print '-------------map--------------'
print map(str,range(10))
print [str(i) for i in range(10)]

print '-------------filter:基于布尔值返回型函数的过滤--------------'
def func(x):
    if x > 100:
        return True
    else:
        return False
seq = [1,200,3,400]
print filter(func,seq)

#简单点
print [i for i in seq if i > 100]

print '-------------lanmbda 匿名函数--------------'
print map(lambda x:x*3,range(10)) 
#print filter(lambda x : if x>100:return True else :return False,seq)








