#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:apscheduler_demo2.py
@time:2018/7/30 19:42
@desc:
https://www.cnblogs.com/qq1207501666/p/9195186.html
"""

from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


def print_args(*args):
    """要定时执行的函数"""
    for arg in args:
        print(arg)


# 执行器，常用的就线程池和进程池两种
thread_pool = ThreadPoolExecutor(30)
process_pool = ProcessPoolExecutor(5)
executors = {
    'thread': thread_pool,
    'process': process_pool
}

#存储器 默认使用内存，对定时任务丢失什么的不敏感，对定时任务执行要求低
redis_store = RedisJobStore(host="172.16.120.120",port='6379')
sqlite_store = SQLAlchemyJobStore(url= 'sqlite:///jobs.sqlite')
jobstores = {
    'redis':redis_store,
    'default':sqlite_store
}
#删除被持久化的定时任务， redis_store.remove_all_jobs()

#调度器
#调度器设置
job_defaults = {
    'coalesce':False,
    'max_instances':5,
    'misfire_grace_time':60
}



