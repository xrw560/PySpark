#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:driver.py
@time:2018/5/3 17:48
"""
from pyke import knowledge_engine

if __name__ == '__main__':
    engine = knowledge_engine.engine(__file__)
    engine.activate('bc')
    st = 'fred'
    with engine.prove_goal('bc.uncle_nephew(' + st + ', $nephew, $distance)') as gen:
        for vars, no_plan in gen:
            print(vars['nephew'], vars['distance'])
