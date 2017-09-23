#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com fengyangsgs@js.chinamobile.com
 DateTime:    Sat Sep 23 21:13:39 2017
 Description: Description
"""
__author__ = 'FengYang'


#Python支持多种图形界面的第三方库，包括：Tk，wxWidgets，Qt，GTK 等等。
#但是Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。
#本章简单介绍如何使用Tkinter进行GUI编程。

#第一步是导入Tkinter包的所有内容：
from Tkinter import *

#第二步是从Frame派生一个Application类，这是所有Widget的父容器：
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
'''
在GUI中，每个Button、Label、输入框等，都是一个Widget。
Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
pack()方法把Widget加入到父容器中，并实现布局。
pack()是最简单的布局，grid()可以实现更复杂的布局。
在createWidgets()方法中，我们创建一个Label和一个Button，
当Button被点击时，触发self.quit()使程序退出。
'''       

#FY：好像不是很正常的哦。

#第三步，实例化Application，并启动消息循环：
app = Application()
# 设置窗口标题:
app.master.title('Hello World!!!')
# 主消息循环:
app.mainloop()




