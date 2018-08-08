#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:Word2Vec_demo.py
@time:2018/8/7 20:25
@desc:

Word2Vec是一种著名的词嵌入(Word Embedding)方法，
它可以计算每个单词在其给定语料库环境下的分布式词向量(Distributed Representation,亦直接被称为词向量)。
词向量表示可以在一定程度上刻画每个单词的语义。

如果词的语义相近，它们的词向量在向量空间中也相互接近，这使得词语的向量化建模更加精确，可以改善现有方法并提高鲁棒性。
词向量已被证明在许多自然语言处理问题，如机器翻译，标注问题，实体识别等问题中具有非常重要的作用。

Word2Vec是一个Estimator，它采用一些列代表文档的词语来训练word2vecMode。
该模型将每个词语映射到一个固定大小的向量。
word2vecModel使用文档中每个词语的平均数来将文档抓换为向量，
然后这个向量可以作为预测的特征来计算文档相似度计算等等。

首先用一组文档，其中一个词语序列代表一个文档。
对于每一个文档，我们将其转换为一个特征向量。此特征向量可以被传递到一个学习算法。
"""

from pyspark.ml.feature import Word2Vec
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("logistic_regression").getOrCreate()

"""创建三个词语序列，每个代表一个文档"""
documentDF = spark.createDataFrame([
    ("Hi I heard about Spark".split(" "),),
    ("I wish Java could use case classes".split(" "),),
    ("Logistic regression models are neat".split(" "),)
], ["text"])

word2Vec = Word2Vec(vectorSize=3, minCount=0, inputCol="text", outputCol="result")

model = word2Vec.fit(documentDF)

"""利用Word2VecModel把文档转变成特征向量"""
result = model.transform(documentDF)

for row in result.collect():
    text, vector = row
    print("Text: [%s] => \nVector: %s\n" % (",".join(text), str(vector)))
"""文档被转变成一个3维的特征向量"""
spark.stop()
