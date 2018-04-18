#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:API_Test.py
@time:2018/4/16 9:26
"""
from __future__ import print_function
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

    # # groupBy
    # x = sc.parallelize([1, 2, 3])
    # y = x.groupBy(lambda x: 'A' if (x % 2 == 1) else 'B')
    # print(x.collect())
    # # y is nested, this iterates through it
    # print([(j[0], [i for i in j[1]]) for j in y.collect()])

    # # pipe
    # x = sc.parallelize(['A', 'Ba', 'C', 'AD'])
    # y = x.pipe('grep -i "A"')  # calls out to grep, may fail under window
    # print(x.collect())
    # print(y.collect())

    # # foreach
    # x = sc.parallelize([1, 2, 3])
    # def f(el):
    #     """side effect: append the current RDD elements to a file"""
    #     f1 = open('./foreachExample.txt', 'a+')
    #     # 将print结果输出到文件中
    #     print(el, file=f1)
    # # first clear the file contents
    # open('./foreachExample.txt', 'w').close()
    # y = x.foreach(f)  # writes into foreachExample.txt
    # print(x.collect())
    # print(y)  # foreach returns 'None'
    # # print the contents of foreachExample.txt
    # with open('./foreachExample.txt', 'r') as foreachExample:
    #     print(foreachExample.read())

    # # foreachPartition
    # x = sc.parallelize([1, 2, 3], 5)
    # def f(partition):
    #     """side effect: append the current RDD partition contents to a file"""
    #     f1 = open('./foreachPartitionExample.txt','a+')
    #     print([el for el in partition], file=f1)
    # # first clear the  file contents
    # open('./foreachPartitionExample.txt','w').close()
    # y = x.foreachPartition(f) # writes into foreachPartitionExample.txt
    # print(x.glom().collect())
    # print(y) # foreachPartition returns 'None'
    # # print the contents of foreachPartitionExample.txt
    # with open('./foreachPartitionExample.txt','r') as foreachPartitionExample:
    #     print(foreachPartitionExample.read())

    # # collect
    # x = sc.parallelize([1, 2, 3])
    # y = x.collect()
    # print(x)  # distributed
    # print(y)  # not distributed

    # # reduce
    # """
    #     对RDD成员使用func进行reduce操作，func接受两个参数，合并之后只返回一个值。
    #     reduce操作的返回结果只有一个值。需要注意的是，func会并发执行
    # """
    # x = sc.parallelize([1, 2, 3])
    # y = x.reduce(lambda obj, accumulated: obj + accumulated)  # computes a cumulative sum
    # print(x.collect())
    # print(y)

    # # fold
    # x = sc.parallelize([1, 2, 3])
    # neutral_zero_value = 0  # 0 for sum, 1 for multiplication
    # y = x.fold(neutral_zero_value, lambda obj, accumulated: accumulated + obj)  # computes cumulative sum
    # print(x.collect())
    # print(y)

    # # aggregate
    # x = sc.parallelize([2, 3, 4])
    # neutral_zero_value = (0, 1) # sum: x+0 = x, product: 1*x = x
    # seqOp = (lambda aggregated, el: (aggregated[0] + el, aggregated[1] * el))
    # combOp = (lambda aggregated, el: (aggregated[0] + el[0], aggregated[1] * el[1]))
    # y = x.aggregate(neutral_zero_value, seqOp, combOp)  # computes(cumulative sum, cumulative product)
    # print(x.collect())
    # print(y)

    # # max
    # x = sc.parallelize([1, 3, 2])
    # y = x.max()
    # print(x.collect())
    # print(y)

    # # min
    # x = sc.parallelize([1, 3, 2])
    # y = x.min()
    # print(x.collect())
    # print(y)

    # # sum
    # x = sc.parallelize([1, 3, 2])
    # y = x.sum()
    # print(x.collect())
    # print(y)

    # # count
    # x = sc.parallelize([1, 3, 2])
    # y = x.count()
    # print(x.collect())
    # print(y)

    # # histogram(example #1): bucket是一个数字
    # x = sc.parallelize([1, 3, 1, 2, 3])
    # y = x.histogram(buckets=2)
    # print(x.collect())
    # print(y)  # [1, 2, 3]是桶，表示[1,2),[2,3]; [2,3]是各个桶分布的频数

    # # histogram(example #2): bucket是一个列表
    # x = sc.parallelize([1, 3, 1, 2, 3])
    # y = x.histogram([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5])
    # print(x.collect())
    # print(y)

    # # mean
    # x = sc.parallelize([1, 3, 2])
    # y = x.mean()
    # print(x.collect())
    # print(y)

    # # variance 方差
    # x = sc.parallelize([1, 3, 2])
    # y = x.variance()  # divides by N
    # print(x.collect())
    # print(y)

    # # stdev 标准方差
    # x = sc.parallelize([1, 3, 2])
    # y = x.stdev()  # divides by N
    # print(x.collect())
    # print(y)

    # # sampleStdev
    # x = sc.parallelize([1, 3, 2])
    # y = x.sampleStdev()  # divides by N-1
    # print(x.collect())
    # print(y)

    # # sampleVariance
    # x = sc.parallelize([1, 3, 2])
    # y = x.sampleVariance()  # divides by N-1
    # print(x.collect())
    # print(y)

    # # countByValue
    # x = sc.parallelize([1, 3, 1, 2, 3])
    # y = x.countByValue()
    # print(x.collect())
    # print(y)

    # # top
    # x = sc.parallelize([1, 3, 1, 2, 3])
    # y = x.top(num=3)
    # print(x.collect())
    # print(y)

    # # takeOrdered : takeOrdered和top类似，只不过以和top相反的顺序返回元素。
    # x = sc.parallelize([1, 3, 1, 2, 3])
    # y = x.takeOrdered(num=3)
    # print(x.collect())
    # print(y)

    # # take: take用于获取RDD中从0到num-1下标的元素，不排序。
    # x = sc.parallelize([1, 3, 1, 2, 3])
    # y = x.take(num=3)
    # print(x.collect())
    # print(y)

    # # first
    # x = sc.parallelize([1, 3, 1, 2, 3])
    # y = x.first()
    # print(x.collect())
    # print(y)

    # # collectAsMap
    # x = sc.parallelize([('C', 3), ('A', 1), ('B', 2)])
    # y = x.collectAsMap()
    # print(x.collect())
    # print(y)
    # print(type(y))

    # # keys
    # x = sc.parallelize([('C', 3), ('A', 1), ('B', 2)])
    # y = x.keys()
    # print(x.collect())
    # print(y.collect())

    # # values
    # x = sc.parallelize([('C', 3), ('A', 1), ('B', 2)])
    # y = x.values()
    # print(x.collect())
    # print(y.collect())

    # # reduceByKey
    """
        该函数用于将RDD[K,V]中每个K对应的V值根据映射函数来运算。
        参数numPartitions用于指定分区数；
        参数partitioner用于指定分区函数；
    """
    def sumFunc(accum,n):
        print("===============")
        print(str(accum)+":"+str(n))
        return accum+n
    x = sc.parallelize([('B', 1), ('B', 2), ('A', 3), ('A', 4), ('A', 5)])
    # y = x.reduceByKey(lambda agg, obj: agg + obj)
    y = x.reduceByKey(sumFunc)
    print(x.collect())
    print(y.collect())

    # reduceByKeyLocally
    """
        该函数将RDD[K,V]中每个K对应的V值根据映射函数来运算，运算结果映射到一个Map[K,V]中，而不是RDD[K,V]。
    """
    # x = sc.parallelize([('B', 1), ('B', 2), ('A', 3), ('A', 4), ('A', 5)])
    # y = x.reduceByKeyLocally(lambda agg, obj: agg + obj)
    # print(x.collect())
    # print(y)

    # # countByKey
    # x = sc.parallelize([('B', 1), ('B', 2), ('A', 3), ('A', 4), ('A', 5)])
    # y = x.countByKey()
    # print(x.collect())
    # print(y)

    # # join
    # x = sc.parallelize([('C', 4), ('B', 3), ('A', 2), ('A', 1)])
    # y = sc.parallelize([('A', 8), ('B', 7), ('A', 6), ('D', 5)])
    # z = x.join(y)
    # print(x.collect())
    # print(y.collect())
    # print(z.collect())

    # # leftOuterJoin
    # x = sc.parallelize([('C', 4), ('B', 3), ('A', 2), ('A', 1)])
    # y = sc.parallelize([('A', 8), ('B', 7), ('A', 6), ('D', 5)])
    # z = x.leftOuterJoin(y)
    # print(x.collect())
    # print(y.collect())
    # print(z.collect())

    # # rightOuterJoin
    # x = sc.parallelize([('C', 4), ('B', 3), ('A', 2), ('A', 1)])
    # y = sc.parallelize([('A', 8), ('B', 7), ('A', 6), ('D', 5)])
    # z = x.rightOuterJoin(y)
    # print(x.collect())
    # print(y.collect())
    # print(z.collect())

    # # partitionBy
    # x = sc.parallelize([(0, 1), (1, 2), (2, 3)], 2)
    # y = x.partitionBy(numPartitions=3, partitionFunc=lambda x: x)  # only key is passed to partitionFunc
    # print(x.glom().collect())
    # print(y.glom().collect())

    # # combineByKey
    # x = sc.parallelize([('B', 1), ('B', 2), ('A', 3), ('A', 4), ('A', 5)])
    # createCombiner = (lambda el: [(el, el ** 2)])
    # mergeVal = (lambda aggregated, el: aggregated + [(el, el ** 2)])  # append to aggregated
    # mergeComb = (lambda agg1, agg2: agg1 + agg2)  # append agg1 with agg2
    # y = x.combineByKey(createCombiner, mergeVal, mergeComb)
    # print(x.collect())
    # print(y.collect())

    # # aggregateByKey
    # x = sc.parallelize([('B', 1), ('B', 2), ('A', 3), ('A', 4), ('A', 5)])
    # zeroValue = []  # empty list is 'zero value' for append operation
    # mergeVal = (lambda aggregated, el: aggregated + [(el, (el ** 2))])
    # mergeComb = (lambda agg1, agg2: agg1 + agg2)
    # y = x.aggregateByKey(zeroValue, mergeVal, mergeComb)
    # print(x.collect())
    # print(y.collect())

    # # foldByKey
    # x = sc.parallelize([('B', 1), ('B', 2), ('A', 3), ('A', 4), ('A', 5)])
    # zeroValue = 1  # one is 'zero value' for multiplication
    # y = x.foldByKey(zeroValue, lambda agg, x: agg * x)  # computes cumulative product within each key
    # print(x.collect())
    # print(y.collect())

    # # groupByKey
    # x = sc.parallelize([('B', 5), ('B', 4), ('A', 3), ('A', 2), ('A', 1)])
    # y = x.groupByKey()
    # print(x.collect())
    # print([(j[0], [i for i in j[1]]) for j in y.collect()])

    # flatMapValues
    # x = sc.parallelize([('A', (1, 2, 3)), ('B', (4, 5))])
    # y = x.flatMapValues(lambda x: [i ** 2 for i in x])  # function is applied to entire value, then result is flattened
    # print(x.collect())
    # print(y.collect())

    # # mapValues
    # x = sc.parallelize([('A', (1, 2, 3)), ('B', (4, 5))])
    # y = x.mapValues(lambda x: [i ** 2 for i in x])  # functions is applied to entire value
    # print(x.collect())
    # print(y.collect())

    # # groupWith
    # x = sc.parallelize([('C', 4), ('B', (3, 3)), ('A', 2), ('A', (1, 1))])
    # y = sc.parallelize([('B', (7, 7)), ('A', 6), ('D', (5, 5))])
    # z = sc.parallelize([('D', 9), ('B', (8, 8))])
    # a = x.groupWith(y, z)
    # print(x.collect())
    # print(y.collect())
    # print(z.collect())
    # print("Result: ")
    # for key, val in list(a.collect()):
    #     print(key, [list(i) for i in val])

    # # cogroup
    # x = sc.parallelize([('C', 4), ('B', (3, 3)), ('A', 2), ('A', (1, 1))])
    # y = sc.parallelize([('B', (7, 7)), ('A', 6), ('D', (5, 5))])
    # z = x.cogroup(y)
    # print(x.collect())
    # print(y.collect())
    # for key, val in list(z.collect()):
    #     print(key, [list(i) for i in val])

    # # sampleByKey
    # x = sc.parallelize([('A', 1), ('B', 2), ('C', 3), ('B', 4), ('A', 5)])
    # y = x.sampleByKey(withReplacement=False, fractions={'A': 0.5, 'B': 1, 'C': 0.2})
    # print(x.collect())
    # print(y.collect())

    # # subtractByKey
    # x = sc.parallelize([('C', 1), ('B', 2), ('A', 3), ('A', 4)])
    # y = sc.parallelize([('A', 5), ('D', 6), ('A', 7), ('D', 8)])
    # z = x.subtractByKey(y)
    # print(x.collect())
    # print(y.collect())
    # print(z.collect())

    # # subtract
    # x = sc.parallelize([('C', 4), ('B', 3), ('A', 2), ('A', 1)])
    # y = sc.parallelize([('C', 8), ('A', 2), ('D', 1)])
    # z = x.subtract(y)
    # print(x.collect())
    # print(y.collect())
    # print(z.collect())

    # # keyBy
    # x = sc.parallelize([1, 3, 2])
    # y = x.keyBy(lambda x: x ** 2)
    # print(x.collect())
    # print(y.collect())

    # # repartition
    # x = sc.parallelize([1, 2, 3, 4, 5], 2)
    # y = x.repartition(numPartitions=3)
    # print(x.glom().collect())
    # print(x.getNumPartitions())
    # print(y.glom().collect())
    # print(y.getNumPartitions())

    # # coalesce
    # x = sc.parallelize([1, 2, 3, 4, 5], 2)
    # y = x.coalesce(numPartitions=1)
    # print(x.glom().collect())
    # print(y.glom().collect())

    # # zip
    # x = sc.parallelize(['B', 'A', 'A'])
    # # zip expects x and y to have same #partitions and #elements/partition
    # y = x.map(lambda x: ord(x))
    # z = x.zip(y)
    # print(x.collect())
    # print(y.collect())
    # print(z.collect())

    # # zipWithIndex
    # x = sc.parallelize(['B','A','A'],2)
    # y = x.zipWithIndex()
    # print(x.glom().collect())
    # print(y.collect())

    # # zipWithUniqueId
    # x = sc.parallelize(['B','A','A'],2)
    # y = x.zipWithUniqueId()
    # print(x.collect())
    # print(y.collect())