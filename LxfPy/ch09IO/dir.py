#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-11 22:39:21
 Description: 操作文件和目录
"""
__author__ = 'FengYang'

print '---------------ch 9.2------------------'
import os
print os.name
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

# print os.uname() #注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。


# 环境变量
print os.environ
print '----- -----'
print os.getenv('PATH')
print '----- -----'
print os.path

 
print '----- 操作文件和目录 -----'
# 查看当前目录的绝对路径:
print os.path.abspath('.')
# '/Users/michael'  # D:\Git\python\LxfPy\ch09IO

# # 在某个目录下创建一个新目录，
# # 首先把新目录的完整路径表示出来:
# print  os.path.join('D:\Git\python\LxfPy\ch09IO', 'testdir')
 
# # 然后创建一个目录:
os.mkdir('D:/Git/python/LxfPy/ch09IO/testdir')

# # 删掉一个目录:
os.rmdir('D:/Git/python/LxfPy/ch09IO/testdir')

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print os.path.splitext('D:/Git/python/LxfPy/ch09IO/test.txt')

#改名
os.rename('test.txt', 'test.py')
os.rename('test.py', 'test.txt')

#删除
#os.remove('test.py')



# 但是复制文件的函数居然在os模块中不存在！
# 原因是复制文件并非由操作系统提供的系统调用。
# 理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。


print '----- ----------- -----'
# 比如我们要列出当前目录下的所有目录，只需要一行代码：
os.mkdir('D:/Git/python/LxfPy/ch09IO/testdir')
print [x for x in os.listdir('.') if os.path.isdir(x)]
os.rmdir('D:/Git/python/LxfPy/ch09IO/testdir')

print '----- ----------- -----'
# 要列出所有的.py文件，也只需一行代码：
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']


# 小结

# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。


