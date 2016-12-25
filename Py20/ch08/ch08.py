# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 21:42:37 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

 

#每个异常都是 一些类，是程序可以捕捉错误并且处理，不至于整个程序失效
#Exception 是所有异常类的基类


    

print '--------------raise---------------'
class MuffledCalculator:
    muffled = False
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print 'Division by zero is illegal'
            else:
                raise

calculator =    MuffledCalculator()
calculator.calc('10/2')  
calculator.muffled = True
calculator.calc('10/0') 


        