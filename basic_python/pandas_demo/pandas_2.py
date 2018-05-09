#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:pandas_2.py
@time:2018/5/9 12:05
"""
import pandas

if __name__ == '__main__':
    food_info = pandas.read_csv("food_info.csv")
    col_names = food_info.columns.tolist()
    print(col_names)
    # print(food_info.head(3))

    # print(food_info["Iron_(mg)"])
    div_100 = food_info["Iron_(mg)"] / 1000
    # print(div_100)
    # Adds 100 to each value in the column and returns a series object
    add_100 = food_info["Iron_(mg)"] + 100

    # subtracts 100 from each value in the column and returns a series object
    sub_100 = food_info["Iron_(mg)"] - 100

    # multiplies each value in the column by 2 and returns a series object
    mult_2 = food_info["Iron_(mg)"] * 2

    # it applies the arithmetic operator to the first value in both columns, the second value in both columns, and son on
    water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
    iron_grams = food_info["Iron_(mg)"] / 1000
    food_info["Iron_(g)"] = iron_grams

    # Score = 2 X (Protein_(g))- 0.75 X (Lipid_Tot_(g))
    weighted_protein = food_info["Protein_(g)"] * 2
    weight_fat = -0.75 * food_info["Lipid_Tot_(g)"]
    initial_rating = weighted_protein + weight_fat

    # the "Vit_A_IU" column ranges from 0 to 100000, while the "Fiber_TD_(g)" column ranges from 0 to 79
    # For certain calculations, columns like "Vit_A_IU" can have a greater effect on the result.
    # due to the scale of the values
    # The largest value in the "Energ_Kcal" column.
    max_calories = food_info["Energ_Kcal"].max()
    # Divide the values in "Energ_Kcal" by the largest value.
    normalized_calories = food_info["Energ_Kcal"] / max_calories
    normalized_protein = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
    normalized_fat = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
    food_info["Normalized_Protein"] = normalized_protein
    food_info["Normalized_Fat"] = normalized_fat

    # 排序
    # by default, pandas will  sort the data by the column  we specify in ascending order and returns a new DataFrame
    # sorts the DataFrame in-place, rather than returning a new DataFrame.
    food_info.sort_values("Sodium_(mg)", inplace=True)
    # print(food_info["Sodium_(mg)"])
    # sorts by descending order, rather than ascending
    food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)
    print(food_info["Sodium_(mg)"])
