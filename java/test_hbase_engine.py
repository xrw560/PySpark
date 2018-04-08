#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:.py
@time:2018/4/4 14:56
"""
from pyspark import SparkContext
from py4j.java_gateway import java_import

sc = SparkContext(appName="Py4jTesting")
java_import(sc._jvm, "pie.data.hbase.DyJa")
dy_ja = sc._jvm.DyJa()
helper = dy_ja.getDataHb('z_spark_500w_one')
result = helper.getAllData("z_spark_1w")
sc.parallelize(result).saveAsTextFile('hdfs://master:9000/work/data/output06')

