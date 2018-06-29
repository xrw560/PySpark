#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:df_to_pandas_df.py
@time:2018/6/29 18:46
@desc:
"""

import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext

sc = SparkContext()
if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("testDataFrame") \
        .getOrCreate()

sentenceData = spark.createDataFrame([
    (0.0, "I like Spark"),
    (1.0, "Pandas is useful"),
    (2.0, "They are coded by Python ")
], ["label", "sentence"])

pandas_df = sentenceData.toPandas()

print(pandas_df)
