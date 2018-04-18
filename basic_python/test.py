#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:test.py
@time:2018/4/16 17:42
"""
import datetime
import random

if __name__ == '__main__':
    # now = datetime.datetime.now()
    # one_hour_later = now + datetime.timedelta(milliseconds=1000)
    # print(now)
    # print(one_hour_later)
    # print(now.strftime('%Y%m%d%H%M%S%f'))
    # print(len(now.strftime('%Y%m%d%H%M%S%f')))

    print('SS{:0>20},info,A1,{:}'.format('2355', '011000111100'))
    print('SS{:0>20},info,A2,{:}'.format('2355', 0.05 + (random.random() * 0.05)))
    print('SS{:0>20},info,A3,{:}'.format('2355', 0.05 + (random.random() * 0.05)))
    print('SS{:0>20},info,A4,{:}'.format('2355', 7 + (random.random() * 0.4)))
    print('SS{:0>20},info,A5,{:}'.format('2355', 6 + (random.random() * 0.4)))
    print('SS{:0>20},info,A6,{:}'.format('2355', 0))
