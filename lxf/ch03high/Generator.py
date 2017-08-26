#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso
 DateTime:    2017-08-26 14:50:08
 Description: 生成器（Generator）
"""

#一个全新的 概念


print '-----------生成器（Generator）-----------'
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
# 如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。
print '-----------生成器方法1：直接定义-----------'
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (i*i for i in range(10))
print g  #注意，这个是一个generetor
print g.next()
print g.next()
for n in g:  #通常用for循环迭代，而非next()调用
	print n
#print g.next() #当全部弹出后，再次调用就会失败退出   StopIteration


print '-----------生成器方法2：yeild-----------'
print '-----------解释-----------'
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# 定义一个generator，依次返回数字1，3，5
def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5
o = odd()
print o.next()
print o.next()
print o.next() 
#print o.next() #当全部弹出后，再次调用就会失败退出   StopIteration

print '-----------应用场景-----------'
# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

print '------函数-----'
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1
print fib(6)
print '------生成器----------'
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
print '------生成器调用1----------'
print fib(6)
fib(6).next()
fib(6).next()
fib(6).next()
for i in fib(6):
	print i

print '--------生成器调用2-------'
g = fib(6)
print g.next()
print g.next()
for n in g:
	print n


# 小结
# generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，
# 也可以通过函数实现复杂逻辑的generator。
# 
# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，
# 并在适当的条件结束for循环。对于函数改成的generator来说，
# 遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。  