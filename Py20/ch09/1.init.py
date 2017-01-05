# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 21:12:56 2017  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""


class NewStyle(object):
    name = 1
    
class OldStyle:
    name = 1
    
class FooBar:
    def __init__(self,value = 42):
        self.somevar = value
    
f = FooBar()    
print f.somevar

f = FooBar('This is a constructor argument')
print f.somevar

