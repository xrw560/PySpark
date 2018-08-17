#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:path_demo.py
@time:2018/8/9 18:00
@desc:
"""

import os

# 当前文件的path
print("dirname: ", os.path.dirname(__file__))
# 当前文件的文件名
print("basename: ", os.path.basename(__file__))

"""绝对路径"""
print("abspath: ", os.path.abspath(__file__))
print("realpath: ", os.path.realpath(__file__))

# 将path分割成目录和文件名二元组返回
print("split: ", os.path.split(__file__))

path = os.path.split(os.path.realpath(__file__))[0]
print(path)

print(os.listdir(os.path.dirname(__file__)))
