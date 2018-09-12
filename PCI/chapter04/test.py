#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com 
 DateTime:    Wed Sep 12 09:02:18 2018
 Description: Description
"""
__author__ = 'FYSO'


import searchengine
pagelist = ['http://wap.js.10086.cn/YHHD.thtml'] 
#https://www.crummy.com/software/BeautifulSoup/
#http://wap.js.10086.cn/YWFL.thtml
#http://wap.js.10086.cn/YHHD.thtml
crawler=searchengine.crawler()
crawler.crawl(pagelist)

