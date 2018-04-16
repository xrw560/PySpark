# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:write_to_hbase.py
@time:2018/3/28 15:58
"""
from pyspark import SparkConf, SparkContext
import random
import datetime

if __name__ == '__main__':
    start = datetime.datetime.now()
    sparkConf = SparkConf() \
        .setAppName('write_to_hbase')
    sc = SparkContext(conf=sparkConf)
    sc.setLogLevel('WARN')

    host = 'slave1,slave2,slave3'
    table = 'z_spark_5000w_three'
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

    for cnt in range(160, 201):
        raw_data = []
        for i in range(1, 250001):
        # for i in range(1, 10001):
        # for i in range(1, 100001):
            for j in range(1, 5):
                raw_data.append('SS%.4d%.8d,info,data0%d,%.2f' % (cnt, i, j, j - 0.25 + (random.random() * 0.5)))

        sc.parallelize(raw_data) \
            .map(lambda x: (table, x.split(','))) \
            .saveAsNewAPIHadoopDataset(conf=conf, keyConverter=keyConv, valueConverter=valueConv)
        print("----------------> ", cnt)
        end = datetime.datetime.now()
        print(end - start)

    sc.stop()
    print('============== end ===================')
