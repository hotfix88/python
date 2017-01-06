# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 21:35:59 2017  : Administrator

Author: FengYang
E-mail: hotfix88@sina.com
Github: hotfix88
"""
__metaclass__ = type #确定使用新式类

#如果一个类的构造方法被重写，那么必须使用超类的未绑定构造方法
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Aaaah'
            self.hungry = False
        else:
            print 'No,thanks!'
            
b = Bird()
b.eat()
b.eat()

print '---------------调用未绑定的超类的构造方法,用这个更好----------------'
class SongBird(Bird):
    def __init__(self):        
        self.sound = "Squawk"
        Bird.__init__(self)   
        #调用未绑定的超类的构造方法，使hungry属性可以被设置
    def sing(self):
        print self.sound
sb = SongBird()
sb.sing()
sb.eat() 
sb.eat()    


print '-------------使用super函数--------------'
class SongBird2(Bird):
    def __init__(self):        
        self.sound = "Squawk"
        super(SongBird2,self).__init__()
        #确定使用新式类,调用super函数
        
    def sing(self):
        print self.sound
sb2 = SongBird2()
sb2.sing()
sb2.eat() 
sb2.eat()   




    