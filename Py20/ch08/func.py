# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 22:35:27 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

#函数的异常处理

def faulty():
    raise Exception('Something is wrong')

def ignore_except():
    faulty()

def handle_except():
    try:
        faulty()
    except:
        print 'exception handled'


ignore_except()  #最终导致栈跟踪
handle_except()  #最终被 try except 个性化的处理了！
