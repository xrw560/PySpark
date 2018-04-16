#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:API_Test.py
@time:2018/4/16 9:26
"""
from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('API_Test')
    sc = SparkContext(conf=conf)
    sc.setLogLevel('WARN')

    # # map
    # # sc = spark context, parallelize creates an RDD from the passed object
    # x = sc.parallelize([1, 2, 3])
    # y = x.map(lambda x: (x, x ** 2))
    #
    # # collect copies RDD elements to a list on the driver
    # print(x.collect())
    # print(y.collect())

    # # flatMap
    # x = sc.parallelize([1, 2, 3])
    # y = x.flatMap(lambda x: (x, 100 * x, x ** 2))
    # print(x.collect())
    # print(y.collect())

    # # mapPartitions
    # x = sc.parallelize([1, 2, 3], 2)
    # def f(iterator): yield sum(iterator)
    # y = x.mapPartitions(f)
    # # glom() flattens elements on the same partition
    # print(x.glom().collect())
    # print(y.glom().collect())

    # # mapPartitionsWithIndex
    # x = sc.parallelize([1,2,3],2)
    # def f(partitionIndex,iterator):yield (partitionIndex,sum(iterator))
    # y = x.mapPartitionsWithIndex(f)
    # # glom() flattens elements on the same partition
    # print(x.glom().collect())
    # print(y.glom().collect())

    # getNumPartitions
    # x = sc.parallelize([1, 2, 3], 2)
    # y = x.getNumPartitions()
    # print(x.glom().collect())
    # print(y)

    # # filter
    # x = sc.parallelize([1, 2, 3])
    # y = x.filter(lambda x: x % 2 == 1)  # filter out even elements
    # print(x.collect())
    # print(y.collect())

    # # distinct
    # x = sc.parallelize(['A', 'A', 'B'])
    # y = x.distinct()
    # print(x.collect())
    # print(y.collect())

    # # sample
    # x = sc.parallelize(range(7))
    # # call 'sample' 5 times
    # '''
    #     对RDD进行抽样，其中参数withReplacement为true时表示抽样之后还放回，可以被多次抽样，false表示不放回；
    #     fraction表示抽样比例；
    #     seed为随机数种子，比如当前时间戳
    # '''
    # ylist = [x.sample(withReplacement=False, fraction=0.5) for i in range(5)]
    # print('x= ' + str(x.collect()))
    # for cnt, y in zip(range(len(ylist)), ylist):
    #     print('sample:' + str(cnt) + ' y= ' + str(y.collect()))

    # takeSample:和sample用法相同，只不第二个参数换成了个数。返回也不是RDD，而是collect。
    # x = sc.parallelize(range(7))
    # # call  'sample' 5 times
    # ylist = [x.takeSample(withReplacement=False, num=3) for i in range(5)]
    # print('x= ' + str(x.collect()))
    # for cnt, y in zip(range(len(ylist)), ylist):
    #     print('sample:' + str(cnt) + ' y= ' + str(y))  # no collect on y

    # # union
    # x = sc.parallelize(['A', 'A', 'B'])
    # y = sc.parallelize(['D', 'C', 'A'])
    # z = x.union(y)
    # print(x.collect())
    # print(y.collect())
    # print(z.collect())

    # # intersection
    # x = sc.parallelize(['A','A','B'])
    # y = sc.parallelize(['A','C','D'])
    # z = x.intersection(y)
    # print(x.collect())
    # print(y.collect())
    # print(z.collect())

    # # sortByKey
    # x = sc.parallelize([('B', 1), ('A', 2), ('C', 3)])
    # y = x.sortByKey()
    # print(x.collect())
    # print(y.collect())

    # # sortBy: Return this RDD sorted by the given key function.
    # x = sc.parallelize(['Cat', 'Apple', 'Bat'])
    # def keyGen(val): return val[0]
    # y = x.sortBy(keyGen)
    # print(y.collect())

    # # glom
    # x = sc.parallelize(['C', 'B', 'A'], 2)
    # y = x.glom()
    # print(x.collect())
    # print(y.collect())

    # # cartesian: 两个RDD进行笛卡尔积合并
    # x = sc.parallelize(['A', 'B'])
    # y = sc.parallelize(['C', 'D'])
    # z = x.cartesian(y)
    # print(x.collect())
    # print(y.collect())
    # print(z.collect())

    # groupBy
    x = sc.parallelize([1, 2, 3])
    y = x.groupBy(lambda x: 'A' if (x % 2 == 1) else 'B')
    print(x.collect())
    # y is nested, this iterates through it
    print([(j[0], [i for i in j[1]]) for j in y.collect()])
