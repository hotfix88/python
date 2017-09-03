#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-03 17:49:47
 Description: Description
"""
__author__ = 'FengYang'

print '---------------ch08.06------------------'
print '------------1----------'
import logging
import pdb
logging.basicConfig(level=logging.DEBUG)

s = '0'
n = int(s)
logging.info('n = %d' %n)
pdb.set_trace()
print 10 / n

# 这就是logging的好处，它允许你指定记录信息的级别，
# 有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。
# 同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

print '------------2----------'
# 第4种方式是启动Python的调试器pdb，
# 让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：
# 
# python -m pdb err.py
# l可以看源代码
# 
# 输入命令n可以单步执行代码：
# 
# 任何时候都可以输入命令p 变量名来查看变量：
# 
# 输入命令q结束调试，退出程序：
# 
# c继续

print '------------3 pdb.set_trace()----------'
# 这种通过pdb在命令行调试的方法理论上是万能的，
# 但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。
# 还好，我们还有另一种调试方法。

# 这个方法也是用pdb，但是不需要单步执行，
# 我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
# 
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：

# 这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去。

print '------------4 IDE----------'
# IDE

# 如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有PyCharm：

# http://www.jetbrains.com/pycharm/

# 另外，Eclipse加上pydev插件也可以调试Python程序。

print '------------ ----------'
# 小结
# 写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，
# 你期待执行的语句其实根本没有执行，这时候，就需要调试了。
# 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。