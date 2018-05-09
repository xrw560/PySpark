#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:numpy_7.py
@time:2018/5/8 14:25
"""
import numpy as np

if __name__ == '__main__':
    a = np.arange(25).reshape(5, 5)
    # print(a)
    # 交换矩阵的其中两行
    a[[0, 1]] = a[[1, 0]]
    # print(a)

    z = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
    a = 5.1
    # print(np.abs(z - a).argmin())  # 5

    # 判断二维矩阵中有没有一整列数为0
    z = np.random.randint(0, 3, (2, 10))
    print(z)
    print(z.any(axis=0))

    # 生成二维的高斯矩阵
    print(help(np.random.randint))
