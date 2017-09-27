#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Tue Sep 26 08:53:56 2017
 Description: Description
"""
__author__ = 'FengYang'

# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:    
conn = mysql.connector.connect(user='root', password='123123', database='mysql', use_unicode=True)
cursor = conn.cursor()


# 创建user表: 
try:  
    #sql = 'create table if not exists user (id varchar(20) primary key, name varchar(20))'
    sql = 'create table user2 (id varchar(20) primary key, name varchar(20))'   
    cursor.execute(sql)
    conn.commit()    
    print cursor.rowcount  
    print 'create table user2 success...'
except  Exception as e:
    print 'except:', e 
   
finally:
    pass


# 插入一行记录，
try:   
    #注意MySQL的占位符是%s:
    cursor.execute('insert into user2 (id, name) values (%s, %s)', ['1', 'Michael'])
    cursor.execute('insert into user2 (id, name) values (%s, %s)', ['2', 'Tom'])
    cursor.execute('insert into user2 (id, name) values (%s, %s)', ['3', 'Adam'])
    # 提交事务:
    conn.commit()
    print 'insert table user2 success...'
except  Exception as e:
    print 'except:', e    
finally:
    pass

# 运行查询:
cursor.execute('select * from user2 where id >= %s', ('1',))
values = cursor.fetchall()  #在execute 一些select 后,如果不调用fetcchxxx 之类的语法,就去执行insert 或者update 或者其他语句,有的时候会出错:Unread result found
print values

#删除记录
#cursor.execute('delete from user2 where id = %s', ('1',))
#conn.commit()


# 关闭Cursor和Connection:
cursor.close()
conn.close()
print 'the end'


'''
#连接
import mysql.connector
conn = mysql.connector.connect(user='root', password='123123', database='mysql', use_unicode=True)
cursor = conn.cursor()
print cursor

#建表 user2
sql = 'create table user2 (id varchar(20) primary key, name varchar(20))'   
cursor.execute(sql)
conn.commit()    
print cursor.rowcount


  
#删表
cursor.execute('drop table user2')
conn.commit()

#删jilu
cursor.execute('delete from user2 where id = %s', ('1',))
conn.commit()

#查询条件
cursor.execute('select * from user2 where id = %s', ('2',))
values = cursor.fetchall()  
print values

#查询全部
cursor.execute('select * from user2')
values = cursor.fetchall()  
print values

#插入
cursor.execute('insert into user2 (id, name) values (%s, %s)', ['1', 'Michael'])
conn.commit()
cursor.execute('insert into user2 (id, name) values (%s, %s)', ['4', 'Michael'])

# 关闭Cursor和Connection:
cursor.close()
conn.close()

'''
#-----------------------------
'''
#连接
import mysql.connector
conn = mysql.connector.connect(user='root', password='123123', database='mysql', use_unicode=True)
cursor = conn.cursor()
print cursor


#删表 book
cursor.execute('drop table book')
conn.commit()

#建表 book
sql = 'create table book (id varchar(20) , name varchar(100))'   
cursor.execute(sql)
conn.commit()    
print cursor.rowcount

#插入 book
cursor.execute('insert into book (id, name) values (%s, %s)', ['1', 'A'])
cursor.execute('insert into book (id, name) values (%s, %s)', ['1', 'B'])
cursor.execute('insert into book (id, name) values (%s, %s)', ['1', 'C'])
cursor.execute('insert into book (id, name) values (%s, %s)', ['1', 'D'])
cursor.execute('insert into book (id, name) values (%s, %s)', ['2', 'A'])
cursor.execute('insert into book (id, name) values (%s, %s)', ['2', 'C'])
cursor.execute('insert into book (id, name) values (%s, %s)', ['3', 'C'])
cursor.execute('insert into book (id, name) values (%s, %s)', ['3', 'D'])
cursor.execute('insert into book (id, name) values (%s, %s)', ['3', 'E'])
cursor.execute('insert into book (id, name) values (%s, %s)', ['4', 'F'])
cursor.execute('insert into book (id, name) values (%s, %s)', ['4', 'A'])
cursor.execute('insert into book (id, name) values (%s, %s)', ['5', 'C'])
conn.commit()

#查询全部book
cursor.execute('select * from book')
values = cursor.fetchall()  
print values

#查询条件
cursor.execute('select * from book where id = %s', ('1',))
values = cursor.fetchall()  
print values

# 关闭Cursor和Connection:
cursor.close()
conn.close()

'''

