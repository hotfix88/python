#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-03 17:18:13
 Description: Description
"""
__author__ = 'FengYang'

print '---------------ch08.04------------------'
print '---------1-----------'
def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:   #ZeroDivisionError: integer division or modulo by zero
        print 'Error!!!! fuck U '
        raise    ValueError('input error!')    
        #只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。 
        ## raise语句如果不带参数，就会把当前错误原样抛出。
        # 此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：


def main():
    bar('0')

main()


# 在bar()函数中，我们明明已经捕获了错误，但是，打印一个Error!后，
# 又把错误通过raise语句抛出去了，这不有病么？

# 其实这种错误处理方式不但没病，而且相当常见。
# 捕获错误目的只是记录一下，便于后续追踪。
# 但是，由于当前函数不知道应该怎么处理该错误，
# 所以，最恰当的方式是继续往上抛，让顶层调用者去处理。



# 小结
# Python内置的try...except...finally用来处理错误十分方便。
# 出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。
# 程序也可以主动抛出错误，让调用者来处理相应的错误。
# 但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。