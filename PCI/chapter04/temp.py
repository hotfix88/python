#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com 
 DateTime:    Wed Sep 12 08:51:35 2018
 Description: Description
"""
__author__ = 'FYSO'


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

page = 'http://segaran.com/wiki'
page = 'https://www.wikipedia.org'
try:
    c = urllib2.urlopen(page)
except:
    print('could not open %s'%page)
    