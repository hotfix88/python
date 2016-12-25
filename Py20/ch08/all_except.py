# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 22:08:50 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

print '-----------扑捉异常3---------'

try:
    x = input('Enter the first Number:')
    y = input('Enter the second Number:')
    print x/y
    
except (NameError,ValueError) as e1:  #一次捕捉多个异常
    if x == 1:
        raise
    else:
        print e1
except :   #扑捉所有的异常！
    if x == 1:
        raise
    else:
        print 'something Wrong'
else:
    print 'Ah ....It went as planned!'