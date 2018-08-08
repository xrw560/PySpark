#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:demo1.py
@time:2018/8/7 19:07
@desc:
"""

from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import HashingTF, Tokenizer

spark = SparkSession.builder.appName("logistic_regression").getOrCreate()

"""构建训练数据集"""
# Prepare training documents from a list of (id,text,label) tuples
training = spark.createDataFrame([
    (0, "a b c d e spark", 1.0),
    (1, "b d", 0.0),
    (2, "spark f g h", 1.0),
    (3, "hadoop mapreduce", 0.0)
], ["id", "text", "label"])

""" 定义Pipeline中的各个工作流阶段PipelineStage,包括转换器和评估器"""
tokenizer = Tokenizer(inputCol='text', outputCol='words')
hashing_tf = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol='features')
lr = LogisticRegression(maxIter=10, regParam=0.001)

pipeline = Pipeline(stages=[tokenizer, hashing_tf, lr])

model = pipeline.fit(training)

"""构建测试数据"""
test = spark.createDataFrame([
    (4, "spark i j k"),
    (5, "l m n"),
    (6, "spark hadoop spark"),
    (7, "apache hadoop")
], ["id", "text"])
prediction = model.transform(test)
selected = prediction.select("id", "text", "probability", "prediction")
for row in selected.collect():
    rid, text, prob, prediction = row
    print("(%d,%s) --> prob=%s, prediction=%f" % (rid, text, str(prob), prediction))

spark.stop()
