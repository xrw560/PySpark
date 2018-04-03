# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:.py
@time:2018/3/28 15:09
"""
from pyspark import SparkConf, SparkContext, SQLContext
import json
import datetime
from pyspark.sql import DataFrameWriter
import pymysql
from pyspark.sql import functions as F


def split_key_value(key, value):
    value_split = value.split("\n")
    lst = []
    for v in value_split:
        lst.append((key, v))
    return lst


def dict_add(rdict, key, value):
    rdict[key] = value
    return rdict


def dict_del(rdict):
    del rdict['columnFamily']
    del rdict['timestamp']
    del rdict['type']
    rdict['value'] = float(rdict['value'])
    return rdict


if __name__ == '__main__':
    start = datetime.datetime.now()

    # =======================MySQL配置===============================
    url = "jdbc:mysql://192.168.0.179:3306/zn"
    mysql_table = "hbase_test02"
    mysql_properties = {"user": "root", "password": "root"}
    # ===============================================================

    sparkConf = SparkConf() \
        .setAppName('read_from_hbase')
    sc = SparkContext(conf=sparkConf)
    sc.setLogLevel('WARN')
    sqlContext = SQLContext(sc)

    host = 'slave1,slave2,slave3'
    table = 'z_spark_50w'
    # table = 'z_spark_500w'
    # table = 'z_spark_1000w'
    # table = 'z_spark_5000w'
    inputFormatClass = 'org.apache.hadoop.hbase.mapreduce.TableInputFormat'
    keyClass = 'org.apache.hadoop.hbase.io.ImmutableBytesWritable'
    valueClass = 'org.apache.hadoop.hbase.client.Result'
    conf = {'hbase.zookeeper.quorum': host,
            'hbase.mapreduce.inputtable': table,
            # 'hbase.mapreduce.scan.column.family': 'info',
            # 'hbase.mapreduce.scan.columns': 'info:data01',
            # 'hbase.mapreduce.scan.row.start': 'ss0001',
            # 'hbase.mapreduce.scan.row.stop': 'ss0010'
            }
    keyConv = 'org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter'
    valueConv = 'org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter'

    hbase_rdd = sc.newAPIHadoopRDD(inputFormatClass, keyClass, valueClass, keyConverter=keyConv,
                                   valueConverter=valueConv, conf=conf)
    values__take = hbase_rdd.values().take(1)
    for x in values__take:
        print(x)
    end = datetime.datetime.now()
    print('-----newAPIHadoopRDD------- time :', end - start)

    # values = hbase_rdd.values()
    # n_map = values.flatMap(lambda x: x.split("\n")).map(lambda x: json.loads(x))
    # data_frame = sqlContext.read.json(n_map)
    # data_frame.show()
    # data_frame.printSchema()

    values = hbase_rdd.values()
    n_map = values.flatMap(lambda x: x.split("\n")).map(lambda x: json.loads(x)).map(lambda x: dict_del(x))
    data_frame = sqlContext.read.json(n_map)



    # data_frame.show()
    # data_frame.printSchema()
    # print('count', data_frame.count())
    # print('avg', data_frame.groupBy('qualifier').avg("value").collect())
    # print('avg', data_frame.groupBy('qualifier')
    #       .agg(F.min(data_frame.value),
    #            F.max(data_frame.value),
    #            F.avg(data_frame.value),
    #            F.sum(data_frame.value),
    #            F.count(data_frame.value)).collect())
    # df_avg1 = data_frame.groupBy('qualifier').avg("value")

    # lookup = sqlContext.createDataFrame([(1, "foo"), (2, "bar")], ("k", "v"))
    # lookup.show()
    # lookup.printSchema()

    # 写入到mysql中
    # df_avg1.withColumnRenamed('qualifier', 'column').withColumnRenamed('avg(value)', 'value') \
    #     .write.jdbc(url, mysql_table, 'append', mysql_properties)

    result = data_frame.groupBy('qualifier') \
        .agg(F.min(data_frame.value),
             F.max(data_frame.value),
             F.avg(data_frame.value),
             F.sum(data_frame.value),
             F.count(data_frame.value))
    end = datetime.datetime.now()
    print('------------ time :', end - start)
    print('-------mysql-----------')
    result.write.jdbc(url, mysql_table, 'append', mysql_properties)

    # n_map = hbase_rdd.flatMap(lambda x: split_key_value(x[0], x[1])).map(lambda x: (x[0], json.loads(x[1]))).count()
    # print(n_map)

    # n_map = hbase_rdd.flatMap(lambda x: split_key_value(x[0], x[1])).map(lambda x: (x[0], json.loads(x[1]))) \
    #     .map(lambda x: dict_add(x[1], 'key', x[0])).foreach(lambda x: print(x))
    # n_map = hbase_rdd.flatMap(lambda x: split_key_value(x[0], x[1])).map(lambda x: (x[0], json.loads(x[1]))) \
    #     .map(lambda x: dict_add(x[1], 'key', x[0]))
    # data_frame = sqlContext.read.json(n_map)
    # data_frame.show()
    # data_frame.printSchema()

    # data_frame = sqlContext.read.json(n_map[1])
    # data_frame.show()
    # data_frame.printSchema()

    # values.foreach(lambda x: print(json.loads(x), type(json.loads(x))))
    # values.map(lambda x: json.dumps(x)).map(lambda x: json.loads(x)).foreach(lambda x: print(type(x)))
    # json_data = values.map(lambda x: json.dumps(x)).collect()
    # read_json = sqlContext.read.json(json_data)
    # read_json.show()
    # read_json.printSchema()

    # print(type(json_loads))
    # json_str = json.loads(values)
    # print(json_str)
    # data2 = json.dumps(json_str)
    # print(data2)
    # values.map(lambda x: json.loads(values)).foreach(lambda x: print(x))
    # hbase_rdd.foreach(lambda x: print(repr(x[1])))
    # tmp_data = hbase_rdd \
    #     .map(lambda x: json.dumps(x[1]))
    # tmp_data.foreach(lambda x: print(x))
    # read_json = sqlContext.read.json(tmp_data)
    # read_json.show()
    # read_json.printSchema()
    # print(read_json.count())
    # tmp_data.foreach(lambda x: print(x))
    # frame = sqlContext.createDataFrame(hbase_data)
    # print(frame.count)
    # hbase_rdd.foreach(lambda x: print(type(x[1])))
    # count = hbase_rdd.count()
    # print("-------------> " + str(count))
    # hbase_rdd.cache()
    # output = hbase_rdd.collect()
    #
    # for (k, v) in output:
    #     print(k, v)

    sc.stop()

    end = datetime.datetime.now()
    print('------------ time :', end - start)
