#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Tue Sep 26 23:39:29 2017
 Description: Description
"""
__author__ = 'FengYang'


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

# 定义Book对象:
class Book(Base):
    __tablename__ = 'book'
    
    id = Column(String(20))
    name = Column(String(100))

 

# 初始化数据库连接:
#create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
#'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'

engine = create_engine('mysql+mysqlconnector://root:123123@localhost:3306/mysql')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(Book).filter(Book.id=='1').one()
# 打印类型和对象的name属性:
#print 'type:', type(user)
#print 'name:', user.name
# 关闭Session:
session.close()
 

