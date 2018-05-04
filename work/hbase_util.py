#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:hbase_util.py
@time:2018/4/16 14:42
"""
from dao import posture_dao


def get_hbase_rdd(sc, table='posture_10w'):
    """
    使用newAPIHadoopRDD方式获取HbaseRDD
    @param sc: SparkContext
    @param table: hbase表
    @return:
    """
    # last_update_time = posture_dao.get_last_update()
    row_start = ""
    # if last_update_time:
    #     row_start = "SS" + last_update_time['update_time'].decode()
    hbase_util = HBaseUtil()
    hbase_util.setTable(table)
    hbase_util.setRowStart(row_start)
    return sc.newAPIHadoopRDD(HBaseUtil.inputFormatClass,
                              HBaseUtil.keyClass,
                              HBaseUtil.valueClass,
                              keyConverter=HBaseUtil.keyConv,
                              valueConverter=HBaseUtil.valueConv,
                              conf=hbase_util.conf)


class HBaseUtil:
    host = 'slave1,slave2,slave3'
    table = 'posture_10w'
    inputFormatClass = 'org.apache.hadoop.hbase.mapreduce.TableInputFormat'
    keyClass = 'org.apache.hadoop.hbase.io.ImmutableBytesWritable'
    valueClass = 'org.apache.hadoop.hbase.client.Result'
    conf = {'hbase.zookeeper.quorum': host,
            'hbase.mapreduce.inputtable': table,
            'hbase.mapreduce.scan.timerange.start': '1524046789053',
            'hbase.mapreduce.scan.timerange.end': '2624046789035'
            # 'hbase.mapreduce.scan.column.family': 'info',
            # 'hbase.mapreduce.scan.columns': 'info:data01',
            # 'hbase.mapreduce.scan.row.start': 'ss0001',
            # 'hbase.mapreduce.scan.row.stop': 'ss0010'
            }
    keyConv = 'org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter'
    valueConv = 'org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter'

    def __init__(self):
        pass

    def setRowStop(self, row_stop):
        self.conf['hbase.mapreduce.scan.row.stop'] = row_stop

    def setRowStart(self, row_start):
        self.conf['hbase.mapreduce.scan.row.start'] = row_start

    def setColumns(self, colums):
        self.conf['hbase.mapreduce.scan.columns'] = colums

    def getColumns(self):
        return self.conf

    def setTable(self, table):
        self.table = table
        self.conf['hbase.mapreduce.inputtable'] = table

    def getConf(self):
        return self.conf


if __name__ == '__main__':
    hbase_utils = HBaseUtil()
    hbase_utils.setColumns("info:A1")

    print(HBaseUtil.conf)
