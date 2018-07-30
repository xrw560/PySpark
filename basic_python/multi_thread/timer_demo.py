#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:timer_demo.py
@time:2018/7/30 19:23
@desc:
　Timer（定时器）是Thread的派生类，用于在指定时间后调用一个方法。
"""

import threading


def func():
    print("hello timer!")


timer = threading.Timer(5, func)
timer.start()
