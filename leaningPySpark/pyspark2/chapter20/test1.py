#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:test1.py
@time:2018/7/12 17:55
@desc:
"""
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("test") \
    .getOrCreate()
row_df = (spark.read.format("csv")  # 指定为csv格式
          .option("header", "true")  # 指定第一行是字段名
          .option("delimiter", "\t")  # 指定字段的分隔符是tab键"\t"
          .load("../../../data/train.tsv"))  # 指定要加载的文件
print(row_df.count())
row_df.printSchema()
"""查看前10项数据"""
row_df.select('url', 'alchemy_category', 'alchemy_category_score', 'is_news', 'label').show(10)

"""编写DataFrames UDF用户自定义函数"""
from pyspark.sql.functions import udf


def replace_question(x):
    return ("0" if x == '?' else x)


replace_question = udf(replace_question)  # 将replace_quetion抓换为DataFrames UDF用户自定义函数

from pyspark.sql.functions import *
import pyspark.sql.types

df = row_df.select(['url', 'alchemy_category'] + [replace_question(column).cast('double').alias(column) for column in
                                                  row_df.columns[4:]])
df.printSchema()
