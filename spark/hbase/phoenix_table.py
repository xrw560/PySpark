#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:phoenix_table.py
@time:2018/4/8 13:35
"""
from pyspark import SQLContext,SparkContext
import datetime
if __name__ == '__main__':
    start = datetime.datetime.now()
    sc = SparkContext(appName="phoenix_table")
    sqlContext = SQLContext(sparkContext=sc)
    df = sqlContext.read \
        .format("org.apache.phoenix.spark") \
        .option("table", "\"z_spark_1w\"") \
        .option("zkUrl", "master:2181") \
        .load()
    print(df.count())
    sc.stop()

