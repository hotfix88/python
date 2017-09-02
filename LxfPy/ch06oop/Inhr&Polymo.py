#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-09-02 08:09:16
 Description: 继承是 Inheritance 多态是 Polymorphism
"""
__author__ = 'FengYang'
print '---------------ch06.04------------------'

# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
# 新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。



# 比如，我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印：
class Animal(object):
    def run(self):
        print 'Animal is running...'
ani = Animal()
ani.run()

# 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
class Dog(Animal):
    pass

class Cat(Animal):
    pass

#继承有什么好处？最大的好处是子类获得了父类的全部功能。
dog = Dog()
cat = Cat()
dog.run()
cat.run()
print '---------'
# 当然，也可以对子类增加一些方法，并且对代码做一点改进。
class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Dog eating meat...'
class Cat(Animal):
    def run(self):
        print 'Cat is running...'
    def eat(self):
        print 'Cat eating fish...'

dog = Dog()
cat = Cat()
dog.run()
dog.eat()
cat.run()
cat.eat()
print '---------'

# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，
# 在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
# 
print isinstance(ani, Animal)
print isinstance(ani, Dog)
print isinstance(ani, Cat)

print isinstance(dog, Animal)
print isinstance(dog, Dog)
print isinstance(dog, Cat)

print isinstance(cat, Animal)
print isinstance(cat, Dog)
print isinstance(cat, Cat)

print '---------'



# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，
# 而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，
# 这就是多态真正的威力：调用方只管调用，不管细节，
# 而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
# 这就是著名的“开闭”原则：
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

# 小结

# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写；

# 有了继承，才能有多态。在调用类实例方法的时候，尽量把变量视作父类类型，这样，所有子类类型都可以正常被接收；

# 旧的方式定义Python类允许不从object类继承，但这种编程方式已经严重不推荐使用。任何时候，如果没有合适的类可以继承，就继承自object类。

