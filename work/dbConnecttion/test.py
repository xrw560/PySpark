#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:test.py
@time:2018/4/17 14:42
"""
from MySqlConn import Mysql
# from _sqlite3 import Row
import datetime
import posture_dao


def insert_data():
    # 申请资源
    mysql = Mysql()
    roll_max = 0.0999989
    roll_min = 0.050000374106515644
    roll_mean = 0.07501550874813788
    roll_count = 100
    pitch_max = 0.09999891074324113
    pitch_min = 0.050000374106515644
    pitch_mean = 0.07501550874813788
    pitch_count = 1000
    deviation_max = 0.09999891074324113
    deviation_min = 0.050000374106515644
    deviation_mean = 0.07501550874813788
    deviation_count = 100
    total_score = 87.76071883296575

    insert_sql = "INSERT INTO posture_result(update_time,delta_roll_max,delta_roll_min,delta_roll_mean,delta_roll_count,delta_pitch_max,delta_pitch_min,delta_pitch_mean,delta_pitch_count,delta_deviation_max,delta_deviation_min,delta_deviation_mean,delat_deviation_count,score) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    update_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    mysql.insertMany(insert_sql, [(
        update_time, roll_max, roll_min, roll_mean, roll_count, pitch_max, pitch_min, pitch_mean, pitch_count,
        deviation_max, deviation_min, deviation_mean, deviation_count, total_score)])

    # 释放资源
    mysql.dispose()


def get_one():
    # 申请资源
    mysql = Mysql()

    get_sql = "SELECT * FROM posture_result ORDER BY update_time DESC LIMIT 1"
    result = mysql.getOne(get_sql)
    # print("{:}\t{:}".format(result['update_time'],result['score']))
    print(type(result))
    print(result)

    # 释放资源
    mysql.dispose()


if __name__ == '__main__':
    a = b = 'aa'
    print(a, '  ', b)
