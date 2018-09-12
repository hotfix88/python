#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    Tue Sep 11 16:34:52 2018
 Description: Description
"""
__author__ = 'FYSO'

print(33333332)

import urllib #在python2中为urllib2
from urllib.parse import urljoin #在python2中为from urlparse import urljoin
from bs4 import BeautifulSoup

#构造忽略单词列表
ignorewords = set(['the','of','to','and','a','in','is','it'])


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
        print('----------------Indexing %s '%url ) #临时打印

    #从HTML提取文字
    def gettextonly(self,soup):
        print('----------------call soup %s '%soup )#临时打印
        return None

    #对非空字符 分词处理
    def separatewords(self,text):
        return None

    #如果url已经建立过索引，返回True
    def isindexed(self,url):
        print('----------------isindexed test %s '%url )#临时打印
        return False

    #添加管理两个网页的链接
    def addlinkref(self,urlFrom,urlTo,linkText):
        pass

    #从以小组网页进行广度优先搜索，知道某一给定深度
    #期间为网页建立索引
    def crawl(self,pages,depth=2):
        for i in range(depth):
            newpages=set()
            for page in pages:
                try:
                    c = urllib.request.urlopen(page) #python2 c = urllib2.urlopen(page)
                except:
                    print('-------could not open : %s '%page)
                    continue
                soup=BeautifulSoup(c.read())
                self.addtoindex(page,soup)
                
                links = soup('a')
                for link in links:
                    if('href' in dict(link.attrs)):
                        url = urljoin(page,link['href'])
                        if url.find("'") != -1:
                            continue
                        url = url.split('#')[0]
                        if url[0:4]=='http' and not self.isindexed(url):
                            newpages.add(url)
                        linkText = self.gettextonly(link)
                        self.addlinkref(page,url,linkText)
                self.dbcommit()
            pages=newpages
                            
        pass

    #创建数据库表
    def createindextables(self):
        pass


























