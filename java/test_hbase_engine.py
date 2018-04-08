#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:.py
@time:2018/4/4 14:56
"""
from pyspark import SparkContext, SQLContext
from py4j.java_gateway import java_import
import datetime
import json

if __name__ == '__main__':
    start = datetime.datetime.now()
    sc = SparkContext(appName="test_hbase_engine")
    try:
        sqlContext = SQLContext(sparkContext=sc)
        java_import(sc._jvm, "pie.data.hbase.DyJa")
        dy_ja = sc._jvm.DyJa()
        result = dy_ja.getDataHb("z_spark_500w_one", 'info', 'data01')
        # result = dy_ja.getDataHb("z_spark_1w", 'info', 'data01')
        print('----> len: ', len(result))
        print(sc.parallelize(result).count())
        # result_json = json.loads(" ".join(result))
        # df = sqlContext.read.json(result_json)
        # print('---------> df.count() : ', df.count())

        # end = datetime.datetime.now()
        # print('-----getData------- time :', end - start)
        # sc.parallelize(result).saveAsTextFile('hdfs://master:9000/work/data/output06')

        end = datetime.datetime.now()
        print('-----application run time :', end - start)
        sc.stop()
    except Exception as e:
        print(e)
        end = datetime.datetime.now()
        print('-----application run time :', end - start)
        sc.stop()
    print("-------------finished-----------------------")
