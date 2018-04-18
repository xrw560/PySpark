#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:common_util.py
@time:2018/4/17 16:47
"""
from pyspark import SparkConf, SparkContext
import dict_util


def create_spark_context(app_name='demo', log_level='WARN'):
    """
    获取SparkContext
    @param app_name:
    @param log_level:
    @return:
    """
    spark_conf = SparkConf() \
        .setAppName(app_name) \
        .set("spark.ui.showConsoleProgress", "false")
    sc = SparkContext(conf=spark_conf)
    sc.setLogLevel(log_level)
    sc.addPyFile("dict_util.py")
    sc.addPyFile("data_prepare.py")
    return sc


if __name__ == '__main__':
    pass
