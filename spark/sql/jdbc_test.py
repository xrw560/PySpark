#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:jdbc_test.py
@time:2018/7/30 16:34
@desc:
"""
from pyspark import SparkConf, SparkContext
import os
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("jdbc_test") \
    .getOrCreate()
url = "jdbc:mysql://192.168.2.179:3306/bigdata_test"
table = "(select evaluate_time_length from script_metadata) t"  # 注意括号和表别名，必须得有，这里可以过滤数据
properties = {
    "user": "root",
    "password": "root",
    "driver": "com.mysql.jdbc.Driver"
}

df = spark.read.jdbc(url, table, properties=properties)
print(df.schema)
df.show()
