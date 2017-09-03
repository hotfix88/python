#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-02 22:55:50
 Description: metaclass 元类
"""

 
"""
 Author:      fyso@163.com
 DateTime:    2017-09-03 16:29:44
 Description: modify
"""

__author__ = 'FengYang'

print '---------------ch07.05.02------------------'


# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”

# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。
# 正常情况下，你不会碰到需要使用metaclass的情况，
# 所以，以下内容看不懂也没关系，因为基本上你不会用到。
#FY: so，那我就不看了。。
#