#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:plt_1.py
@time:2018/4/28 14:01
"""
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    unrate = pd.read_csv("unrate.csv")
    unrate["DATE"] = pd.to_datetime(unrate["DATE"])
    # print(unrate.head(12))

    first_twelve = unrate[0:12]
    plt.plot(first_twelve["DATE"], first_twelve["VALUE"])
    plt.xticks(rotation=45) # rotate the x-axis tick labels by 45 degrees
    plt.xlabel("Month")
    plt.ylabel("Unemployment Rate")
    plt.title("Monthly Unemployment Trends, 1948")
    plt.show()
