#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:aps_scheduler_demo1.py
@time:2018/7/30 19:32
@desc:APScheduler是基于Quartz的一个Python定时任务框架。提供了基于日期、固定时间间隔以及crontab类型的任务，并且可以持久化任务。
"""
from datetime import datetime
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print("Tick! The time is: %s " % datetime.now())


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    # 间隔3秒钟执行一次
    scheduler.add_job(tick, 'interval', seconds=3)
    # 这里的调度任务是独立的一个线程
    scheduler.start()
    print("Press Ctrl+{0} to exit.".format('Break' if os.name == 'nt' else 'C'))
    try:
        while True:
            time.sleep(2)
            print('sleep!')
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Exit The Job!")
