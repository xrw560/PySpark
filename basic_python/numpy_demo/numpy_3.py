#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:numpy_3.py
@time:2018/5/8 10:26
"""
import numpy as np

if __name__ == '__main__':
    # print(np.arange(15)) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
    a = np.arange(15).reshape(3, 5)
    # print(a)

    # print(a.shape)  # (3, 5)

    # the number os axes (dimensions) of the array
    # print(a.ndim)  # 2

    # print(a.dtype.name)  # int32

    # the total number of elements of the array
    # print(a.size)

    # print(np.zeros((3, 4)))

    # print(np.ones((2, 3, 4), dtype=np.int32))

    # print(np.arange(10, 30, 5))  # [10 15 20 25]

    # print(np.arange(0, 2, 0.3))  # [0.  0.3 0.6 0.9 1.2 1.5 1.8]

    # print(np.arange(12).reshape(4, 3))

    # 权重参数初始化
    # print(np.random.random((2, 3)))

    from numpy import pi

    # print(np.linspace(0, 2 * pi, 100))  # 在区间平均取100个数
    # print(np.sin(np.linspace(0, 2 * pi, 100)))

    # the product乘积 operator * operates elementwise in Numpy arrays
    a = np.array([20, 30, 40, 50])
    b = np.arange(4)
    # print(a - b)
    # print(b ** 2)
    # print(b < 35)

    A = np.array([
        [1, 1],
        [0, 1]])
    B = np.array([
        [2, 0],
        [3, 4]])
    print(A * B)    # 对应位置相乘
    print("-----------------")
    print(A.dot(B))  # 矩阵乘法
    print("-----------------")
    print(np.dot(A, B))
