#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:happybase.py
@time:2018/6/13 10:47
"""
import happybase

if __name__ == '__main__':
    connection = happybase.Connection("192.168.2.190")
    table = connection.table("sat_new")
    row = table.row('001')
    print(row)
    # table.put("00PT20180613105203", {"info:SATNUM": "03"})
    # rows = table.scan(limit=10)

    # # scanner = table.scan(row_start=None, row_stop=None, row_prefix=None, columns=None,
    #                      filter=None, timestamp=None, include_timestamp=False, batch_size=1000, scan_batching=None,
    #                      limit=None, sorted_columns=False, reverse=False)
    # for i in scanner:
    #     print(i)
