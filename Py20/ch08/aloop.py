# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 22:19:33 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

#感觉最有用的就是这个循环了！
#知道程序会发生某种异常，又不希望程序中止，这个时候就可以使用try except语句进行处理！


while True:
    try:
        x = input('Enter the first Number:')
        y = input('Enter the second Number:')
        print x/y
    
    
    except Exception ,e1:   #扑捉所有的异常！
        if x == 1:
            raise     #使用系统默认的会跳出！
        else:
            print 'Invalid is ',e1
            print 'Try Again!'
    else:
        print 'Ah ....It went as planned!'
        break
    finally:
        print 'ends'