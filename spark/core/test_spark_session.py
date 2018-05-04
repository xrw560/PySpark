#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:test_spark_session.py
@time:2018/5/2 9:21
spark-submit --master spark://master:7077 --num-executors 3 --executor-memory 8G --jars /usr/local/hbase/lib/hive-hbase-handler-2.3.3.jar ~/pythonCode/zn/spark/core/test_spark_session.py
"""
from pyspark.sql import SparkSession
import datetime

if __name__ == '__main__':
    start = datetime.datetime.now()
    spark = (SparkSession
             .builder
             .appName("test_spark_session")
             .enableHiveSupport()
             .getOrCreate())
    sc = spark.sparkContext
    print(sc.master)
    # # =======================MySQL配置===============================
    # url = "jdbc:mysql://192.168.0.190:3306/spark_test"
    # mysql_table = "test01"
    # mysql_properties = {"user": "root", "password": "root"}
    # # ===============================================================

    my_df = spark.sql(
        "SELECT cast(`A1` AS FLOAT) AS A1,"
        "cast(`A2` AS FLOAT) AS A2,"
        "cast(`A3` AS FLOAT) AS A3,"
        "cast(`A4` AS FLOAT) AS A4,"
        "cast(`A5` AS FLOAT) AS A5,"
        "cast(`A6` AS FLOAT) AS A6,"
        "cast(`A7` AS FLOAT) AS A7,"
        "cast(`A8` AS FLOAT) AS A8,"
        "cast(`A9` AS FLOAT) AS A9,"
        "cast(`A10` AS FLOAT) AS A10,"
        "cast(`A11` AS FLOAT) AS A11,"
        "cast(`A12` AS FLOAT) AS A12,"
        "cast(`A13` AS FLOAT) AS A13,"
        "cast(`A14` AS FLOAT) AS A14"
        " FROM zn.hbase_satellite_state_1000w")
    # my_df = spark.sql(
    #     "SELECT cast(`data01` AS FLOAT) AS data01,"
    #     "cast(`data02` AS FLOAT) AS data02,"
    #     "cast(`data03` AS FLOAT) AS data03,"
    #     "cast(`data04` AS FLOAT) AS data04 FROM zn.z_spark_5000w_three")

    # my_df = spark.sql("SELECT * FROM zn.z_spark_100w_three")
    # my_df = spark.sql("SELECT count(*) FROM zn.z_spark_test")
    # my_df = my_df.filter("data01 is not null").cache()
    # my_df = spark.sql("SELECT (data01) FROM zn.hive_5000w ")
    # my_df = spark.sql("SELECT * FROM zn.z_spark_test ")
    # my_df = spark.sql("SELECT * FROM zn.z_spark_5000w_three order by key limit 1")
    # my_df = spark.sql("SELECT * FROM zn.z_spark_5000w_three ORDER BY `KEY` LIMIT 1 ")
    # my_df = spark.sql("SELECT * FROM zn.z_spark_test")
    # my_df.describe(["data01"]).show
    # my_df.describe(["data01", "data02", "data03", "data04"]) \
    #     .write.jdbc(url, mysql_table, 'append', mysql_properties)
    # my_df.show()
    my_df.groupBy().avg("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13", "A14").show()
    end = datetime.datetime.now()
    print(end - start)

