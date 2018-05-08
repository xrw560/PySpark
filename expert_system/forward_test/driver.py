#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:driver.py
@time:2018/5/7 10:54
https://blog.csdn.net/lawme/article/details/5378278
"""
from pyke import knowledge_engine, goal

if __name__ == '__main__':
    engine = knowledge_engine.engine(__file__)
    engine.activate("fc_related")  # This is where the  rules are run!
    engine.get_kb("family").dump_specific_facts()
    # print(engine.prove_1_goal('family1.son_of(thomas,$son)'))
    print(engine.prove_1_goal('family.father_son(hiram,$son,())'))
    fc_goal = goal.compile('family.how_related($person1, $person2, $relationship)')
    print("finish...")