#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:posture_dao.py
@time:2018/4/17 16:04
"""
from dbConnecttion.MySqlConn import Mysql


def get_last_update():
    """
    获取mysql中最后一条统计数据
    @return: 行数据<dict>
    """
    # 申请资源
    mysql = Mysql()
    get_sql = "SELECT * FROM posture_result ORDER BY update_time DESC LIMIT 1"
    result = mysql.getOne(get_sql)
    # 释放资源
    mysql.dispose()
    return result


def insert_stat_data(values):
    """
    [(update_time, roll_max, roll_min, roll_mean, roll_count, pitch_max, pitch_min, pitch_mean, pitch_count,
        deviation_max, deviation_min, deviation_mean, deviation_count, total_score)]
    @param values:
    @return:
    """
    # 申请资源
    mysql = Mysql()
    insert_sql = "INSERT INTO posture_result(update_time,delta_roll_max,delta_roll_min,delta_roll_mean,delta_roll_count,delta_pitch_max,delta_pitch_min,delta_pitch_mean,delta_pitch_count,delta_deviation_max,delta_deviation_min,delta_deviation_mean,delat_deviation_count,score) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    mysql.insertMany(insert_sql, values)
    # 释放资源
    mysql.dispose()


def insert_stat_data_with_merge_data(values):
    """
    插入本次统计以及融合后的数据
    @param values:(update_time, roll_max, roll_min, roll_mean, roll_count, pitch_max, pitch_min, pitch_mean, pitch_count,
         deviation_max, deviation_min, deviation_mean, deviation_count, merge_roll_max, merge_roll_min, merge_roll_mean,
         merge_roll_count, merge_pitch_max, merge_pitch_min, merge_pitch_mean, merge_pitch_count, merge_deviation_max,
         merge_deviation_min, merge_deviation_mean, merge_deviation_count, total_score)
    @return:
    """
    # 申请资源
    mysql = Mysql()
    insert_sql = "INSERT INTO posture_result(update_time,delta_roll_max,delta_roll_min,delta_roll_mean,delta_roll_count,delta_pitch_max,delta_pitch_min,delta_pitch_mean,delta_pitch_count,delta_deviation_max,delta_deviation_min,delta_deviation_mean,delat_deviation_count,merge_roll_max,merge_roll_min,merge_roll_mean,merge_roll_count,merge_pitch_max,merge_pitch_min,merge_pitch_mean,merge_pitch_count,merge_deviation_max,merge_deviation_min,merge_deviation_mean,merge_deviation_count,score) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    mysql.insertMany(insert_sql, values)
    # 释放资源
    mysql.dispose()


if __name__ == '__main__':
    pass
