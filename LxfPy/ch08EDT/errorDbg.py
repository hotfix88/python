#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-03 16:38:10
 Description: Description
"""
__author__ = 'FengYang'

print '---------------ch08.01------------------'

print '---------1-----------'
# 用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，
# 造成调用者必须用大量的代码来判断是否出错：
# 一旦出错，还要一级一级上报，直到某个函数可以处理该错误（比如，给用户输出一个错误信息）。

def foo():
    r = some_function()
    if r==(-1):
        return (-1)
    # do something
    return r

def bar():
    r = foo()
    if r==(-1):
        print 'Error!'
    else:
    	print 'sucess'
        pass

def some_function():
	return -1

bar()

print '----------2----------'
# 所以高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。
try:
    print 'try...'
    r = 10 / 0  #修改
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'

print '---------3-----------'
# 可以有多个except来捕获不同类型的错误：
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
finally:
    print 'finally...'
print 'END'


print '----------4----------'
# 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'


print '---------5-----------'
def foo():
	return 10/0

# 第二个except永远也捕获不到ValueError，因为ValueError是StandardError的子类，
# 如果有，也被第一个except给捕获了。
try:
    foo()
except StandardError, e:
    print 'StandardError'
except ValueError, e:
    print 'ValueError'

print '---------6-----------'
def foo():
	return 10/0
#无论顺序如何了。
try:
    foo()
except ValueError, e:
    print 'ValueError'
except StandardError, e:
    print 'StandardError'



print '----------7----------'
# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
# 比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，
# 这时，只要main()捕获到了，就可以处理：

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        print 'Error!'
    finally:
        print 'finally...'

main()
# 也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。
# 这样一来，就大大减少了写try...except...finally的麻烦。

print '----------8----------'
#FY 是的，无论在哪里调用，都是一样的效果！
def main():
    try:
        s = 1/0
    except StandardError, e:
        print 'Error!'
    finally:
        print 'finally...'

main()