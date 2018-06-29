#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:diff.py
@time:2018/6/29 15:09
@desc:
"""

from pyspark import SparkConf, SparkContext
import numpy as np
import pandas as pd

if __name__ == '__main__':
    spark_conf = SparkConf().setAppName("word_count")
    sc = SparkContext(conf=spark_conf)
    sc.setLogLevel('WARN')

    # rdd = sc.parallelize([1, 2, 3, 4, 5], 2)
    # print(rdd.getNumPartitions())
    # print(rdd.glom().collect())


    # re_rdd = rdd.groupByKey().collectAsMap()
    # print(type(re_rdd))
    # for x, v in re_rdd.items():
    #     print(x, end='')
    #     print(np.diff(list(v)))

    rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 5), ("b", 1), ("a", 2), ("b", 1), ("a", 3), ("b", 1), ("a", 1)], 3)
    def diff_sort(x):
        l = list(x)
        l.sort()
        return np.diff(l)
    res_rdd = rdd.groupByKey().mapValues(lambda x: diff_sort(x)).collect()
    for x in res_rdd:
        print(x)
