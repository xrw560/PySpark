#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:numpy_6.py
@time:2018/5/8 14:17
"""
import numpy as np

if __name__ == '__main__':
    # z = np.zeros((8, 8), dtype=int)
    # # 8*8棋盘矩阵，其中1、3、5、7行&&0、2、4、6列的元素置为1 ;  1 ,3，5，7列&&0,2,4,6行也是1
    # z[1::2, ::2] = 1
    # z[::2, 1::2] = 1
    # # print(z)

    # # min() max()函数
    # z = np.random.random((10, 10))
    # zmin, zmax = z.min(), z.max()
    # print(zmin, zmax)

    # 归一化，将矩阵规格化到0~1，即最小的变成0，最大的变成1，最小与最大之间的等比缩放
    # z = 10 * np.random.random((5, 5))
    # print(z)
    # zmin, zmax = z.min(), z.max()
    # z = (z - zmin) / (zmax - zmin)
    # print(z)

    # 生成0~10之间均匀分布的11个数，包括0和10
    z = np.linspace(0, 10, 11, endpoint=True, retstep=True)
    print(z)
    print(help(np.linspace))
