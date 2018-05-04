#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:AHP.py
@time:2018/4/27 10:14
层次分析法
"""

import numpy as np
import numpy.linalg as nplg

if __name__ == '__main__':
    da = np.loadtxt("data.csv", delimiter=",")
    sum = np.sum(da, axis=0)  # 列
    print("sum：", sum)
    col_arv = da / sum  # 对列进行归一化
    w = np.sum(col_arv, axis=1)  # 行求和
    w_n = w / np.sum(w)  # 行归一化
    print(w_n)
    print(np.max(nplg.eig(da)[0]))
