#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:pd_rolling.py
@time:2018/6/29 19:12
@desc:
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
df.rolling()
print(df)
