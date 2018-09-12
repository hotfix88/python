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
import sqlite3.dbapi2 as sqlite
import re


#构造忽略单词列表
ignorewords = set(['the','of','to','and','a','in','is','it'])


MAXTEST = 100000

class crawler:
    #初始化类，并传入数据库名称
    def __init__(self,dbname):
        print(':-) call init')
        self.con=sqlite.connect(dbname)
        pass

    def __del__(self):
        print(':-) call del')
        self.con.close()    
        pass

    def dbcommit(self):
        print(':-) call db')
        self.con.commit()
        pass
    

    #获取条目id，如果不存在，则新建
    def getentryid(self,table,field,value,createnew=True):
        return 1

    #为每个网页建立索引
    def addtoindex(self,url,soup):
        print(':-) addtoindex(),url = %s '%url ) #临时打印
        print(':-) addtoindex(),soup = %s '%soup )
        if self.isindexed(url):
            return
        print('Indexing'+url)
        
        #获取每个单词
        text = self.gettextonly(soup)
        words = self.separatewords(text)
        
        #得到URL的id
        urlid=self.getentryid('urllist','url',url)
        
        #将每个单词和该url关联
        for i in range(len(words)):
            word = words[i]
            if word in ignorewords:
                continue
            wordid = self.getentryid('wordlist','word',word)
            self.con.execute('insert to wordlocation(urlid,wordid,location)\
                             values(%d,%d,%d)'%(urlid,wordid,i))
        

    #从HTML提取文字,
    #返回一个长字符串，包含网页中所有文字。
    def gettextonly(self,soup):
        print(':-) gettextonly(),soup = %s '%soup )#临时打印
        v = soup.string
        if v == None:
            c = soup.contents
            resulttext = ''
            for t in c:
                subtext = self.gettextonly(t)#递归调用
                resulttext+=subtext+'\n'
            return resulttext
        else:
            return v.strip()
        #return None

    #对非空字符 分词处理
    #将字符串拆分成一组独立单词
    def separatewords(self,text):
        splitter = re.compile('\\W*') #将任何非字母，非数字字符当做分隔符
        return [s.lower() for s in splitter.split(text) if s != '']
        #return None

    #如果url已经建立过索引，返回True
    def isindexed(self,url):
        print('----------------isindexed test %s '%url )#临时打印
        return False

    #添加管理两个网页的链接
    def addlinkref(self,urlFrom,urlTo,linkText):
        pass

    #从以小组网页进行广度优先搜索，知道某一给定深度
    #期间为网页建立索引
    #增加一个测试结束标记 maxtest
    def crawl(self,pages,depth=2,maxtest = 100000000):
        TEST = 0
        for i in range(depth):
            newpages=set()
            for page in pages:
                try:
                    c = urllib.request.urlopen(page) #python2 c = urllib2.urlopen(page)
                except:
                    print('could not open : %s '%page)
                    continue
                soup=BeautifulSoup(c.read())
                self.addtoindex(page,soup)
                
                links = soup('a')
                print(':-) links = %s'%links)
                for link in links:
                    if('href' in dict(link.attrs)):
                        url = urljoin(page,link['href'])
                        if url.find("'") != -1:
                            continue
                        url = url.split('#')[0]
                        if url[0:4]=='http' and not self.isindexed(url):
                            newpages.add(url)
                        linkText = self.gettextonly(link)
                        print(':-) linkText = %s'%linkText)
                        self.addlinkref(page,url,linkText)
                self.dbcommit()
            pages=newpages
            
            TEST +=1
            if TEST > maxtest:
                break
                            
        pass

    #创建数据库表
    def createindextables(self):
        try:
            self.con.execute('create table urllist(url)')
        except:
            print('table urllist exist')
        
        try:
            self.con.execute('create table wordlist(word)')
        except:
            print('table wordlist exist')
            
        try:
            self.con.execute('create table wordlocation(urlid,wordid,location)')
        except:
            print('table wordlocation exist')
        
        try:
            self.con.execute('create table link(fromid integer,toid integer')
        except:
            print('table link exist')
        
        try:
            self.con.execute('create table linkwords(wordid,linkid')
        except:
            print('table linkwords exist')
        
        try:
            self.con.execute('create index urlidx on urllist(url)')
        except:
            print('index urlidx exist')
        
        try:
            self.con.execute('create index wordidx on wordlist(word)')
        except:
            print('index wordidx exist')
        
        try:
            self.con.execute('create index wordurlidx on wordlocation(wordid)')
        except:
            print('index wordurlidx exist')
        
        try:
            self.con.execute('create index urltoidx on link(toid)')
        except:
            print('index urltoidx exist')
        
        try:
            self.con.execute('create index urlfromidx on link(fromid)')
        except:
            print('index urlfromidx exist')
        
        try:
            self.dbcommit() 
        except:
            print('dbcommit failure')  
               
        pass
    



























