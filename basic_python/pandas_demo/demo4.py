#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:demo4.py
@time:2018/8/17 11:04
@desc:
"""
import pandas as pd
from pandas import DataFrame
import numpy as np

class1 = ["A", "A", "B", "B"]
class2 = ["x1", "x2", "y1", "y2"]
m_index2 = pd.MultiIndex.from_arrays([class1, class2], names=["class1", "class2"])

count_df = DataFrame(np.random.randint(1, 10, (4, 3)), index=m_index2)
print count_df
for row in count_df.iterrows():
    print row[0], row[1].values
