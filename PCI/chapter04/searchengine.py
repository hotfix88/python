#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    Tue Sep 11 16:34:52 2018
 Description: Description
"""
__author__ = 'FYSO'

import sys
print(sys.version)
#2.7.6 (default, Nov 10 2013, 19:24:24) [MSC v.1500 64 bit (AMD64)]

class crawler:
    #初始化类，并传入数据库名称
    def __init__(self):
        pass

    def __del__(self):
        pass

    def dbcommit(self):
        pass

    #获取条目id，如果不存在，则新建
    def getentryid(self,table,field,value,createnew=True):
        return None

    #为每个网页建立索引
    def addtoindex(self,url,soup):
        print('Indexing %s '%url )

    #从HTML提取文字
    def gettextonly(self,soup):
        return None

    #对非空字符 分词处理
    def separatewords(self,text):
        return None

    #如果url已经建立过索引，返回True
    def isindexed(self,url):
        return False

    #添加管理两个网页的链接
    def addlinkref(self,urlFrom,urlTo,linkText):
        pass

    #从以小组网页进行广度优先搜索，知道某一给定深度
    #期间为网页建立索引
    def crawl(self,pages,depth=2):
        pass

    #创建数据库表
    def createindextables(self):
        pass


# http://segaran.com/wiki



import urllib2
c=urllib2.urlopen('https://www.wikipedia.org/') #http://www.baidu.com
contents = c.read()
print(contents[0:200])
'''
 '<!DOCTYPE html>\n<html lang="mul" class="no-js">\n<head>\n
 <meta charset="utf-8">\n<title>Wikipedia</title>\n<meta
 name="description" content="Wikipedia is a free online encyclopedia,
 created and edited by
'''















