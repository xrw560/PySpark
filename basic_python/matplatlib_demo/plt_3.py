#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:plt_3.py
@time:2018/4/28 14:41
条形图和散点图
"""
import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

if __name__ == '__main__':
    reviews = pd.read_csv("fandango_scores.csv")
    cols = ["FILM", "RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]
    norm_reviews = reviews[cols]
    # print(norm_reviews[:1])

    # num_cols = ["RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]
    # bar_heights = norm_reviews.ix[0, num_cols].values
    # # print(bar_heights)
    # bar_positions = arange(5) + 0.75
    # # print(bar_positions)
    # fig, ax = plt.subplots()  # ax实际画图，fig控制图的风格
    # """
    #     The Axes.bar() method has 2 required parameters, left and height
    #     We use the left parameter to specific the x coordinates of the left sides of the bar
    #     We use the height parameter to specific the height of each bar
    # """
    # ax.bar(bar_positions, bar_heights, 0.5)  # 0.5：条形图的粗细
    # plt.show()

    # num_cols = ["RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]
    # bar_widths = norm_reviews.ix[0, num_cols].values
    # bar_positions = arange(5) + 0.75
    # tick_positions = range(1, 6)
    # fig, ax = plt.subplots()
    # ax.barh(bar_positions, bar_widths, 0.5)
    #
    # ax.set_yticks(tick_positions)
    # ax.set_yticklabels(num_cols)
    # ax.set_ylabel("Rating Source")
    # ax.set_xlabel("Average Rating")
    # ax.set_title("Average User Rating For Avengers:Age of Ultron(2015)")
    # plt.show()

    # fig, ax = plt.subplots()
    # ax.scatter(norm_reviews["Fandango_Ratingvalue"], norm_reviews["RT_user_norm"])
    # ax.set_xlabel("Fandango")
    # ax.set_ylabel("Rotten Tomatoes")
    # plt.show()

    # Switching Axes
    fig = plt.figure(figsize=(5, 10))
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    ax1.scatter(norm_reviews["Fandango_Ratingvalue"], norm_reviews["RT_user_norm"])
    ax1.set_xlabel("Fandango")
    ax1.set_ylabel("Rotten Tomatoes")
    ax2.scatter(norm_reviews["RT_user_norm"], norm_reviews["Fandango_Ratingvalue"])
    ax2.set_xlabel("Rotten Tomatoes")
    ax2.set_ylabel("Fandango")
    plt.show()
