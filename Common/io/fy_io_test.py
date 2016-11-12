# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 20:35:32 2016  @author: Administrator

@author: deepblue
@GitHub: hotfix88
@Email : hotfix88@sina.com
"""
import fy_io
#sys.path.append('D:\\Git\\python\\Common\\io')

f1 = 'D:\\Git\\python\\Common\\io\\fy_io_1.txt'
f2 = 'D:\\Git\\python\\Common\\io\\fy_io_2.txt'
f3 = 'D:\\Git\\python\\Common\\io\\fy_io_3.txt'

fy_io.readfile(f1)
fy_io.readfile(f1,sp='\t')
fy_io.readfile(f2,sp=',')
fy_io.readfile(f3,sp=' ')

#return some
rownames,colnames,data = fy_io.readfile(f1)
print data[rownames.index('sohu')][colnames.index('US')]
print data[rownames.index('baidu')][colnames.index('China')]

