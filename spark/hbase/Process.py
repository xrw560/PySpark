#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:.py
@time:2018/4/8 9:54
"""
import happybase
import datetime
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.stat import Statistics
from pyspark import SparkConf, SparkContext
import time
import random


class Test(object):
    """this is a test"""

    def __init__(self, appName, columns, master, table):
        conf = SparkConf()
        conf.setAppName(appName)
        self.sc = SparkContext(conf=conf)
        connection = happybase.Connection(master)
        self.table = connection.table(table)
        self.columns = columns

    """this is a job test"""

    def scriptJob(self, limit=None, rowstart=None, rowstop=None):
        start = datetime.datetime.now()
        # create hbase connection

        row = self.table.scan(row_start=rowstart, row_stop=rowstop, limit=limit, columns=self.columns)
        print(type(row))

        testRdd = self.sc.parallelize(row)
        values = testRdd.values()
        print(values.count())

        col = bytes(self.columns.encode("utf-8"))
        serilizeRdd = values.map(lambda value: float(value.get(col).decode()))

        #
        # def hash_domain(url):
        #     return hash(urlparse.urlparse(url).netloc)

        mlibRDD = self.sc.parallelize((([Vectors.dense(x)]) for x in serilizeRdd.collect()))

        cStats = Statistics.colStats(mlibRDD)
        # print(cStats.mean())

        end = datetime.datetime.now()
        print(end - start)
        return cStats.mean()

    def insertBatch(self):
        """put(row, data, timestamp=None, wal=True)   table.put("row1",{"cf:1":"1"})"""
        RowKeyFirst = "NO1"
        sp = "XP"

        for i in range(50000, 100000):
            # print(i)
            num = "%08d" % int(i)
            # dateName = str(int(time.time()))
            rowkey = RowKeyFirst + sp + num
            # print(rowkey)
            self.table.put(row=rowkey, data={"cf1:gdj": str(int(80)),
                                             "cf1:fyj": str(int(90)),
                                             "cf1:phj": str(int(95)),
                                             "cf1:phl": str(int(100))})
        # return 0
