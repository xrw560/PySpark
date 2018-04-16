#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:happy_base_read.py
@time:2018/4/8 9:52
"""

import happybase
from pyspark import SparkConf, SparkContext
import datetime

if __name__ == '__main__':
    start = datetime.datetime.now()
    print("开始时间：", start)
    appName = "HappyBase"
    master = "192.168.0.190"
    table = "z_spark_500w_three"
    conf = SparkConf()
    conf.setAppName(appName)
    sc = SparkContext(conf=conf)

    try:
        connection = happybase.Connection(master)
        table = connection.table(table)
        # rows = table.scan(limit=5000000)
        rows = table.scan(limit=10000000)
        testRdd = sc.parallelize(rows)

        # print("数据量：", str(testRdd.count()))

        # # -------------------------计算平均值---------------------------------
        values = testRdd.values().cache()
        col = bytes("info:data01".encode("utf-8"))
        serilizeRdd = values.map(lambda value: float(value.get(col).decode()))
        data01_mean_value = serilizeRdd.mean()

        col = bytes("info:data02".encode("utf-8"))
        serilizeRdd = values.map(lambda value: float(value.get(col).decode()))
        data02_mean_value = serilizeRdd.mean()

        col = bytes("info:data03".encode("utf-8"))
        serilizeRdd = values.map(lambda value: float(value.get(col).decode()))
        data03_mean_value = serilizeRdd.mean()

        col = bytes("info:data04".encode("utf-8"))
        serilizeRdd = values.map(lambda value: float(value.get(col).decode()))
        data04_mean_value = serilizeRdd.mean()

        print("data01_mean_value:", data01_mean_value)
        print("data02_mean_value:", data02_mean_value)
        print("data03_mean_value:", data03_mean_value)
        print("data04_mean_value", data04_mean_value)

        # # # ---------------------------- pyspark -------------------------------------
        # import pymysql
        #
        # conn = pymysql.connect(host='192.168.0.179', port=3306, user='root', passwd='root', db='zn')
        # cursor = conn.cursor()
        # insert_sql = "INSERT INTO hbase_test04(qualifier,value) VALUES(%s,%s)"
        # mean_values = []
        # mean_values.append(('data01', data01_mean_value))
        # mean_values.append(('data02', data02_mean_value))
        # mean_values.append(('data03', data03_mean_value))
        # mean_values.append(('data04', data04_mean_value))
        # cursor.executemany(insert_sql, mean_values)
        # # 提交
        # conn.commit()
        # # 关闭游标和连接
        # cursor.close()
        # conn.close()

        end = datetime.datetime.now()
        print("结束时间: ", end)
        print("运行时间: ", end - start)
        sc.stop()
    except Exception as e:
        print(e)
        end = datetime.datetime.now()
        print("结束时间: ", end)
        print("运行时间: ", end - start)
        sc.stop()
