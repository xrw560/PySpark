#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:driver.py
@time:2018/5/7 9:44
https://blog.csdn.net/lawme/article/details/5396290
"""
from pyke import knowledge_engine

if __name__ == '__main__':
    engine = knowledge_engine.engine(__file__)
    engine.activate("plan_example")
    no_vars, plan1 = engine.prove_1_goal("plan_example.transfer((bruce,checking),(bruce,savings))")
    plan1(100)
