#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:numpy_5.py
@time:2018/5/8 14:02
"""
import numpy as np

if __name__ == '__main__':
    data = np.sin(np.arange(20)).reshape(5, 4)
    # print(data)
    ind = data.argmax(axis=0)
    # print(ind)  # [2 0 3 1]
    data_max = data[ind, range(data.shape[1])]
    # print(data.shape[0])
    # print(data[ind,:])
    # print(data_max)  # [0.98935825 0.84147098 0.99060736 0.6569866 ]
    # print(all(data_max == data.max(axis=0)))  # [0.98935825 0.84147098 0.99060736 0.6569866 ]

    a = np.arange(0, 40, 10)
    b = np.tile(a, (3, 5))  # 扩展
    # print(b)

    a = np.array([
        [4, 3, 5],
        [1, 2, 1]
    ])
    b = np.sort(a, axis=1)
    # print(b)
    a.sort(axis=1)
    # print(a)
    a = np.array([4, 3, 1, 2])
    j = np.argsort(a)
    print(j)
    print(a[j])
