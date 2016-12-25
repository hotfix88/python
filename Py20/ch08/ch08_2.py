# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 21:58:22 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

print '-----------扑捉异常2：各种各样的异常---------'

try:
    x = input('Enter the first Number:')
    y = input('Enter the second Number:')
    print x/float(y)
except ZeroDivisionError:
    if x == 1:
        raise
    else:
        print 'The second is zero'
except (NameError,ValueError):  #一次捕捉多个异常
    if x == 1:
        raise
    else:
        print 'The second  is bugs'
except (NameError):
    if x == 1:
        raise
    else:
        print 'The second is error'
except ValueError:
    if x == 1:
        raise
    else:
        print 'The second is bad'        


#0      ZeroDivisionError: float division by zero
#hi     NameError: name 'hi' is not defined
#'hi'   ValueError: could not convert string to float: hi
#'hi'    unsupported operand type(s) for /: 'int' and 'str'  #需要把x/float(y) 修改为 x/y
#直接回车  SyntaxError: unexpected EOF while parsing
