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
    print("开始时间：", start)
    sc = SparkContext(appName="test_hbase_engine")
    try:
        sqlContext = SQLContext(sparkContext=sc)
        java_import(sc._jvm, "pie.data.hbase.DyJa")
        dy_ja = sc._jvm.DyJa()
        result = dy_ja.getAllDataHb("z_spark_50w_three")

        # print(int(int(result.size()) / 4))

        first_rdd = sc.parallelize(result)
        # print(int(first_rdd.count() / 4))
        base_rdd = first_rdd.map(lambda x: x.split(":")).map(lambda x: (x[0], float(x[1])))
        result_mysql = base_rdd.combineByKey(
            lambda x: (x, 1),
            lambda x, y: (x[0] + y, x[1] + 1),
            lambda x, y: (x[0] + y[0], x[1] + y[1])
        ).map(lambda x: (x[0], float(x[1][0]) / float(x[1][1]))).collect()
        # for x in result_mysql:
        #     print(x)
        # ---------------------------- pyspark -------------------------------------
        import pymysql

        conn = pymysql.connect(host='192.168.0.179', port=3306, user='root', passwd='root', db='zn')
        cursor = conn.cursor()
        insert_sql = "INSERT INTO hbase_test04(qualifier,value) VALUES(%s,%s)"
        cursor.executemany(insert_sql, result_mysql)
        # 提交
        conn.commit()
        # 关闭游标和连接
        cursor.close()
        conn.close()

        end = datetime.datetime.now()
        print("当前时间：", end)
        print('总运行时间', end - start)
        sc.stop()
    except Exception as e:
        print(e)
        sc.stop()
