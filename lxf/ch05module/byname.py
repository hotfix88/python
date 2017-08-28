#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-08-28 21:03:30
 Description: 别名
"""

print '-----------1/别名-----------'

# 导入模块时，还可以使用别名，这样，可以在运行时根据当前环境选择最合适的模块。
# 比如Python标准库一般会提供StringIO和cStringIO两个库，这两个库的接口和功能是一样的，
# 但是cStringIO是C写的，速度更快，所以，你会经常看到这样的写法：
try:
    import cStringIO as StringIO
    print 'import cStringIO as StringIO SUCCESS!'
except ImportError: # 导入失败会捕获到ImportError
    import StringIO
    print 'import cStringIO as StringIO FAILURE! import StringIO'
# 如果有些平台不提供cStringIO，还可以降级使用StringIO。


print '-----------2/别名-----------'
# 还有类似simplejson这样的库，
# 在Python 2.6之前是独立的第三方库，从2.6开始内置，所以，会有这样的写法：
try:
    import json # python >= 2.6
    print 'import json   SUCCESS!'
except ImportError:
    import simplejson as json # python <= 2.5
    print 'import json   FAILURE! import simplejson'

# 由于Python是动态语言，函数签名一致接口就一样，因此，无论导入哪个模块后续代码都能正常工作