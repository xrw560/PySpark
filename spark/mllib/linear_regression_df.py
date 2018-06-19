#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:linear_regression_df.py
@time:2018/6/12 9:49
"""
from pyspark.ml.linalg import Vectors
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.ml.regression import IsotonicRegression, LinearRegression

if __name__ == '__main__':
    spark = SparkSession.builder \
        .master("local") \
        .appName("lr") \
        .getOrCreate()
    df = spark.createDataFrame([(1.0, 2.0, Vectors.dense(1.0)),
                                (0.0, 2.0, Vectors.sparse(1, [], []))],
                               ["label", "weight", "features"])
    lr = LinearRegression(maxIter=5, regParam=0.0, solver="normal", weightCol="weight")
    model = lr.fit(df)
    print("---> ", model.coefficients)
    test0 = spark.createDataFrame([(Vectors.dense(-1.0),)], ["features"])
    print(abs(model.transform(test0).head().prediction - (-1.0)) < 0.001)
