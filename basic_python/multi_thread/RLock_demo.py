#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:RLock_demo.py
@time:2018/7/30 18:38
@desc:
RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令。RLock使用了“拥有的线程”和“递归等级”的概念，处于锁定状态时，RLock被某个线程拥有。拥有RLock的线程可以再次调用acquire()，释放锁时需要调用release()相同次数。
可以认为RLock包含一个锁定池和一个初始值为0的计数器，每次成功调用 acquire()/release()，计数器将+1/-1，为0时锁处于未锁定状态。
简言之：Lock属于全局，Rlock属于线程。
构造方法：
Lock()，Rlock（）,推荐使用Rlock()
实例方法：
　　acquire([timeout]): 尝试获得锁定。使线程进入同步阻塞状态。
　　release(): 释放锁。使用前线程必须已获得锁定，否则将抛出异常。
"""

import threading

r_lock = threading.RLock()  # RLock对象
r_lock.acquire()
r_lock.acquire()  # 在同一线程内，程序不会堵塞。
r_lock.release()
r_lock.release()  # 释放锁时需要调用release()相同次数。
