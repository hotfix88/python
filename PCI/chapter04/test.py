#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso 
 DateTime:    Wed Sep 12 09:02:18 2018
 Description: Description
"""
__author__ = 'FYSO'


import searchengine
pagelist = ['https://www.crummy.com/software/BeautifulSoup/'] 
#https://www.crummy.com/software/BeautifulSoup/
#http://wap.j s.100 86.cn/YW FL.thtml
#http://wap.j s.100 86.cn/YH HD.thtml  #

#初始化类
crawler=searchengine.crawler('searchindex.db')

#建库和索引
crawler.createindextables()

#爬取数据
crawler.crawl(pagelist,2,0)


