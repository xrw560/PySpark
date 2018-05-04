#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:data_prepare.py
@time:2018/4/16 15:04
"""


def init_hbase_data(rdict):
    """
    初始化hbase返回的字典数据
    @param rdict:
    @return:
    """
    del rdict['columnFamily']
    del rdict['timestamp']
    del rdict['type']
    rdict[rdict['qualifier']] = rdict['value']  # 数据格式：A1:0.01
    del rdict['qualifier']
    del rdict['value']
    return rdict


def dict_del(rdict):
    """
    初始化hbase返回的字典数据，去除无用的数据
    @param rdict:
    @return:
    """
    del rdict['columnFamily']
    del rdict['timestamp']
    del rdict['type']
    rdict['value'] = float(rdict['value'])
    return rdict
