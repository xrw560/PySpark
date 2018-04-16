#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:jdbc_fetch.py
@time:2018/4/9 14:44
"""
import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='python_test')

    # 游标设置为字典类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    r = cursor.execute("call p1()")
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
