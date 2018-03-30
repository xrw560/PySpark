# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:.py
@time:2018/3/30 17:40
"""
from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[2]").setAppName("transform")
    sc = SparkContext(conf=conf)
    sc.setLogLevel('WARN')

    # 创建RDD
    initRDD = sc.parallelize([3, 1, 2, 5, 5])
    print(initRDD.collect())
    stringRDD = sc.parallelize(['Apple', 'Orange', 'Banana', 'Grape', 'Apple'])
    print(stringRDD.collect())

    # filter数字运算
    print(' x < 3 ', initRDD.filter(lambda x: x < 3).collect())
    print(' x == 3 ', initRDD.filter(lambda x: x == 3).collect())
    print(' 1 < x and x > 5 ', initRDD.filter(lambda x: 1 < x and x < 5).collect())
    print(' x >= 5 or x < 3 ', initRDD.filter(lambda x: x >= 5 or x < 3).collect())

    # filter字符串运算
    print(stringRDD.filter(lambda x: 'ra' in x).collect())

    # distinct 运算
    print(initRDD.distinct().collect())
    print(stringRDD.distinct().collect())

    # randomSplit运算
    sRDD = initRDD.randomSplit([0.4, 0.6])
    print(sRDD[0].collect())
    print(sRDD[1].collect())

    # groupBy运算
    gRDD = initRDD.groupBy(lambda x: 'even' if (x % 2 == 0) else 'odd').collect()
    print(gRDD)
    print(gRDD[0][0], sorted(gRDD[0][1]))
    print(gRDD[1][0], sorted(gRDD[1][1]))
