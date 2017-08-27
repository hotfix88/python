#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-08-27 07:46:04
 Description: 闭包（Closure）
"""

# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

print '-----------1 求和函数 -----------'
# 通常情况下，求和的函数是这样定义的：
def calc_sum(*args): #一个可变参数函数
    ax = 0
    for n in args:
        ax = ax + n
    return ax

print calc_sum(1,2,3,4,5)
print calc_sum(1,2,3,4,5,100)
f = calc_sum(1,2,3,1000)
print f

print '-----------2 返回求和函数 -----------'
# 可以不返回求和的结果，而是返回求和的函数！
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

d = lazy_sum(1, 2,3,4,5)
f = lazy_sum(1, 3, 5, 7, 9)
print f,'\n',d,'\n',lazy_sum(1, 2,3,4,5)
print f(),d()
print lazy_sum(1, 2,3,4,6)()

print '-----------3 闭包（Closure） -----------'
# 我们在函数lazy_sum中又定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。

#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1,'\n',f2,'\n',f1==f2

print '-----------4 闭包调用时间 -----------'
# 注意到返回的函数在其定义内部引用了局部变量args，
# 所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
# 所以，闭包用起来简单，实现起来可不容易。
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：

# 每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()  #注意，这里必须返回3个


print f1
print f2
print f3

print f1()
print f2()
print f3()
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


 
print '-----------5 闭包循环的使用 -----------'
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，
# 用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs
f1, f2, f3 = count()  #注意，这里必须返回3个


print f1
print f2
print f3

print f1()
print f2()
print f3()
# 缺点是代码较长，可利用lambda函数缩短代码。
# 
# FY：还是有点难以理解，先暂时知道这个概念就是了，过！  这么搞意义何在？？
# FY：闭包的使用场景？