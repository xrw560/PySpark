#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:Turtle.py
@time:2018/4/10 20:11
"""
"""
    self：相当于C++中的指针，对象自身
    __init__(self)：构造方法
    公有和私有：对象的属性和方法默认是公有的
    在Python中定义私有变量只需要在变量名或函数名前加上“__”两个下划线，那么这个函数或变量就会为私有的了
    _类名__属性名：可以访问私有属性
"""


class Turtle:  # Python中的类名约定以大写字母开头
    """"关于类的一个简单例子"""
    # 属性
    color = 'gree'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    # 方法
    def climb(self):
        print("我正在努力的向前爬.......")


if __name__ == '__main__':
    tt = Turtle()
    tt.climb()
