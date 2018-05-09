#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:pandas1.py
@time:2018/5/9 11:42
"""
import pandas

if __name__ == '__main__':
    food_info = pandas.read_csv("food_info.csv")
    # print(type(food_info))
    # print(food_info.dtypes)

    first_rows = food_info.head()
    # print(first_rows)
    # print(food_info.head(3))
    print(food_info.columns)
    # print(food_info.shape)

    # pandas uses zero-indexing
    # series object representing the row at index 0.
    # print(food_info.loc[0])

    # series object representing the seventh row.
    # print(food_info.loc[6])

    # will throw an error: KeyError: 'the label [8620] is not in the [index]'
    # food_info.loc[8620]

    # the object dtype is equivalent to a string in python
    # object - for string values
    # int - for integer values
    # float - for float values
    # datetime - for time values
    # bool - for boolean values
    # print(food_info.dtypes)

    # returns a DataFrame containing the rows at indexes 3,4,5 and 6
    # print(food_info.loc[3:6])

    # returns a DataFrame containing the rows at indexes 2,5 and 10. Either of the following approaches will work.
    # Method  1
    # two_five_ten = [2, 5, 10]
    # print(food_info.loc[two_five_ten])

    # Method 2
    # print(food_info.loc[[2, 5, 10]])

    # series object representing the "NDB_no" column
    # ndb_col = food_info["NDB_No"]
    # print(ndb_col)
    # Alternatively, you can access a column by passing in a string variable
    # col_name = "NDB_No"
    # ndb_col = food_info[col_name]
    # print(ndb_col)

    # columns = ["Zinc_(mg)", "Copper_(mg)"]
    # zinc_copper = food_info[columns]
    # print(zinc_copper)
    # skipping the assignment.
    # zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]
    # print(zinc_copper)

    col_names = food_info.columns.tolist()
    # print(col_names)
    # print(food_info.head(2))
    gram_columns = []

    for c in col_names:
        if c.endswith("(g)"):
            gram_columns.append(c)
    gram_df = food_info[gram_columns]
    print(gram_df.head(3))