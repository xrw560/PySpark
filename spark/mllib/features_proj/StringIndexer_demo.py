#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:StringIndexer_demo.py
@time:2018/8/7 21:02
@desc:
StringIndexer转换器可以把一列类别型的特征（或标签）进行编码，使其数值化，索引的范围从0开始，
该过程可以使得相应的特征索引化，使得某些无法接受类别型特征的算法可以使用，并提高诸如决策树等机器学习算法的效率。

索引构建的顺序为标签的频率，优先编码频率较大的标签，所以出现频率最高的标签为0号。
如果输入的是数值型，我们会把它转化为字符型，然后对其进行编码。

"""
from pyspark.ml.feature import StringIndexer
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("logistic_regression").getOrCreate()

df = spark.createDataFrame([
    (0, "a"),
    (1, "b"),
    (2, "c"),
    (3, "a"),
    (4, "a"),
    (5, "c")
], ["id", "category"])

indexer = StringIndexer(inputCol="category", outputCol="categoryIndex")
model = indexer.fit(df)

indexed = model.transform(df)
indexed.show()

spark.stop()
