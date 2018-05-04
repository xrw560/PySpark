#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:jdbc_get.py
@time:2018/4/9 14:38
"""
import pymysql
import MySQLdb as db

if __name__ == '__main__':
    # conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password='root', db='python_test')
    conn = db.connect(host='192.168.138.134', user="root", passwd="root", db="movie_db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movie")


    # 获取第一行数据
    # row_1 = cursor.fetchone()
    # print(row_1)

    # # 获取前N行数据
    # row_2 = cursor.fetchmany(3)
    # print(row_2)

    # 获取所有数据
    row_3 = cursor.fetchall()
    print(row_3)

    conn.commit()
    cursor.close()
    conn.close()
