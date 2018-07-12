#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:test_vector.py
@time:2018/7/11 16:38
@desc:
"""
from pyspark.mllib.linalg import *
from pyspark.mllib.regression import *

v = Vectors.dense(1.0, 2.0)
lp = LabeledPoint(0.0, v)
print(lp.label)

