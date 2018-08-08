#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:IndexToString.py
@time:2018/8/7 21:09
@desc:
与StringIndexer相对应，IndexToString的作用是把标签索引的一列重新映射回原有的字符型标签。
其主要使用场景一般都是和StringIndexer配合，先用StringIndexer将标签转化成标签索引，进行模型训练，
然后在预测标签的时候再把标签索引转化为原有的字符标签。当然，你也可以另外定义其他的标签

"""

from pyspark.ml.feature import StringIndexer, IndexToString
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
indexed.show()

converter = IndexToString(inputCol="categoryIndex", outputCol="originalCategory")
converted = converter.transform(indexed)
converted.select("id", "categoryIndex", "originalCategory").show()

spark.stop()
