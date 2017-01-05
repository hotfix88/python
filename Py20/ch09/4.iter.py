# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 21:58:46 2017  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""



#迭代：一件事情做很多次！迭代器必须具有next方法
#一个实现了next方法的对象就是迭代器

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):        
        self.a,self.b = self.b,self.a + self.b
        return self.a
        
    def __iter__(self):
        return self

fibs = Fibs()
for f in fibs:
    if f > 1000:
        print f
        break
print fibs.next()
print fibs.next()
for i in range(10):
    print fibs.next()

print '-------------------'
it = iter([1,2,3])
print it.next()
print it.next()    





print '--------使用迭代器得到序列：有毛用？-----------'
class TestIterator:
    value = 0
    def next(self):
        self.value += 1
        if self.value > 10 : raise StopIteration
        return self.value
    def __iter__(self):
        return self
ti = TestIterator()
print ti
print list(ti)       
        
    