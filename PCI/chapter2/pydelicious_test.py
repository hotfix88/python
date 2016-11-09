# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 20:06:45 2016
@author: Administrator
created by CMCC.fengyang
fyso@163.com
"""

'''
C:\Users\Administrator>pip install feedparser
Downloading/unpacking feedparser
  Running setup.py (path:c:\users\admini~1\appdata\local\temp\pip_build_Administ
rator\feedparser\setup.py) egg_info for package feedparser

Installing collected packages: feedparser
  Running setup.py install for feedparser

Successfully installed feedparser
Cleaning up...
'''

import pydelicious

print '\n\n------------------1.Building a del.icio.us Link Recommender-------------------'
print pydelicious.get_popular(tag='Programming')
#print pydelicious.get_urlposts('https://shop.icio.us/sales/the-limited-edition-black-hawk-drone-hd-camera?utm_source=del.icio.us&utm_medium=referral&utm_campaign=the-limited-edition-black-hawk-drone-hd-camera')

print '\n\n------------------2.Building the Dataset-------------------'
from deliciousrec import *
delusers = initializeUserDict('Programming')
#delusers['delicious'] = {}
#fillItems(delusers)
#PyDeliciousException: HTTP Error 500: Internal Server Error

