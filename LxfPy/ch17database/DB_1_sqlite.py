#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Sat Sep 23 22:35:57 2017
 Description: 数据库简介  sqlite

"""
__author__ = 'FengYang'


#为了便于程序保存和读取数据，而且，能直接通过条件快速查询到指定的数据，
#就出现了数据库（Database）这种专门用于集中存储和查询的软件。
#我们现在广泛使用的关系数据库是20世纪70年代基于关系模型的基础上诞生的。
#基于表（Table）的一对多的关系就是关系数据库的基础。

#NoSQL
#你也许还听说过NoSQL数据库，很多NoSQL宣传其速度和规模远远超过关系数据库，
#所以很多同学觉得有了NoSQL是否就不需要SQL了呢？
#千万不要被他们忽悠了，连SQL都不明白怎么可能搞明白NoSQL呢？


#数据库类别
#既然我们要使用关系数据库，就必须选择一个关系数据库。目前广泛使用的关系数据库也就这么几种：
#付费的商用数据库：
#Oracle，典型的高富帅；
#SQL Server，微软自家产品，Windows定制专款；
#DB2，IBM的产品，听起来挺高端；
#Sybase，曾经跟微软是好基友，后来关系破裂，现在家境惨淡。

#这些数据库都是不开源而且付费的，最大的好处是花了钱出了问题可以找厂家解决，
#不过在Web的世界里，常常需要部署成千上万的数据库服务器，当然不能把大把大把的银子扔给厂家，
#所以，无论是Google、Facebook，还是国内的BAT，无一例外都选择了免费的开源数据库：
#MySQL，大家都在用，一般错不了；
#PostgreSQL，学术气息有点重，其实挺不错，但知名度没有MySQL高；
#sqlite，嵌入式数据库，适合桌面和移动应用。
#作为Python开发工程师，选择哪个免费数据库呢？当然是MySQL。
#因为MySQL普及率最高，出了错，可以很容易找到解决方法。
#而且，围绕MySQL有一大堆监控和运维的工具，安装和使用很方便。
#为了能继续后面的学习，你需要从MySQL官方网站下载并安装MySQL Community Server 5.6，
#这个版本是免费的，其他高级版本是要收钱的（请放心，收钱的功能我们用不上）。

#
#SQLite是一种嵌入式数据库，它的数据库就是一个文件。
#由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，
#甚至在iOS和Android的App中都可以集成。
#Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。

# 导入SQLite驱动:
import sqlite3



  
    

try:
    print 'trying......'
    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect('test.db')
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
    print cursor.rowcount ,'row insert'
    
except  sqlite3.Error as e:
    print 'except:', e   #OperationalError: table user already exists
else:    
    pass
finally:
    print 'finally...close anything! '
    # 关闭Cursor:
    cursor.close()
    
    # 提交事务:
    conn.commit()
    
    # 关闭Connection:
    conn.close()



print '----------------query -------------'
try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # 执行查询语句:
 
    cursor.execute('select * from user where id=?', ('1',) )
    #<sqlite3.Cursor object at 0x10f8aa340>
    
    # 获得查询结果集:
    values = cursor.fetchall()
    
    print values
    #[(u'1', u'Michael')]
except  sqlite3.Error as e:
    print 'except:', e 
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



'''
try:
    conn=sqlite3.connect('test.db')
    cur=conn.cursor()
    sql="select * from hello"
    cur.execute(sql)
    res=cur.fetchall()
    print conn
    print res
except sqlite3.Error as e:
    print e
finally:
    cur.close()
    conn.close()
    print conn
    '''

