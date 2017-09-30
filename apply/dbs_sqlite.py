#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Sat Sep 23 22:35:57 2017
 Description: 数据库简介  sqlite

"""
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Sat Sep 30 15:59:26 2017
 Description: 从lxfpy移植过来
"""
__author__ = 'FengYang'


# 导入SQLite驱动:
import sqlite3 
    

try:
    print( 'trying......')
    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect('dbs_sqlite_test.db')
    # 创建一个Cursor:
    cursor = conn.cursor()
    # 执行一条SQL语句，创建user表:
    sql = 'create table user (id varchar(20) primary key, name varchar(20))'
    cursor.execute(sql)
    #<sqlite3.Cursor object at 0x10f8aa260>
    
    # 继续执行一条SQL语句，插入一条记录:
    sql = 'insert into user (id, name) values (\'1\', \'Michael\')'
    cursor.execute(sql)
    #<sqlite3.Cursor object at 0x10f8aa260>
    # 通过rowcount获得插入的行数:
    print( cursor.rowcount ,'row insert')
    
except  sqlite3.Error as e:
    print('except:', e)   #OperationalError: table user already exists
else:    
    pass
finally:
    print( 'finally...close anything! ')
    # 关闭Cursor:
    cursor.close()
    
    # 提交事务:
    conn.commit()
    
    # 关闭Connection:
    conn.close()



print( '----------------query -------------')
try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # 执行查询语句:
 
    cursor.execute('select * from user where id=?', ('1',) )
    #<sqlite3.Cursor object at 0x10f8aa340>
    
    # 获得查询结果集:
    values = cursor.fetchall()
    
    print( values)
    #[(u'1', u'Michael')]
except  sqlite3.Error as e:
    print( 'except:', e )
finally:
    cursor.close()
    conn.close()

'''
使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。
使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：
cursor.execute('select * from user where name=? and pwd=?', ('abc', '123456'))
SQLite支持常见的标准SQL语句以及几种常见的数据类型。具体文档请参阅SQLite官方网站。
'''

    


#小结
#
#在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。
#
#要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。




