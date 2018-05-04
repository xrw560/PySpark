#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:score_compute_util.py
@time:2018/4/17 9:48
"""


def get_roll_score(angle):
    """
    获取滚动角打分值
    @param angle: 滚动角均值
    @return: 分数
    """
    angle = abs(angle)
    if angle <= 0.06:
        return 100
    elif angle >= 0.1:
        return 60
    else:
        return 100 - (angle - 0.06) / (0.1 - 0.06) * 40


def get_pitch_score(angle):
    """
    获取俯仰角打分值
    @param angle: 俯仰角均值
    @return: 分数
    """
    angle = abs(angle)
    if angle <= 0.06:
        return 100
    elif angle >= 0.1:
        return 60
    else:
        return 100 - (angle - 0.06) / (0.1 - 0.06) * 40


def get_deviation_score(angle):
    """
    获取卫星偏航的打分值
    @param angle: 偏航角偏执量-偏航角
    @return: 分数
    """
    angle = abs(angle)
    if angle <= 0.5:
        return 100
    elif angle >= 1.0:
        return 60
    else:
        return 100 - (angle - 0.5) / (1.0 - 0.5) * 40


def get_total_score(roll_score, pitch_score, deviation_score):
    """
    获取项目总分
    @param roll_score: 滚动角分数
    @param pitch_score: 俯仰角分数
    @param deviation_score: 偏航分数
    @return:
    """
    return 1 / 3 * roll_score + 1 / 3 * pitch_score + 1 / 3 * deviation_score


def get_mean_value(first_mean, first_count, second_mean, second_count):
    """
    获取平均值
    @param first_mean: 第一个均值
    @param first_count: 第一个数目
    @param second_mean: 第二个均值
    @param second_count: 第二个数目
    @return: 两者的均值
    """
    total = first_count * first_mean + second_count * second_mean
    return total / (first_count + second_count)


if __name__ == '__main__':
    print(get_roll_score(-0.04))
    print(get_roll_score(-0.1))
    print(get_roll_score(-0.2))
    print(get_deviation_score(-0.5))
    print(get_deviation_score(-1.0))
    print(get_deviation_score(-0.75))
