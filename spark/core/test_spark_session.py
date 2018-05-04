#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:test_spark_session.py
@time:2018/5/2 9:21
"""
from pyspark.sql import SparkSession
import datetime

if __name__ == '__main__':
    start = datetime.datetime.now()
    spark = (SparkSession
             .builder
             .appName("test_spark_session")
             .config("spark.jars", "/usr/local/hive/lib/hive-hbase-handler-1.2.2.jar")
             .enableHiveSupport()
             .getOrCreate())
    sc = spark.sparkContext
    print(sc.master)
    # # =======================MySQL配置===============================
    # url = "jdbc:mysql://192.168.0.190:3306/spark_test"
    # mysql_table = "test01"
    # mysql_properties = {"user": "root", "password": "root"}
    # # ===============================================================

    # my_df = spark.sql(
    #     "SELECT cast(`data01` AS FLOAT) AS data01,"
    #     "cast(`data02` AS FLOAT) AS data02,"
    #     "cast(`data03` AS FLOAT) AS data03,"
    #     "cast(`data04` AS FLOAT) AS data04 FROM zn.hive_5000w")
    # my_df = spark.sql(
    #     "SELECT cast(`data01` AS FLOAT) AS data01,"
    #     "cast(`data02` AS FLOAT) AS data02,"
    #     "cast(`data03` AS FLOAT) AS data03,"
    #     "cast(`data04` AS FLOAT) AS data04 FROM zn.z_spark_5000w_three")

    # my_df = spark.sql("SELECT * FROM zn.z_spark_100w_three")
    my_df = spark.sql("SELECT count(*) FROM zn.z_spark_test")
    # my_df = my_df.filter("data01 is not null").cache()
    # my_df = spark.sql("SELECT (data01) FROM zn.hive_5000w ")
    # my_df = spark.sql("SELECT * FROM zn.z_spark_test ")
    # my_df = spark.sql("SELECT * FROM zn.z_spark_5000w_three order by key limit 1")
    # my_df = spark.sql("SELECT * FROM zn.z_spark_5000w_three ORDER BY `KEY` LIMIT 1 ")
    # my_df = spark.sql("SELECT * FROM zn.z_spark_test")
    # my_df.describe(["data01"]).show
    # my_df.describe(["data01", "data02", "data03", "data04"]) \
    #     .write.jdbc(url, mysql_table, 'append', mysql_properties)
    my_df.show()
    # my_df.groupBy().avg("data01", "data02", "data03", "data04").show()
    end = datetime.datetime.now()
    print(end - start)
