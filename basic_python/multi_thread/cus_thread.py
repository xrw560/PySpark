#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:cus_thread.py
@time:2018/7/30 18:14
@desc:
"""
import threading
from time import sleep, ctime


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        # threading.Thread.__init__(self)
        super(MyThread, self).__init__()
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def super_play(file, time):
    for i in range(2):
        print("start playing: %s! %s" % (file, ctime()))
        sleep(time)


rdict = {'爱情买卖.mp3': 1, '阿凡达.mp4':1}

# 创建线程
threads = []
files = range(len(rdict))

for k, v in rdict.items():
    t = MyThread(super_play, (k, v), super_play.__name__)
    threads.append(t)

if __name__ == "__main__":
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

    # 主线程
    print("end: %s" % ctime())
