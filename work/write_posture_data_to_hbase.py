# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:write_posture_data_to_hbase.py
@time:2018/3/28 15:58
"""
from pyspark import SparkConf, SparkContext
import random
import datetime

if __name__ == '__main__':
    start = datetime.datetime.now()
    sparkConf = SparkConf() \
        .setAppName('write_posture_data_to_hbase')
    sc = SparkContext(conf=sparkConf)
    sc.setLogLevel('WARN')

    host = 'slave1,slave2,slave3'
    table = 'posture_500w'
    keyClass = 'org.apache.hadoop.hbase.io.ImmutableBytesWritable'
    valueClass = 'org.apache.hadoop.hbase.client.Result'
    conf = {'hbase.zookeeper.quorum': host,
            'hbase.mapred.outputtable': table,
            "mapreduce.outputformat.class": "org.apache.hadoop.hbase.mapreduce.TableOutputFormat",
            "mapreduce.job.output.key.class": "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
            "mapreduce.job.output.value.class": "org.apache.hadoop.io.Writable"
            }
    keyConv = 'org.apache.spark.examples.pythonconverters.StringToImmutableBytesWritableConverter'
    valueConv = 'org.apache.spark.examples.pythonconverters.StringListToPutConverter'

    now = datetime.datetime.now()

    for cnt in range(1, 21):
        raw_data = []
        for i in range(1, 250001):
            row_key = (now + datetime.timedelta(milliseconds=(250000 * (cnt - 1) + i))).strftime('%Y%m%d%H%M%S%f')
            raw_data.append('SS{:0>20},info,A1,{:}'.format(row_key, '011000111100'))
            raw_data.append('SS{:0>20},info,A2,{:}'.format(row_key, 0.05 + (random.random() * 0.05)))
            raw_data.append('SS{:0>20},info,A3,{:}'.format(row_key, 0.05 + (random.random() * 0.05)))
            raw_data.append('SS{:0>20},info,A4,{:}'.format(row_key, 6.6 + (random.random() * 0.4)))
            raw_data.append('SS{:0>20},info,A5,{:}'.format(row_key, 6 + (random.random() * 0.4)))
            raw_data.append('SS{:0>20},info,A6,{:}'.format(row_key, 0))

        sc.parallelize(raw_data) \
            .map(lambda x: (table, x.split(','))) \
            .saveAsNewAPIHadoopDataset(conf=conf, keyConverter=keyConv, valueConverter=valueConv)
        print("----------------> ", cnt)
        end = datetime.datetime.now()
        print(end - start)

    sc.stop()
    print('============== end ===================')
