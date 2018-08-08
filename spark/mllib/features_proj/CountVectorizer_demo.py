#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:CountVectorizer_demo.py
@time:2018/8/7 20:48
@desc:
CountVectorizer旨在通过计数来将一个文档转换为向量。
当不存在先验字典时，CounterVectorizer作为Estimator提取词汇进行训练，
并生成一个CountVectorizerModel用于存储相应的词向量空间。
该模型产生文档关于词汇的稀疏表示，其表示可以传递给其他算法，例如LDA。

在CountVectorizerModel的训练过程中，CountVectorizer将根据语料库中的词频排序从高到低进行选择，
词汇表的最大含量由vocabsize超参数来指定，超参数minDF，则指定词汇表中的词语至少要在多少个不同文档中出席那。

"""

from pyspark.ml.feature import CountVectorizer
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("logistic_regression").getOrCreate()

"""假设我们有如下的DataFrame，其包含id和word两列，可以看成一个包含两个文档的迷你语料库"""
df = spark.createDataFrame([
    (0, "a b c d".split(" ")),
    (1, "a b b c a d d".split(" "))
], ["id", "words"])

# fit a CountVectorizerModel from the corpus
# 通过CountVectorizer设定超参数，训练一个CountVectorizer
# 这里设定词汇表的最大量为3，设定词汇表中的词至少要在2个文档中出现过，以过滤那些偶然出现的词汇
cv = CountVectorizer(inputCol="words", outputCol="features", vocabSize=3, minDF=2.0)
model = cv.fit(df)

# 利用模型对DataFrame进行变换，可以得到文档的向量化表示
result = model.transform(df)
result.show(truncate=False)

spark.stop()
