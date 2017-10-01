#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Sun Oct  1 23:30:37 2017
 Description: Description
"""
__author__ = 'FengYang'

#作者：司毅
#链接：https://www.zhihu.com/question/25404709/answer/128171562
#来源：知乎
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#! /usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib.font_manager import FontManager
import subprocess

fm = FontManager()
mat_fonts = set(f.name for f in fm.ttflist)
#print(mat_fonts)
output = subprocess.check_output('fc-list :lang=zh -f "%{family}\n"', shell=True)
#print( '*' * 10, '系统可用的中文字体', '*' * 10)
#print (output)
zh_fonts = set(f.split(',', 1)[0] for f in output.decode('utf-8').split('\n'))
available = mat_fonts & zh_fonts
print ('*' * 10, '可用的字体', '*' * 10)
for f in available:
     print (f)



#再补充一个win10的：
import matplotlib 
print(matplotlib.matplotlib_fname())      
#C:\WP362\python-3.6.2.amd64\lib\site-packages\matplotlib\mpl-data\matplotlibrc
#   2. 编辑器打开此文件 matplotlibrc
#删除font.family和font.sans-serif两行前的#
#，并在font.sans-serif后添加微软雅黑字体Microsoft YaHei  
#3. 下载字体:msyh.ttf (微软雅黑)放在matplotlib 字体文件夹下:# D:\Program Files\Python36\Lib\site-packages\matplotlib\mpl-data\fonts\ttf
#4. 删除.matplotlib/cache里面的两个缓存字体文件C:\Users\你的用户名\.matplotlib
#tex.cache   fontList.py3k.cache
#5. 重启Python
#作者：司毅
#链接：https://www.zhihu.com/question/25404709/answer/128171562
#来源：知乎
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。





#大致就是matplotlib库中没有中文字体。
#方法1
#coding:utf-8
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'


#方法2
import matplotlib
matplotlib.matplotlib_fname() #将会获得matplotlib包所在文件夹



  