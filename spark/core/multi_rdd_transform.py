# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:multi_rdd_transform.py
@time:2018/3/30 18:08
@description:
"""
from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[2]").setAppName("multi_rdd_transform")
    sc = SparkContext(conf=conf)
    sc.setLogLevel('WARN')

    # 创建3个范例RDD
    intRDD1 = sc.parallelize([3, 1, 2, 5, 5])
    intRDD2 = sc.parallelize([5, 6])
    intRDD3 = sc.parallelize([2, 7])

    # union并集运算
    print(intRDD1.union(intRDD2).union(intRDD3).collect())

    # intersection并集运算
    print(intRDD1.intersection(intRDD2).collect())

    # subtract差集运算
    print(intRDD1.subtract(intRDD2).collect())

    # cartesian笛卡尔乘积运算
    print(intRDD1.cartesian(intRDD2).collect())
