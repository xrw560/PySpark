#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:numpy_1.py
@time:2018/5/4 9:00
"""
import numpy

if __name__ == '__main__':
    world_alcohol = numpy.genfromtxt("world_alcohol.txt", delimiter=",")
    # print(help(numpy.genfromtxt))
    # print(type(world_alcohol))

    # The numpy.array() function can take a list or lists as input
    # When we input a list, we get a one-dimensional  array as a result
    vector = numpy.array([5, 10, 15, 20])
    # When we input a list of lists, we get a matrix as a result
    matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
    # print(vector)
    # print(matrix)

    # We can use the ndarray.shape property to figure out how many elements are in the array
    # print(vector.shape)
    # For matrics, the shape property contains a tuple with 2 elements
    # print(matrix.shape)

    # Each value in a Numpy array has to have the same data type
    # Numpy will automatically figure out an appropriate data type when reading in data or converting lists to arrays.
    # You can check the data type of a Numpy array using the dtype property
    # print(vector.dtype)

    # When Numpy can't convert a value to a numeric data type like float or integer, it uses a special nan value that stands for Not a Number
    # nan  is the missing data
    # 1.987e+03 is actually 1.987*10^3
    # print(world_alcohol)

    world_alcohol = numpy.genfromtxt("world_alcohol.txt", delimiter=",", dtype="U75", skip_header=1)
    # print(world_alcohol)

    # 通过索引取某个值
    uruguay_other_1986 = world_alcohol[1, 4]  # 第二个样本，第五列
    third_country = world_alcohol[2, 2]
    # print(uruguay_other_1986)
    # print(third_country)

    # 切片
    vector = numpy.array([5, 10, 15, 20])
    # print(vector[0:3])

    matrix = numpy.array([
        [5, 10, 15],
        [20, 25, 30],
        [35, 40, 45]])
    # print(matrix[:, 1])  # 取某列，":"表示所有
    # print(matrix[:, 0:2])  # 取两列
    print(matrix[1:3, 0:2])  # 取某些行，某些列
