#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:feature_selection_demo.py
@time:2018/8/8 19:30
@desc:
特征选择(Feature Selection)指的是在特征向量中选择出那些“优秀”的特征，组成新的、更“精简”的特征向量的过程。
它在高维数据分析中非常常用，可以剔除“冗余”和“无关”的特征，提升学习器的性能。

特征选择方法和分类方法一样，也主要分为有监督(Supervised)和无监督(Unsupervised)两种，
卡方选择器则是统计学上常用的一种有监督特征选择方法，
它通过对特征和真实标签之间进行卡方检验，来判断该特征和真实标签的关联程度，进而确定是否对其进行选择。
"""

from pyspark.ml.feature import ChiSqSelector
from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("logistic_regression").getOrCreate()

df = spark.createDataFrame([
    (7, Vectors.dense([0.0, 0.0, 18.0, 1.0]), 1.0),
    (8, Vectors.dense([0.0, 1.0, 12.0, 0.0]), 0.0),
    (9, Vectors.dense([1.0, 0.0, 15.0, 0.1]), 0.0),
], ["id", "features", "clicked"])

selector = ChiSqSelector(numTopFeatures=1, featuresCol="features", outputCol="selectedFeatures", labelCol="clicked")
result = selector.fit(df).transform(df)
result.show()

spark.stop()
