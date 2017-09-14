#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    2017-09-14 16:18:49
 Description: Description
"""
__author__ = 'FengYang'


print '---------------ch 9.3------------------'

d = dict(name='Bob', age=20, score=88)
print d
print type(d)
print d['name']
d['name'] = 'Bill'
print d['name']
# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

# Python提供两个模块来实现序列化：cPickle和pickle。cPickle是C语言写的，速度快
try:
    import cPickle as pickle
    print 'import cPickle success!'
except ImportError:
    import pickle
    print 'import pickle success!'

#写入字符串
d = dict(name='Bob', age=20, score=88)
s = pickle.dumps(d)
print type(s)

# 写入一个file-like Object
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

#写出序列
f = open('dump.txt', 'rb')
d2 = pickle.load(f)
f.close()
print d2

# 这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
print d is d2 #但不是一个对象
print d == d2 #内容相同
print type(d),type(d2)

# 注意：可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系


