#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:numpy_4.py
@time:2018/5/8 13:42
"""
import numpy as np

if __name__ == '__main__':
    B = np.arange(3)
    # print(B)  # [0 1 2]
    # print(np.sqrt(B))  # [0.         1.         1.41421356]

    # return the floor of the input
    a = np.floor(10 * np.random.random((3, 4)))
    # print(a)
    # # flatten the array
    # print(a.ravel())
    # print(a.T)
    # a.resize((2, 6))  # 不生成新的矩阵
    # print(a)

    # if a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated.
    # print(a.reshape((4, -1))) # 生成新的矩阵
    # print(a)

    # a = np.floor(10 * np.random.random((2, 2)))
    # b = np.floor(10 * np.random.random((2, 2)))
    # print(a)
    # print('----')
    # print(b)
    # print('----')
    # print(np.hstack((a, b)))    # 水平拼接为一个矩阵
    # print('----')
    # print(np.vstack((a, b)))    # 垂直拼接为一个矩阵

    # a = np.floor(10 * np.random.random((2, 12)))
    # print(a)
    # # print(np.hsplit(a,3)) # 切分为3份
    # print(np.hsplit(a, (3, 4)))  # split a after the third and the fourth column
    # a = np.floor(10 * np.random.random((12, 2)))
    # print(a)
    # print(np.vsplit(a, 3))

    # 复制
    # Simple assignments make no copy of array objects or of their data.
    a = np.arange(12)
    b = a
    # print(b is a)  # a and b are two names for the same ndarray object
    b.shape = 3, 4
    # print(a.shape)
    # print(a)
    # print(id(a))
    # print(id(b))

    # id 不相同，但是公用数据
    # the view method creates a new array object that looks at the same data.
    c = a.view()
    # print(c is a)
    c.shape = 2, 6
    # print(a.shape)
    c[0, 4] = 1234
    # print(a)
    # print(c)

    d = a.copy()
    print(d is a)
    d[0, 0] = 9999
    print(d)
    print(a)
