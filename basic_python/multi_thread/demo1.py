#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:demo1.py
@time:2018/7/30 16:28
@desc:
"""
import threading
from time import ctime, sleep


def music(func):
    for i in range(2):
        print("I was listening to %s. %s" % (func, ctime()))
        sleep(1)


def move(func):
    for i in range(2):
        print("I was at the %s! %s" % (func, ctime()))
        sleep(1)


def player(name):
    r = name.split(".")[1]
    if r == 'mp3':
        music(name)
    elif r == 'mp4':
        move(name)
    else:
        print("error: The format is not recognized!")


li = ['爱情买卖.mp3', '阿凡达.mp4']
threads = []
files = range(len(li))

for i in li:
    t = threading.Thread(target=player, args=(i,))
    threads.append(t)

if __name__ == "__main__":
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()

    print("all over %s" % ctime())
