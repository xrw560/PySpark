#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:numpy_2.py
@time:2018/5/8 8:54
"""
import numpy

if __name__ == '__main__':
    vector = numpy.array([5, 10, 15, 20])
    # it will compare the second value to each element in the vector
    # if the values  are equal, the python interpreter returns True, otherwise, it returns False
    # print(vector == 10)  # 对每个元素进行同样的运算

    matrix = numpy.array([
        [5, 10, 15],
        [20, 25, 30],
        [35, 40, 45]
    ])
    # print(matrix == 25)

    # compares vector to the value 10, which generates a new Boolean vector[False, True, False, False].
    # It assigns this result to equal_to_ten
    equal_to_ten = (vector == 10)
    # print(equal_to_ten)  # [False  True False False]
    # print(vector[equal_to_ten])  # 10

    second_column_25 = (matrix[:, 1] == 25)
    # print(matrix[:, 1])  # [10 25 40]
    # print(second_column_25)  # [False  True False]
    # print(matrix[second_column_25, :])  # [[20 25 30]]

    # we can also perform comparisons with multiple conditions
    equal_to_ten_and_five = (vector == 10) & (vector == 5)
    # print(equal_to_ten_and_five)  # [False False False False]

    equal_to_ten_or_five = (vector == 10) | (vector == 5)
    # print(equal_to_ten_or_five) #[ True  True False False]
    vector[equal_to_ten_or_five] = 50
    # print(vector)

    second_column_25 = matrix[:, 1] == 25
    # print(second_column_25)  # [False  True False]
    matrix[second_column_25, 1] = 10
    # print(matrix)

    # # we can convert the data tpe of an array with the ndarray.astype() method
    # vector = numpy.array(["1", "2", "3"])
    # print(vector.dtype)  # <U1
    # print(vector)  # ['1' '2' '3']
    # vector = vector.astype(float)
    # print(vector.dtype)  # float64
    # print(vector)  # [1. 2. 3.]

    vector = numpy.array([5, 10, 15, 20])
    # print(vector.sum())#50
    # print(help(numpy.sum))

    matrix = numpy.array([
        [5, 10, 15],
        [20, 25, 30],
        [35, 40, 45]
    ])
    # the  axis dictates which dimensions we preform the operation on
    # I means that we want to perform the operation on each row, and 0 means on each column
    # print(matrix.sum(axis=1))  # [ 30  75 120]
    # print(matrix.sum(axis=0))  # [60 75 90]

    # replace nan value with 0
    world_alcohol = numpy.genfromtxt("world_alcohol.txt", delimiter=",")
    is_value_empty = numpy.isnan(world_alcohol[:, 4])
    # print(is_value_empty)
    world_alcohol[is_value_empty, 4] = '0'
    alcohol_consumption = world_alcohol[:, 4]
    alcohol_comsumption = alcohol_consumption.astype(float)
    total_alcohol = alcohol_comsumption.sum()
    average_alcohol = alcohol_comsumption.mean()
    print(total_alcohol)
    print(average_alcohol)
