#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:OneHotEncoder_demo.py
@time:2018/8/7 21:25
@desc:
"""

from pyspark.ml.feature import StringIndexer, OneHotEncoder
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("logistic_regression").getOrCreate()

df = spark.createDataFrame([
    (0, "ab"),
    (1, "bb"),
    (2, "cb"),
    (3, "aa"),
    (4, "aa"),
    (5, "ca")
], ["id", "category"])

indexer = StringIndexer(inputCol="category", outputCol="categoryIndex")
model = indexer.fit(df)
indexed = model.transform(df)

encoder = OneHotEncoder(inputCol="categoryIndex", outputCol="categoryVec", dropLast=False)
encoded = encoder.transform(indexed)
encoded.show()

spark.stop()