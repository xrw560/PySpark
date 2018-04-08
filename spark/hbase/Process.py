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
