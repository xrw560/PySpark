#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:demo1.py
@time:2018/4/16 14:35
"""
from pyspark import SparkConf, SparkContext, SQLContext
from work.hbase_util import HBaseUtil
from work import num_convertor as nc
import json
from work import data_prepare as dp
from work import score_compute_util as scu
from work import str_util
from work import dict_util
import datetime
from pyspark.sql import functions as F

if __name__ == '__main__':
    start = datetime.datetime.now()
    print("开始时间：", start)
    sparkConf = SparkConf() \
        .setAppName('demo1')
    sc = SparkContext(conf=sparkConf)
    sc.setLogLevel('WARN')
    sqlContext = SQLContext(sc)

    # 读取hbase数据
    hbase_rdd = sc.newAPIHadoopRDD(HBaseUtil.inputFormatClass,
                                   HBaseUtil.keyClass,
                                   HBaseUtil.valueClass,
                                   keyConverter=HBaseUtil.keyConv,
                                   valueConverter=HBaseUtil.valueConv,
                                   conf=HBaseUtil.conf)
    values = hbase_rdd.values()
    init_rdd = values.flatMap(lambda x: x.split("\n")).map(lambda x: json.loads(x)) \
        .map(lambda x: dp.dict_del(x))
    data_frame = sqlContext.read.json(init_rdd)
    # data_frame.show()
    # data_frame.printSchema()

    result = data_frame.groupBy('qualifier').agg(F.min(data_frame.value),
                                                 F.max(data_frame.value),
                                                 F.avg(data_frame.value),
                                                 F.sum(data_frame.value),
                                                 F.count(data_frame.value)).collect()
    for x in result:
        print(x)

    # valid_rdd = init_rdd.filter(
    #     lambda x: x.get('A1')[0:4] == '0110' and int(x.get('A6')) == 0).cache()
    # roll_filter_rdd = valid_rdd.filter(lambda x: not x.get('A2') is None).map(lambda x: float(x.get('A2'))).cache()
    # roll_mean = roll_filter_rdd.mean()
    # roll_count = roll_filter_rdd.count()
    # roll_max = roll_filter_rdd.max()
    # roll_min = roll_filter_rdd.min()
    #
    # pitch_filter_rdd = valid_rdd.filter(lambda x: not x.get('A3') is None).map(lambda x: float(x.get('A3'))).cache()
    # pitch_mean = pitch_filter_rdd.mean()
    # pitch_count = pitch_filter_rdd.count()
    # pitch_max = pitch_filter_rdd.max()
    # pitch_min = pitch_filter_rdd.min()
    #
    # deviation_filter_rdd = valid_rdd.filter(lambda x: not x.get('A4') is None and not x.get(
    #     'A5') is None).map(lambda x: float(x.get('A4')) - float(x.get('A5'))).cache()
    # deviation_mean = deviation_filter_rdd.mean()
    # deviation_count = deviation_filter_rdd.count()
    # deviation_max = deviation_filter_rdd.max()
    # deviation_min = deviation_filter_rdd.min()
    #
    # print("滚动角均值: " + str(roll_mean) + " 俯仰角均值：" + str(pitch_mean)
    #       + " 统计(偏航角偏执量-偏航角)的均值：" + str(deviation_mean))
    # print("滚动角最大值: " + str(roll_max) + " 俯仰角最大值：" + str(pitch_max)
    #       + " 统计(偏航角偏执量-偏航角)的最大值：" + str(deviation_max))
    # print("滚动角最小值: " + str(roll_min) + " 俯仰角最小值：" + str(pitch_min)
    #       + " 统计(偏航角偏执量-偏航角)的最小值：" + str(deviation_min))
    # print("滚动角数量: " + str(roll_count) + " 俯仰角数量：" + str(pitch_count)
    #       + " 统计(偏航角偏执量-偏航角)的数量：" + str(deviation_count))
    #
    # roll_score = scu.get_roll_score(roll_mean)
    # pitch_score = scu.get_pitch_score(pitch_mean)
    # deviation_score = scu.get_deviation_score(deviation_mean)
    # total_score = scu.get_total_score(roll_score, pitch_score, deviation_score)
    # print("滚动角分数: " + str(roll_score) + " 俯仰角分数：" + str(pitch_score)
    #       + " 统计偏航分数：" + str(deviation_score) + " 项目分数：" + str(total_score))
    end = datetime.datetime.now()
    print("结束时间：", end)
    print("运行时间：", end - start)
