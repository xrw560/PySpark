#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:VectorIndexer_demo.py
@time:2018/8/8 9:03
@desc:
StringIndexer是针对单个类别特征进行转换，
倘若所有特征都已经被组织在一个向量中，又想对其中某些单个分量进行处理时，Spark ML提供了VectorIndexer类来解决向量数据集中的类别特征转换。

通过为其提供maxCategories超参数，它可以自动识别哪些特征是类别型的，并且将原始值转换为类别索引。
它基于不同特征值的数量的数量来识别哪些特征需要被类别化，那些取值可能性最对不超过maxCategories的特征需要会被认为是类别型的。

在下面的例子中，我们读入一个数据集，然后使用VectorIndexer训练出模型，来决定哪些特征需要被作为类别特征，将类别特征转换为索引，
这里设置maxCategories为10，即只有种类小的特征才被认为是类别型特征，否则被认为是连续型特征。
"""

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorIndexer

spark = SparkSession.builder.appName("logistic_regression").getOrCreate()

data = spark.read.format('libsvm').load('sample_libsvm_data.txt')
indexer = VectorIndexer(inputCol="features", outputCol="indexed", maxCategories=2)
indexed_model = indexer.fit(data)
categorical_features = indexed_model.categoryMaps
print(categorical_features)
indexed_data = indexed_model.transform(data)
indexed_data.show(truncate=False)
spark.stop()
