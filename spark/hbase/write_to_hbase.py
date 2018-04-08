# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:write_to_hbase.py
@time:2018/3/28 15:58
"""
from pyspark import SparkConf, SparkContext
import random
import datetime

# def converthbase_key_value(key, value):
#     row_key = key
#     column_family = "info"
#     column_name = value.split(":")[0]
#     column_value = value.split(":")[1]
#     result = (table, [row_key, column_family, column_name, column_value])
#     return result


if __name__ == '__main__':
    start = datetime.datetime.now()
    sparkConf = SparkConf() \
        .setAppName('write_to_hbase')
    sc = SparkContext(conf=sparkConf)
    sc.setLogLevel('WARN')

    host = 'slave1,slave2,slave3'
    # table = 'z_spark_1w'
    table = 'z_spark_5000w_one'
    # table = 'z_spark_500w'
    # table = 'z_spark_1000w'
    # table = 'z_spark_500w'
    # table = 'z_spark_1000w_2f'
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

    # rawData = ['002,info,data01,1.2', '002,info,data02,2.1', '002,info,data03,3.1', '002,info,data04,4.1']

    # sc.parallelize(rawData) \
    #     .map(lambda x: (x[0], x.split(','))) \
    #     .saveAsNewAPIHadoopDataset(conf=conf,
    #                                keyConverter=keyConv,
    #                                valueConverter=valueConv)

    # for cnt in range(1, 2):
    for cnt in range(60, 101):
        # for cnt in range(1, 11):
        # for cnt in range(11, 21):
        # for cnt in range(21, 31):
        # for cnt in range(31, 41):
        # for cnt in range(41, 51):
        # for cnt in range(51, 61):
        # for cnt in range(61, 71):
        # for cnt in range(71, 81):
        # for cnt in range(81, 91):
        # for cnt in range(91, 101):

        # for cnt in range(101, 111):
        # for cnt in range(111, 121):
        # for cnt in range(121, 131):
        # for cnt in range(131, 141):
        # for cnt in range(141, 151):
        # for cnt in range(151, 161):
        # for cnt in range(161, 171):
        # for cnt in range(171, 181):
        # for cnt in range(181, 191):
        # for cnt in range(191, 201):

        # for cnt in range(201, 211):
        # for cnt in range(211, 221):
        # for cnt in range(221, 231):
        # for cnt in range(231, 241):
        # for cnt in range(241, 251):
        # for cnt in range(251, 261):
        # for cnt in range(261, 271):
        # for cnt in range(271, 281):
        # for cnt in range(281, 291):
        # for cnt in range(291, 301):

        # for cnt in range(301, 311):
        # for cnt in range(311, 321):
        # for cnt in range(321, 331):
        # for cnt in range(331, 341):
        # for cnt in range(341, 351):
        # for cnt in range(351, 361):
        # for cnt in range(361, 371):
        # for cnt in range(371, 381):
        # for cnt in range(381, 391):
        # for cnt in range(391, 401):
        raw_data = []
        # 50w
        for i in range(1, 250001):
            # for i in range(1, 10001):
            for j in range(1, 5):
                raw_data.append('SS%.4d%.8d,info,data0%d,%.2f' % (cnt, i, j, j - 0.25 + (random.random() * 0.5)))

        # sc.parallelize(raw_data).map(lambda x: (x.split(','))).foreach(lambda x: print(x))
        # sc.parallelize(rawData).foreach(lambda x: print(x.split(',').toList))
        sc.parallelize(raw_data) \
            .map(lambda x: (table, x.split(','))) \
            .saveAsNewAPIHadoopDataset(conf=conf, keyConverter=keyConv, valueConverter=valueConv)
        print("----------------> ", cnt)
        end = datetime.datetime.now()
        print(end - start)

    # sc.stop()
    print('============== end ===================')
