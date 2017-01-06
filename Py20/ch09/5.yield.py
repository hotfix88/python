# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 20:21:24 2017  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""


print '--------生成器简单例子-----------'
nested = [[1,2],[3,4],[5],[6,7,8]]
for i in nested :
    print i

#任何包含yield的语句都可以称之为生成器。
def flatten(nested):
    for sublist in nested:
        for element in sublist :
            yield element

for i in flatten(nested):
    print i
    
print list(flatten(nested))

print '--------生成器 和 列表推导式-----------'
k = [(i+2)**2 for i in range(2,6)]
print k

g = ((i+2)**2 for i in range(2,6)) #生成器的优点是不占用内存！
print g.next()
print g.next()


print '--------可以直接在函数中调用，不用加()-----------'
print sum(i**2 for i in range(4))



print '-------- 递归生成器 -----------'
#需要处理任意层的嵌套怎么办？
nested2=[[[1],2],3,4,[5,[6,7]],8]
def flatten_multi(nested):
    try:
        for sublist in nested:
            for element in flatten_multi(sublist) :
                yield element
    except TypeError:
        yield nested
for i in flatten_multi(nested2):
    print i        


print '--------支持字符串的 递归生成器 -----------'
#如果字符串只有一个字符，那么它的子字符串就是它自己，这样会引起无限死循环
#因此用字符串+''拼接，是检查字符串 最简单、最快速的方法
nested3=[[['foo'],'bar'],'barze','fif',['kk',['jj','bre']],'veri']
def flatten_char(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError

        for sublist in nested:
            for element in flatten_char(sublist) :
                yield element
    except TypeError:
        yield nested
for i in flatten_char(nested3):
    print i  

for i in flatten_char(nested2):
    print i  
    
#下面会导致死循环    
#for i in flatten_multi(nested3):  
#    print i  
    
print '--------使用普通函数重写：支持字符串的 递归生成器 -----------'
print '--------没有比较就没有伤害：生成器省内存啊！不用内建list，逐渐生成结果-----------'
def flatten_char_func(nested):
    result = []
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError

        for sublist in nested:
            for element in flatten_char_func(sublist) :
                result.append(element)
    except TypeError:
        result.append(nested)
    return result

print flatten_char_func(nested) 
print flatten_char_func(nested2) 
print flatten_char_func(nested3) 
    
print '--------通用生成器 -----------'
def simple_generator():
    yield 1


