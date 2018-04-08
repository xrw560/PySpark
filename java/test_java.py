#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:.py
@time:2018/4/4 11:36
"""

from pyspark import SparkContext
from py4j.java_gateway import java_import

sc = SparkContext(appName="Py4jTesting")
java_import(sc._jvm, "org.valux.py4j.Calculate")
func = sc._jvm.Calculate()
result = func.getBody('zhouning', 25)
print(result.getName())
print(func.getBody('zhouning', 25))
