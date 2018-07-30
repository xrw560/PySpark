#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:Lock_demo1.py
@time:2018/7/30 18:32
@desc:
Lock（指令锁）是可用的最低级的同步指令。Lock处于锁定状态时，不被特定的线程拥有。
Lock包含两种状态——锁定和非锁定，以及两个基本的方法。
可以认为Lock有一个锁定池，当线程请求锁定时，将线程至于池中，直到获得锁定后出池。
池中的线程处于状态图中的同步阻塞状态。
"""

import threading
import time

g1_num = 0

lock = threading.Lock()


# 全局变量在在每次被调用时都要获得锁，才能操作，因此保证了共享数据的安全性
# 调用acquire([timeout])时，线程将一直阻塞，
# 直到获得锁定或者直到timeout秒后（timeout参数可选）。
# 返回是否获得锁。
def Func():
    lock.acquire()
    global g1_num
    g1_num += 1
    time.sleep(1)
    print(g1_num)
    lock.release()


for i in range(10):
    t = threading.Thread(target=Func)
    t.start()
