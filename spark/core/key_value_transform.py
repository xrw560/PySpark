# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:key_value_transform.py
@time:2018/4/2 9:24
@description:
"""
from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[2]").setAppName("multi_rdd_transform")
    sc = SparkContext(conf=conf)
    sc.setLogLevel('WARN')

    kvRDD1 = sc.parallelize([(3, 4), (3, 6), (5, 6), (1, 2)])

    # 列出全部key值
    print(kvRDD1.keys().collect())

    # 列出全部values值
    print(kvRDD1.values().collect())

    # 使用filter筛选key运算
    # 使用filter筛选出key<5
    print(kvRDD1.filter(lambda keyValues: keyValues[0] < 5).collect())
    # 使用filter筛选出value<5
    print(kvRDD1.filter(lambda keyValue: keyValue[1] < 5).collect())

    # mapValues运算
    # 将Value的每一个值进行平方运算
    print(kvRDD1.mapValues(lambda x: x * x).collect())

    # sortByKey从小到大按照key排序
    print(kvRDD1.sortByKey(ascending=True).collect())
    print(kvRDD1.sortByKey().collect())
    # sortByKey 按照key值从大到小排序
    print(kvRDD1.sortByKey(ascending=False).collect())

    # reduceByKey
