#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:dict_util.py
@time:2018/4/17 10:04
"""


def dict_concat(dict1, dict2):
    """
    字典拼接
    @param dict1:
    @param dict2:
    @return:
    """
    dict1.update(dict2)
    return dict1


if __name__ == '__main__':
    pass
