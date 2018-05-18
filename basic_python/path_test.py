#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:path_test.py
@time:2018/5/15 9:17
"""
from os import path

if __name__ == '__main__':
    # 获取当前文件的路径：
    print("dirname: ", path.dirname(__file__))  # 返回一个目录的目录名

    print("dirname(dirname(__file__)): ", path.dirname(path.dirname(__file__)))  # 获得d所在的目录,即d的父级目录

    print("abspath：", path.abspath(__file__))  # 返回一个目录的绝对路径
    print("realpath: ", path.realpath(__file__))  # 返回指定文件的标准路径，而非软链接所在的路径
    print("split: ", path.split(path.realpath(__file__)))  # 分割目录名，返回由其目录名和基名给成的元组
