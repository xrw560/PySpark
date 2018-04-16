#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:python_execute.py
@time:2018/4/9 13:49
"""
import pymysql
import datetime

if __name__ == '__main__':
    start = datetime.datetime.now()
    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='python_test')
    # 创建游标
    cursor = conn.cursor()
    # # 执行SQL，并返回影响行数
    # effect_row = cursor.execute("update hosts set host='1.1.1.2'")

    # # 执行SQL，并返回影响行数
    # effect_row = cursor.execute("UPDATE hosts SET host='1.1.1.3' WHERE color_id>%s", (1,))

    # 执行SQL，并返回影响行数
    effect_row = cursor.executemany("INSERT INTO hosts(host,color_id) VALUES(%s,%s)",
                                    [("1.1.1.11", 1), ("1.1.1.12", 2)])

    # 提交，不然无法保存或修改的数据
    conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    end = datetime.datetime.now()
    print(end - start)
