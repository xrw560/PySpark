#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:plt_4.py
@time:2018/4/28 17:42
柱状图和盒图
"""
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    reviews = pd.read_csv("fandango_scores.csv")
    cols = ["FILM", "RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue"]
    norm_reviews = reviews[cols]
    # print(norm_reviews[:5])

    fandango_distribution = norm_reviews["Fandango_Ratingvalue"].value_counts()
    fandango_distribution = fandango_distribution.sort_index()

    imdb_distribution = norm_reviews["IMDB_norm"].value_counts()
    imdb_distribution = imdb_distribution.sort_index()

    # print(fandango_distribution)
    # print(imdb_distribution)

    # fig, ax = plt.subplots()
    # ax.hist(norm_reviews["Fandango_Ratingvalue"])
    # ax.hist(norm_reviews["Fandango_Ratingvalue"],bins=20)
    # ax.hist(norm_reviews["Fandango_Ratingvalue"], range=(4, 5), bins=20)
    # plt.show()

    # fig = plt.figure(figsize=(5, 20))
    # ax1 = fig.add_subplot(4, 1, 1)
    # ax2 = fig.add_subplot(4, 1, 2)
    # ax3 = fig.add_subplot(4, 1, 3)
    # ax4 = fig.add_subplot(4, 1, 4)
    # ax1.hist(norm_reviews["Fandango_Ratingvalue"], bins=20, range=(0, 5))
    # ax1.set_title("Distribution of Fandango Ratings")
    # ax1.set_ylim(0, 50)
    #
    # ax2.hist(norm_reviews["RT_user_norm"], 20, range=(0, 5))
    # ax2.set_title("Distribution of Rotten Tomatoes Ratings")
    # ax2.set_ylim(0, 50)
    #
    # ax3.hist(norm_reviews["Metacritic_user_nom"], 20, range=(0, 5))
    # ax3.set_title("Distribution of Metacritic Rating")
    # ax3.set_ylim(0, 50)
    #
    # ax4.hist(norm_reviews["IMDB_norm"], 20, range=(0, 5))
    # ax4.set_title("Distribution of IMDB Ratings")
    # ax4.set_ylim(0, 50)
    # plt.show()

    # --------------------------盒图------------------------
    # fig, ax = plt.subplots()
    # ax.boxplot(norm_reviews["RT_user_norm"].values)
    # ax.set_xticklabels(["Rotten Tomatoes"])
    # ax.set_ylim(0, 5)
    # plt.show()

    # num_cols = ["RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue"]
    # fig, ax = plt.subplots()
    # ax.boxplot(norm_reviews[num_cols].values)
    # ax.set_xticklabels(num_cols, rotation=90)
    # ax.set_ylim(0, 5)
    # plt.show()
