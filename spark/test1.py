#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:test1.py
@time:2018/7/20 17:55
@desc:
"""

from pyspark.sql import SparkSession, Row
import os

os.environ['JAVA_HOME'] = 'D:\java\jdk'


def rdd_to_tuple(x):
    return [(x, 1), (x, 2), (x, 3)]


spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
sc = spark.sparkContext
rdd = sc.parallelize([(1, 2, 3), (1, 2, 3), (1, 2, 4), (4, 5, 6)])

res_rdd = rdd.aggregateByKey(
    (0, 0),
    lambda x, y: (x[0] + y[0], x[1] + y[1]),
    lambda x, y: (x[0] + y[0], x[1] + y[1])
)
for x in res_rdd.collect():
    print x

# rdd = sc.parallelize([1, 2, 3]).flatMap(lambda x: rdd_to_tuple(x))
# for x in rdd.collect():
# #     print(x[0])
# rdict = {1: "value1", 2: "value2", 3: "value3"}
# # bc_dict = sc.broadcast(rdict)
# # re = rdd.map(lambda x: bc_dict.value[x[0]]).collect()
# # for x in re:
# #     print(x)
# ddict = {(1, 1), (1, 2), (2, 3), (2, 1)}
# zip_value = zip(rdict, ddict)
# # for x in list(zip_value):
# #     print(x)
# print(sc.parallelize(ddict).groupByKey(lambda x: x).collect())
