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
    # x = np.array([1, 2, 4, 7, 0])
    # x3 = [1, 2, 4, 7, 0]
    # # print(np.diff(x))
    # # y = [1, 3, 4, 7]
    # # print(np.diff(y))
    # x1 = np.array([2, 3, 4, 5, 6])
    # x4 = [2, 3, 4, 5, 6]
    # print("".join(x4))
    #
    # # err = np.array(x4) - np.array(x3)
    # #
    # # # print(np.std(err))
    # # # print((np.array(x4) - np.array(x3)).tolist())
    # #
    # # ls = (filter(lambda x: x is not None, x3))
    # # for x in ls:
    # #     print(x)

    #

    # lis = "01234567890123456789"
    # print(list(lis))
    # lis = lis[:15]
    # print(lis)
    # print(lis.count('1'))

    import random

    # print(random.random() * 16 + 30)
    # print(int(random.random()*2))
    # print(int(1.6))
    import math
    # print(round(random.random()+0.3))
    import numpy as np

    # print(np.mean(1,2,3,4,5,6,7))

    lis = [1, 3, 5]
    # print(3 in lis)
    import pandas as pd

    rdict = {1: 1, 2: 3, 3: 3, 4: 1, 5: 1, 6: 1}
    rsdict = {'key': list(rdict.keys()), 'part': list(rdict.values())}
    df = pd.DataFrame.from_dict(rsdict)
    df2 = df.groupby(df['part'])
    for k, v in df2:
        print(k)
        print(len(set(v['key'])))
        print("--------")
    # for x in list(df2['part']):
    #     print(x)
    #     print("----------")
    # rd_dict = dict(list(df2))
    # for k, v in rd_dict.items():
    #     print(k, v)
    #     print(type(k), type(v))
