#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-11 21:36:06
 Description: Description
"""
__author__ = 'FengYang'

print '---------------ch 9.1------------------'

# 由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题。
# CPU输出100M的数据只需要0.01秒，可是磁盘要接收这100M数据可能需要10秒，

# 第一种是CPU等着， 这种模式称为同步IO；另一种方法是CPU不等待， 这种模式称为异步IO。
# 使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂
# 如果是服务员跑过来找到你，这是回调模式，如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。

# 操作IO的能力都是由操作系统提供的，每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用，Python也不例外。
 
print '---------------读文件------------------'
# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：

f = open('D:/Git/python/LxfPy/ch09IO/test.txt', 'r') #标示符'r'表示读，   #/Users/michael/test.txt

# 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
str = f.read()
print str

# 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，
# 因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
f.close()

print '---------------读文件2：异常处理------------------'
# 由于文件读写时都有可能产生IOError，  为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
    f = open('D:/Git/python/LxfPy/ch09IO/test.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()

print '---------------读文件3：with------------------'
# Python引入了with语句来自动帮我们调用close()方法：
with open('D:/Git/python/LxfPy/ch09IO/test.txt', 'r') as f:
    print f.read()


print '---------------读文件4：read(size)------------------'
# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了
# 每次最多读取size个字节的内容。
with open('D:/Git/python/LxfPy/ch09IO/test.txt', 'r') as f:
    print f.read(10)
    print f.read(10)
    print f.read(10)
    print f.read(10)
    print f.read(10)

print '---------------读文件5：readlines()------------------'
# 调用readlines()一次读取所有内容并按行返回list。
with open('D:/Git/python/LxfPy/ch09IO/test.txt', 'r') as f:
	print f.readlines()
	print f.readlines()

print '----- -------'
	# 如果文件很小，read()一次性读取最方便；
	# 如果不能确定文件大小，反复调用read(size)比较保险；
	# 如果是配置文件，调用readlines()最方便：
with open('D:/Git/python/LxfPy/ch09IO/test.txt', 'r') as f:
	for line in f.readlines():
	    print(line.strip()) # 把末尾的'\n'删掉

print '---------------读文件6：readline()------------------'
with open('D:/Git/python/LxfPy/ch09IO/test.txt', 'r') as f:
	print f.readline()
	print f.readline()
	print f.readline()


print '---------------读文件 二进制文件------------------'
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。
# [Decode error - output not utf-8]  不支持print
with open('D:/Git/python/LxfPy/ch09IO/baidu_logo.png', 'rb') as f:
    print f.read()

print '---------------读文件 gbk文件------------------'
with open('D:/Git/python/LxfPy/ch09IO/gbk.txt', 'rb') as f:
    # print f.read()
    pass
# 要在文件开头写入0xfffe，这是Unicode file的identifier，
# windows下的记事本和写字板读到这个头之后，就能正确识别这是一个Unicode文件了。


import codecs
with codecs.open('D:/Git/python/LxfPy/ch09IO/gbk.txt', 'r', 'gbk') as f:
    # print f.read() # u'\u6d4b\u8bd5'
    pass


print '---------------写文件------------------'
with open('D:/Git/python/LxfPy/ch09IO/write.txt', 'w') as f:
    f.write('Hello, world!')
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。


#FY:遗留下 gbk格式文件的研究！

# 小结

# 在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。