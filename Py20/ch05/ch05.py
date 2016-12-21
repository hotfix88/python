# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:04:32 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

#看完本章，基本知识就完毕了，下面就开始抽象了！
 

x,y,z = 1,2,3
print x,y,z

#交换
x,y = y,x
print x,y

#序列解包
values = 10,20,30
print values
x,y,z = values
#x,y = values #错误

#增量赋值
x = 2
x+=2
print x
x*=3
print x
x-=4
print x
x/=3.0
print x


#假
if 0:
    print 1000
if 0.0:
    print 1000
if None:
    print 1000
if False:
    print 1000
if '':
    print 1000
if "":
    print 1000
if []:
    print 1000
if ():
    print 1000
if {}:
    print 1000
    
#真    
if 1:
    print 1001
if bool(0.0):
    print 1002
if True:
    print 1003
if '1':
    print 1004
if "2":
    print 1005
if [1]:
    print 1006
if (2):
    print 1007
if {3,3}:
    print 1008
    

   
#if
x = 5
if x == 0:
    print 2000
elif x == 3:
    print 2001
else:
    print 2002
    
#比较
x = 1
y = 1
z = 3
mv = [1,2]
mc = [1,2]
if x != mv:  #应杜绝不同类型的比较！
    print 1111
 
if x in mv:
    print 1112
    
if x is y:  #注意，is
    print 1113
if x == y:  #注意，is
    print 1119

if mv is mc: #注意比较的是对象
    print 1114

if mv == mc:
    print 1118    
    
if x <> z:  #建议使!=
    print 1115
    
if 1<z<100: #支持连续比较
    print z
    
#逻辑运算符
x = 1
y = 12
z = 32
if (x<3) and (y>4):
    print 2000

if (x<3) or (y>40):
    print 2001

if not (x>4): 
    print 2002

#短路逻辑
print x if y==12 else z
print x if y!=12 else z





#断言，当某个条件必须有，否则就玩不下去
a = 10
assert 0<a<100,'a must 0~100'
a = 2
assert 0<a<100 ,'a must 0~100'


#循环
x=12
while x<=15:
    print x
    x += 1

a = range(5)
for i in a:  #能用for就尽量不用while
    print i

#遍历字典
d = {'x':1,'y':2,'z':3}
for k in d:   #通常字典是无序的
    print k,d[k]
#有序遍历
d2 = []    
for k in d:
    d2.append(k)
d2.sort()
for k in d2:
    print k,d[k]    
    
    
#enumerate
l = ['zhangsan','lisi','zhangwu','lizhang','zhangda','zhanger']
for index,string in enumerate(l):
    if 'zhang' in string:
        l[index] = 'feng'
for i in l:
    print i


#跳出循环break
from math import sqrt
for i in range(99,0,-1):
    root = sqrt(i)
    if root == int(root):
        print i
        break

#多层跳出
print '--------------------'
for i in range(99):
    for j in range(5):
        print j
        if j >= 3:
            print '--'
            break
    if i >= 2:
        break

#continue
for i in range(10):
    if i%2 == 0:
        continue
    print i


#列表推导式
print '--------------------'
m = [x*x for x in range(10) if x%3 == 0]
print m
n = [(x,y) for x in range(3) for y in range(3)]
print n

#pass
x = 3
if x>4:
    print x
elif x == 2:
    pass
else:
    print 'end'
    
    
#del
print '--------------------'
u = 'hello'
v = u
print u,v
del u
print v     


#exec 和命名空间
print '--------------------'
exec "print 1"
scope = {}
exec 'sqrt = 3' in scope
from math import sqrt
print sqrt(4)
print scope['sqrt']

print len(scope)
print scope.keys()

#eval
scope['x']=2
scope['y']=3
print eval('x*y',scope)
print len(scope)
print scope.keys()


#chr ord
print '--------------------'
print chr(0x33)
print ord('4')