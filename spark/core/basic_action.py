# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:basic_action.py
@time:2018/4/2 9:19
@description:
"""
from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[2]").setAppName("multi_rdd_transform")
    sc = SparkContext(conf=conf)
    sc.setLogLevel('WARN')

    intRDD = sc.parallelize([3, 1, 2, 5, 5])

    # 统计
    print(intRDD.stats())

    # 最小
    print(intRDD.min())

    # 最大
    print(intRDD.max())

    # 标准差
    print(intRDD.stdev())

    # 计数
    print(intRDD.count())

    # 总和
    print(intRDD.sum())

    # 平均
    print(intRDD.mean())

