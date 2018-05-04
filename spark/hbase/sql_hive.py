#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:sql_hive.py
@time:2018/5/2 18:13
"""
from pyspark.sql import SparkSession
import datetime
from pyspark.sql import functions as F
import pymysql

if __name__ == '__main__':
    start = datetime.datetime.now()
    spark = SparkSession \
        .builder \
        .appName("sql_hive") \
        .enableHiveSupport() \
        .getOrCreate()
    my_df = spark.sql("SELECT  FROM zn.hive_5000w ORDER BY `key` DESC LIMIT 1")

    conn = pymysql.connect(host='192.168.0.179', port=3306, user='root', passwd='root', db='zn')
    cursor = conn.cursor()
    insert_sql = "INSERT INTO hbase_test03(qualifier,n_value,max_value,avg_value,sum_value,count_value) VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.executemany(insert_sql, result_mysql)
