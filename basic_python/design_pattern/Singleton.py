#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:Singleton.py
@time:2018/8/9 15:56
@desc:
"""


class Singleton:
    """A python style singleton"""

    def __new__(cls):
        print("__new__")
        if not hasattr(cls, "_instance"):
            org = super(Singleton, cls)
            cls._instance = org.__new__(cls)
        return cls._instance

    def __init__(self):
        print("__init__")


if __name__ == "__main__":
    obj1 = Singleton()
    obj2 = Singleton()
    obj1.attr1 = "value1"
    print(id(obj1))
    print(id(obj2))
