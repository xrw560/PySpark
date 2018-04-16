#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:get_last_row_id.py
@time:2018/4/9 14:29
"""
import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='root', db='python_test')
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO hosts(host,color_id) VALUES(%s,%s)", [("1.1.2.11", 3), ("1.1.2.12", 4)])
    conn.commit()
    cursor.close()
    conn.close()

    # 获取最新自增ID
    new_id = cursor.lastrowid
    print(new_id)
