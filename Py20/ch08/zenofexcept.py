# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 22:46:56 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

#尽可能养成使用try except的好习惯！

#leap before you look

def describe(person):
    print 'Name:',person['name']
    print 'Age:',person['age']
    try:
        print 'Occupation:' + person['oc']
    except Exception as e1:
        print 'Invalid is:' ,e1
        pass
    else:
        print 'have occupation'
    finally:
        print '----------------'

tom ={'name':'Tom','age':22}
jack={'name':'Jack','age':22,'oc':'camper'}

describe(tom)
describe(jack)
