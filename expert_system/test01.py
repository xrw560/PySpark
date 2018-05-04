#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:test01.py
@time:2018/4/23 18:12
"""
from functools import partial


def foo(cooked, standard):
    print("foo called with cooked:%s, standard:%s" % (cooked, standard))


def bar(child_fun, a):
    # 函数 bar 的第一参数是个引用，即函数名
    print("bar called with:", a)
    return child_fun(a)


if __name__ == '__main__':
    # foo('a', 'b')

    # # 原函数 foo 的第一个参数，被调制成为函数 cooked1，foo 的第二个参数，成了 cooked1 的唯一参数。
    cooked1 = partial(foo, 'cooked_value1')
    # cooked1('value1')  # foo called with cooked:cooked_value1, standard:value1
    # cooked1('value2')  # foo called with cooked:cooked_value1, standard:value2
    #
    # print('------------------')
    cooked2 = partial(foo, 'cooked_value2')
    # cooked2('value1')  # foo called with cooked:cooked_value2, standard:value1
    # cooked2('value2')  # foo called with cooked:cooked_value2, standard:value2

    bar_float = partial(bar, float)
    # print(bar_float('123'))  # bar called with: 123  # 123.0
    #
    bar_min = partial(bar, min)
    # print(bar_min((3, 2, 5)))  # bar called with: (3, 2, 5) # 2
    #
    bar_cooked1 = partial(bar, cooked1)  # bar called with: abc
    # bar_cooked1('abc')  # bar called with: abc # foo called with cooked:cooked_value1, standard:abc
    #
    bar_bar_min = partial(bar, bar_min)
    # print(bar_bar_min((3, 2, 5)))  # bar called with: (3, 2, 5) # bar called with: (3, 2, 5) # 2
