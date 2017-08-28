#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-08-28 22:50:18
 Description: Description
"""
__author__ = 'FengYang'

#安装最新的版本吧，2017年8月28日，2.7.13或者3.6.2.。。什么2.7.6经典款和3.3.5经典款可以扔了！
#winpython适合懒惰人士，或者搞科学计算的人士
#
#安装的时候选择64bit，这样使用的内存范围可以大很多。
#安装的时候选择pip包！
#安装的时候选择add to sys path，这样就不用手工设置目录了！

#看版本
import sys
print sys.version_info
# sys.version_info(major=2, minor=7, micro=13, releaselevel='final', serial=0)



# ======================2.7.10.3版本下的安装==============================
# C:\Users\fyso>pip install PIL
# Collecting PIL
#   Could not find a version that satisfies the requirement PIL (from versions: )
# No matching distribution found for PIL
# You are using pip version 7.1.2, however version 9.0.1 is available.
# You should consider upgrading via the 'python -m pip install --upgrade pip' command.


# 更新pip
# C:\Users\fyso>python -m pip install --upgrade pip
# Requirement already up-to-date: pip in c:\python27\lib\site-packages
#使用pip list看安装包情况
#
#C:\Users\fyso>python -m pip install --upgrade pip
# Collecting pip
#   Downloading pip-9.0.1-py2.py3-none-any.whl (1.3MB)
#     100% |████████████████████████████████| 1.3MB 301kB/s
# Installing collected packages: pip
#   Found existing installation: pip 7.1.2
#     Uninstalling pip-7.1.2:
#       Successfully uninstalled pip-7.1.2
# Successfully installed pip-9.0.1


# C:\Users\fyso>pip install PIL
# Collecting PIL
#   Could not find a version that satisfies the requirement PIL (from versions: )
# No matching distribution found for PIL

#安装不了！


#   使用豆瓣！
# C:\Users\fyso>pip install PIL -i http://pypi.douban.com/simple
# Collecting PIL
#   The repository located at pypi.douban.com is not a trusted or secure host and is being ignored. If this repository is
# available via HTTPS it is recommended to use HTTPS instead, otherwise you may silence this warning and allow it anyways
# with '--trusted-host pypi.douban.com'.
#   Could not find a version that satisfies the requirement PIL (from versions: )
# No matching distribution found for PIL


#FY：查了下，现在PIL 叫 Pillow了！！
#Pillow (3.0.0)
#
#安装它之后一定要注意的是import Image一定要换成
#from PIL import Image 
# 还有一项需要注意的是，如果你先安装了官方的PIL的话，需要先卸载PIL再安装pillow，
# 并且要保证卸载的时候把site-packages中的PIL文件删掉了，
# 不然的话安装pillow里的PIL会与之前已经存在的PIL合并，导致一些意想不到的错误

#===========================手工安装！废弃！=================================
# 安装完毕后，系统路径  PATH=C:\Python27\;C:\Python27\Scripts;

#安装numpy！
# C:\Users\fyso>pip install numpy
# Collecting numpy
#   Downloading numpy-1.13.1-cp27-none-win_amd64.whl (7.6MB)
#     100% |████████████████████████████████| 7.6MB 49kB/s
# Installing collected packages: numpy
# Successfully installed numpy-1.13.1

#安装scipy失败！
# C:\Users\fyso>pip install scipy
# Collecting scipy
#   Downloading scipy-0.19.1.tar.gz (14.1MB)
#     100% |████████████████████████████████| 14.1MB 33kB/s
# Installing collected packages: scipy
#   Running setup.py install for scipy ... error
#   






# C:\Python27\Scripts>pip install "numpy-1.13.1+mkl-cp27-cp27m-win_amd64.whl"
# Processing c:\python27\scripts\numpy-1.13.1+mkl-cp27-cp27m-win_amd64.whl
# Installing collected packages: numpy
#   Found existing installation: numpy 1.13.1
#     Uninstalling numpy-1.13.1:
#       Successfully uninstalled numpy-1.13.1
# Successfully installed numpy-1.13.1+mkl



# numpy (1.13.1+mkl)
# pip (9.0.1)
# setuptools (28.8.0)





# C:\Python27\Scripts>pip install matplotlib
# Collecting matplotlib
#   Downloading matplotlib-2.0.2-cp27-cp27m-win_amd64.whl (8.6MB)
#     100% |████████████████████████████████| 8.6MB 49kB/s
# Collecting six>=1.10 (from matplotlib)
#   Downloading six-1.10.0-py2.py3-none-any.whl
# Collecting pytz (from matplotlib)
#   Downloading pytz-2017.2-py2.py3-none-any.whl (484kB)
#     100% |████████████████████████████████| 491kB 105kB/s
# Collecting cycler>=0.10 (from matplotlib)
#   Downloading cycler-0.10.0-py2.py3-none-any.whl
# Collecting python-dateutil (from matplotlib)
#   Downloading python_dateutil-2.6.1-py2.py3-none-any.whl (194kB)
#     100% |████████████████████████████████| 194kB 48kB/s
# Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=1.5.6 (from matplotlib)
#   Downloading pyparsing-2.2.0-py2.py3-none-any.whl (56kB)
#     100% |████████████████████████████████| 61kB 58kB/s
# Requirement already satisfied: numpy>=1.7.1 in c:\python27\lib\site-packages (from matplotlib)
# Collecting functools32 (from matplotlib)
#   Downloading functools32-3.2.3-2.zip
# Installing collected packages: six, pytz, cycler, python-dateutil, pyparsing, functools32, matplotlib
#   Running setup.py install for functools32 ... done
# Successfully installed cycler-0.10.0 functools32-3.2.3.post2 matplotlib-2.0.2 pyparsing-2.2.0 python-dateutil-2.6.1 pytz
# -2017.2 six-1.10.0



# Imported NumPy 1.8.0, SciPy 0.13.3, Matplotlib 1.3.1
# + guidata 1.6.1, guiqwt 2.3.2