# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:.py
@time:2018/3/30 17:40
"""
from pyspark import SparkConf, SparkContext


def cus_print(name):
    print("hello ", name)


if __name__ == '__main__':
    spark_conf = SparkConf().setAppName("word_count")
    sc = SparkContext(conf=spark_conf)
    sc.setLogLevel('WARN')

    base_rdd = sc.parallelize(["hello world", "hello python", "hello java", "python is good"])

    words = base_rdd.flatMap(lambda x: x.split(" "))
    pairs = words.map(lambda x: (x, 1))
    word_count = pairs.reduceByKey(lambda x, y: x + y)
    for x in word_count.collect():
        print(x)
    sc.stop()
