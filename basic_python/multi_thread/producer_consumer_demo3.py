#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:producer_consumer_demo3.py
@time:2018/7/30 19:06
@desc:
"""
import threading

a_list = None
condition = threading.Condition()


def doSet():
    if condition.acquire():
        while a_list is None:
            condition.wait()
        for i in range(len(a_list))[::-1]:
            a_list[i] = 1
        condition.release()


def doPrint():
    if condition.acquire():
        while a_list is None:
            condition.wait()
        for i in a_list:
            print(i, end=",")
        print()
        condition.release()


def doCreate():
    global a_list
    if condition.acquire():
        if a_list is None:
            a_list = [0 for i in range(10)]
            condition.notifyAll()
        condition.release()


tset = threading.Thread(target=doSet, name="teSet")
tprint = threading.Thread(target=doPrint, name="tPrint")
tcreate = threading.Thread(target=doCreate, name="tCreate")

tset.start()
tprint.start()
tcreate.start()
