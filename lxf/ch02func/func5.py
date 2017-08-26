#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso
 DateTime:    2017-08-26 12:43:33
 Description: 递归函数
"""

# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数


print '-----------递归函数-----------'
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print fact(1)
print fact(5)
print fact(100)


# 递归函数的优点是定义简单，逻辑清晰。
# 理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

print '-----------尾递归优化-----------'
# print fact(1000)  maximum recursion depth exceeded
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print fact(1)
print fact(5)
print fact(100)




# 小结
# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，
# 没有循环语句的编程语言只能通过尾递归实现循环。
# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。