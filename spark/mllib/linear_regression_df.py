#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:linear_regression_df.py
@time:2018/6/12 9:49
"""
from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler

if __name__ == '__main__':
    spark = SparkSession \
        .builder \
        .appName("lr") \
        .getOrCreate()

    df = spark.createDataFrame([(3.0, 1.0),  ## y, x
                                (7.0, 3.0),
                                (5.0, 2.0)],
                               ["y", "x"])
    # 转换x列为Vector[]
    assembler = VectorAssembler(inputCols=["x"], outputCol="features")
    dfv = assembler.transform(df)
    print(len(dfv.rdd.take(1)[0]))
    dfv.show()
    lr = LinearRegression(labelCol='y', maxIter=50, regParam=0.01, solver="normal", fitIntercept=True)
    model = lr.fit(dfv)
    print("intercept: ", model.intercept)  # 偏置b
    print("---> ", model.coefficients)  # 各特征变量的系数a
    test0 = spark.createDataFrame([(4, Vectors.dense(4.0)),
                                   (5, Vectors.dense(5.0))], ["id", "features"])
    prediction = model.transform(test0)  # 预测
    prediction.show()
    selected = prediction.select("id", "features", "prediction")
    for row in selected.collect():
        print(row)
    # print(abs(model.transform(test0).head().prediction - (-1.0)) < 0.001)
