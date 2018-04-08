#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:.py
@time:2018/4/8 9:52
"""

import happybase
from pyspark import SparkConf, SparkContext
import datetime

# from Process import Test

if __name__ == '__main__':
    start = datetime.datetime.now()
    # columns = "test:phj"
    # appName = "test004hn"
    # master = "192.168.0.190"
    # table = "runisys"
    # test = Test(appName,columns,master,table)
    # test.scriptJob()

    appName = "MySpark"
    master = "192.168.0.190"
    table = "z_spark_500w_one"
    conf = SparkConf()
    conf.setAppName(appName)
    sc = SparkContext(conf=conf)

    try:
        connection = happybase.Connection(master)
        table = connection.table(table)
        # rows = table.scan(limit=5000000)
        rows = table.scan(limit=500000)
        print("row:", rows)
        testRdd = sc.parallelize(rows)
        print(testRdd.count())

        print(testRdd.take(20))

        end = datetime.datetime.now()
        print("time: ", end - start)
        sc.stop()
    except Exception as e:
        print(e)
        end = datetime.datetime.now()
        print("time: ", end - start)
        sc.stop()
