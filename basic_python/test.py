#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:test.py
@time:2018/4/16 17:42
"""
import datetime
import random
import numpy as np

if __name__ == '__main__':
    x = np.array([1, 2, 4, 7, 0])
    print(np.diff(x))
    y = [1, 3, 4, 7]
    print(np.diff(y))
