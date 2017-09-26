#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Tue Sep 26 22:58:50 2017
 Description: Description
"""
__author__ = 'FengYang'

#数据库表是一个二维表，包含多行多列。把一个表的内容用Python的数据结构表示出来的话，
#可以用一个list表示多行，list的每一个元素是tuple，表示一行记录，
#比如，包含id和name的user表：



#这就是传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。
#是不是很简单？
#但是由谁来做这个转换呢？所以ORM框架应运而生。
#在Python中，最有名的ORM框架是SQLAlchemy。我们来看看SQLAlchemy的用法。




# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User2(Base):
    # 表的名字:
    __tablename__ = 'user2'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    
# 定义School对象:
class School(Base):
    __tablename__ = 'school'
    id =  Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
#create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
#'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'

engine = create_engine('mysql+mysqlconnector://root:123123@localhost:3306/mysql')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


try:   
    #由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = User2(id='6', name='Bob')
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()
    print 'insert table user2 success...'
except  Exception as e:
    print 'except:', e    
    print '-----------------\n'
finally:
    pass




#可见，关键是获取session，然后把对象添加到session，最后提交并关闭。
#Session对象可视为当前数据库连接。
#如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是tuple，而是User对象。
#SQLAlchemy提供的查询接口如下：

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User2).filter(User2.id=='1').one()
# 打印类型和对象的name属性:
print 'type:', type(user)
print 'name:', user.name
# 关闭Session:
session.close()



print '--------------------------------------------'
'''
#由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。
#
#例如，如果一个User拥有多个Book，就可以定义一对多关系如下：
#ForeignKey 需要引入   
from sqlalchemy.schema import ForeignKey
#relationship 需要引入   
from sqlalchemy.orm import relationship

'''

'''
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')#NameError: name 'relationship' is not defined
'''

'''
class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20))
    name = Column(String(100))
    # “多”的一方的book表是通过外键关联到user表的:
#    user_id = Column(String(20), ForeignKey('user.id'))

engine = create_engine('mysql+mysqlconnector://root:123123@localhost:3306/mysql')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
book = session.query(Book).filter(Book.id=='1').all()
# 打印类型和对象的name属性:
#print 'book:', type(book)
#print 'name:', User2.id
# 关闭Session:
session.close()
'''
#
#小结
#
#ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。
#
#正确使用ORM的前提是了解关系数据库的原理。

