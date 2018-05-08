#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:driver.py
@time:2018/5/7 11:34
https://blog.csdn.net/lawme/article/details/5383855
"""
from pyke import knowledge_engine

if __name__ == '__main__':
    engine = knowledge_engine.engine(__file__)
    engine.activate("bc_related")
    with engine.prove_goal('bc_related.uncle_nephew(fred, $nephew, $distance)') as gen:
        for vars, no_plan in gen:
            print(vars['nephew'], vars['distance'])
