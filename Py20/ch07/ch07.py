# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 21:02:26 2016  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""

print '---------------多态：不用关心类的对象类型直接进行方法调用---------------'
print  'abc'.count('a')
print [1,2,3,'a'].count('a')
#无论是什么，字符串还是list，都能得到想要的结果
from random import choice
l =['hello world','get','see',['a','e'],'e','get the bee']
for i in range(5):
    x = choice(l)
    print x, x.count('e')
#tips：尽量避免使用函数显式的检查类型！

print '---------------封装：不用关心对象如何构建而直接使用---------------'    
#简单的说，就是对象 有方法 和属性！属性和内部变量一样。
print '---------------继承：学习父类的方法---------------'

print '--------------类是什么？---------------'
#对象是类的实例instance
#python中，使用Bird Lark来表示类
print '--------------类定义---------------'
__metaclass__ = type #确定使用新式类
class Person :
    'an example for class'
    def setName(self,name):
        self.name = name #隐性的定义了  name属性
    def getName(self):
        return self.name
    def greet(self):
        print 'hello,world! I\'m %s !' %self.name
        
foo = Person()
bar = Person()
foo.setName('Tom')
bar.setName('Jack')
foo.greet()
bar.greet()        
print foo.name
print bar.name
print foo.getName()
print bar.getName()        
Person.greet(foo)    #另一种调用方式  
#self是方法和函数区别的地方！
     
print '--------------类定义2---------------'
#__metaclass__ = type #确定使用新式类
class Bird :
    'an example for class'
    song = 'Squaawk'
    def sing(self):
        print self.song
        
bird = Bird()
bird.sing()
print bird.song
birdson = bird.sing
birdson()
bird.song = 'Fell'
birdson()      

print '--------------对象的状态（属性字段），应该对外隐藏---------------'
class Secret:
    
    def __inaccessible(self):
        print "bet you can't see me!"

    def accessible(self):
        print "The message is :"
        self.__inaccessible()

s = Secret()
s.accessible() 
#s.__inaccessible()       
s._Secret__inaccessible()

#事实上，python没有真正的私有化隐藏！
#from module import * 不会导入有下划线开头的名字！！！


print '--------------lambda---------------'        
def foo1(x):
    return x*x
foo2 = lambda x:x*x

print foo1(4)
print foo2(5)        
    
  
print '--------------类的命名空间---------------'  
class MemberCounter:
    members = 0  #可供类的所有成员调用
    def init(self):
        MemberCounter.members += 1
    
    def setName(self,name):
        self.name = name

m1 = MemberCounter()
m1.init()         
print m1.members

m2 = MemberCounter()
m2.init()         
print m1.members,m2.members

m2.members = 'Two'
print m1.members,m2.members

m2.init()#初始化了公共区域的members
print m1.members,m2.members


print '-------隐式命名---------'
m1.setName('m1')
print m1.name
m2.setName('m2')
print m2.name


print '--------------子类：这本书里面叫超类，超过了父类更牛B！所以叫超类---------------'  
class Filter:
    def init(self):
        self.blocked=[]
    def filter(self,seq):   #真正调用的时候self可以忽略显示使用
        return [x for x in seq if x not in self.blocked]

t = ['apple','pen','spam']
f = Filter()
f.init()  #手动初始化
print f.filter(t)   #其实什么都没有过滤
print '----------------'
class SpamFilter(Filter):
    def init(self):
        self.blocked=['spam']
s = SpamFilter()
s.init()
print s.filter(t) 
print '----------------'
class ApplepenFilter(SpamFilter):
    def init(self):
        self.blocked=['apple','pen']
a = ApplepenFilter()
a.init()
print a.filter(t) 


print '--------------检查继承issubclass---------------'  
print issubclass(Filter,SpamFilter)
print issubclass(Filter,Filter)
print issubclass(SpamFilter,Filter)
print issubclass(ApplepenFilter,Filter)  #爷爷辈也可以查出来
 
print '----------------' 
print SpamFilter.__bases__
print Filter.__bases__
print ApplepenFilter.__bases__

print '----------------'
print f.__class__
print s.__class__
print a.__class__

print '----------------'
print type(f)
print type(s)
print type(a)


print '--------------多重继承 multiple inheritance，新手尽量少用。---------------'  
class Calculator:
    def calc(self,exp):
        self.value = eval(exp)
        return self.value
class Talker:
    def talk(self):
        print 'hi,my value is ',self.value
class TalkingCalc(Calculator,Talker):  #多重继承，顺序有讲究！
    pass

c = Calculator()
v = c.calc('3*9')
print v

t = Talker() #其实对象t只有方法，没有属性！你不调用talk就没事

tc = TalkingCalc()
tc.calc("1+3*9")
tc.talk()

print TalkingCalc.__bases__
