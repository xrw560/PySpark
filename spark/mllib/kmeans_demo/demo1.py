#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:demo1.py
@time:2018/8/9 8:48
@desc:

KMeans是一个迭代求解的聚类算法，其属于划分(Partitioning)型的聚类方法，即首先创建K个划分，
然后迭代地将样本从一个划分转移到另一个划分来改善最终聚类的质量。

ML包下的KMeans方法位于org.apache.spark.ml.clustering包下，其过程大致如下：
1. 根据给定的k值，选取k个样本点作为初始划分中心
2. 计算所有样本点到每一个划分中心的距离，并将所有样本点划分到距离最近的划分中心；
3. 计算每个划分中样本点的平均值，将其作为新的样本中心。

循环进行2~3步直至达到最大迭代次数，或划分中心的变化小于某一预定义阈值


"""

from pyspark.sql import Row, SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.linalg import Vectors


def f(x):
    rel = {}
    rel['features'] = Vectors.dense(float(x[1]), float(x[2]), float(x[3]), float(x[4]))
    rel['label'] = str(x[5]).strip("\"")
    return rel


spark = SparkSession.builder.appName("logistic_regression").getOrCreate()

df = spark.sparkContext.textFile("iris.txt").map(lambda line: line.split(",")).map(lambda p: Row(**f(p))).toDF()

"""创建Estimator并调用其fit()方法来生成相应的Transformer对象，
很显然，在这里KMeans类是Estimator，而用于保存训练后模型的KMeansModel类则属于Transformer"""
kmeans_model = KMeans().setK(3).setFeaturesCol("features").setPredictionCol("prediction").fit(df)

results = kmeans_model.transform(df).collect()
for item in results:
    print(str(item[0]) + " is predicted as cluster " + str(item[1]))

"""有可以通过KMeansModel类自带的clusterCenter属性获取到模型的所有聚类中心情况"""
results2 = kmeans_model.clusterCenters()
for item in results2:
    print(item)
"""与MLLib下的实现相同，KMeansModel类也提供了计算集合内误差平方和(Within Set Sum of Squared Error, WSSSE)
的方法来度量聚类的有效性，在真实K值未知的情况下，该值的变化可以作为选取合适K值的一个重要参考"""
print(kmeans_model.computeCost(df))
