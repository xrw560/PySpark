#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:TF_IDF_demo.py
@time:2018/8/7 19:45
@desc:
"""
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("logistic_regression").getOrCreate()

"""创建一个DataFrame,每个句子代表一个文档"""
sentenceData = spark.createDataFrame([
    (0, "I heard about Spark and I love Spark"),
    (0, "I wish Java could use case classes"),
    (1, "Logistic regression models are neat")]) \
    .toDF("label", "sentence")
"""用tokenizer对句子进行分词"""
tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
wordsData = tokenizer.transform(sentenceData)
# wordsData.show()

"""使用HashingTF的transform方法将句子哈希成特征向量"""
hashing_tf = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=200)
featured_data = hashing_tf.transform(wordsData)  # DataFrame
featured_data.show(truncate=False)
"""分词序列被变换成一个稀疏特征向量，其中每个单词都被散列成了一个不同的索引值，特征向量在某一维度上的值即该词汇在文档中出现的次数"""

"""最后，使用IDF对单纯的词频特征进行修正，使其更能体现不同词汇对文本的区别能力，
IDF是一个Estimator,调用fit()方法并将词频向量传入，即产生一个IDFModel.
IDF会减少那些在语料库中出现频次较高的词的权重"""
idf = IDF(inputCol="rawFeatures", outputCol="features")
idfModel = idf.fit(featured_data)
"""IDFModel是一个Transformer，调用它的transform方法，即可得到每一个单词对应的TF-IDF度量值"""
rescaleData = idfModel.transform(featured_data)
rescaleData.select("label", "features").show(truncate=False)

spark.stop()
