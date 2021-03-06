#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:demo1.py
@time:2018/4/16 14:35
"""
import hbase_util
import json
import data_prepare as dp
import data_compute_util as dcu
import dict_util
import datetime
from dao import posture_dao
import common_util
import sys
import time


def filter_data(rdict):
    """
    有效性过滤
    @param rdict:
    @return:
    """
    if (rdict is not None
            and rdict.get('A1') is not None
            and rdict.get('A1')[0:4] == '0110'  # 高4位为6(0110)
            and rdict.get('A6') is not None
            and int(rdict.get('A6')) == 0):
        return True
    else:
        return False


if __name__ == '__main__':
    start = datetime.datetime.now()
    print("开始时间：", start)
    update_time = start.strftime("%Y%m%d%H%M%S%f")

    last_update_time = posture_dao.get_last_update()  # 获取历史最新的融合数据

    sc = common_util.create_spark_context("demo1")

    hbase_rdd = hbase_util.get_hbase_rdd(sc, table='posture')
    print("------> Partition数目：", hbase_rdd.values().getNumPartitions())
    print(hbase_rdd.count())
    values = (hbase_rdd.values())  # .repartition(24))  # standalone中共12个core，repartition后，任务为24个
    for x in hbase_rdd.collect():
        print(x)
    # print('hbase_rdd count --> ', values.count())
    # init_rdd = (values.flatMap(lambda x: x.split("\n"))  # 压平，压扁，把数组数据切分为多个，1对多
    #             .map(lambda x: json.loads(x))  # 将str类型的数据转为dict
    #             .map(lambda x: dp.init_hbase_data(x))  # {'row':rowkey,'A1':0.01} 或者{'row':rowkey,'A2':0.02}
    #             .map(lambda x: (x.get('row'), x))  # 转成元组，(rowkey,{'row':rowkey,'A1':0.01})
    #             .reduceByKey(dict_util.dict_concat)  # (rowkey,{'row':rowkey,'A1':0.01,'A2':0.02})
    #             .map(lambda x: x[1]))  # {'row':rowkey,'A1':0.01,'A2':0.02}
    # # 过滤出有效数据
    # valid_rdd = init_rdd.filter(filter_data).cache()  # 缓存过滤后的有效数据
    # if valid_rdd.isEmpty():  # 若本次计算没有更新的数据，退出
    #     print("============== no update data ===============")
    #     sys.exit(1)
    #
    # # 滚动角计算
    # roll_filter_rdd = (valid_rdd
    #                    .filter(lambda x: not x.get('A2') is None)
    #                    .map(lambda x: float(x.get('A2')))  # float()为了下一步的最小，最大，均值计算
    #                    .cache())  # 下一步需要重用该RDD
    # # roll:滚动角；pitch:俯仰角；deviation：偏航角
    # merge_roll_mean = roll_mean = roll_filter_rdd.mean()  # a = b = c : 把c的值给a,b
    # merge_roll_count = roll_count = roll_filter_rdd.count()
    # merge_roll_max = roll_max = roll_filter_rdd.max()
    # merge_roll_min = roll_min = roll_filter_rdd.min()
    #
    # # 俯仰角计算
    # pitch_filter_rdd = valid_rdd.filter(lambda x: not x.get('A3') is None).map(lambda x: float(x.get('A3'))).cache()
    # merge_pitch_mean = pitch_mean = pitch_filter_rdd.mean()
    # merge_pitch_count = pitch_count = pitch_filter_rdd.count()
    # merge_pitch_max = pitch_max = pitch_filter_rdd.max()
    # merge_pitch_min = pitch_min = pitch_filter_rdd.min()
    #
    # # 偏航计算
    # deviation_filter_rdd = valid_rdd.filter(lambda x: not x.get('A4') is None and not x.get(
    #     'A5') is None).map(lambda x: float(x.get('A4')) - float(x.get('A5'))).cache()
    # merge_deviation_mean = deviation_mean = deviation_filter_rdd.mean()
    # merge_deviation_count = deviation_count = deviation_filter_rdd.count()
    # merge_deviation_max = deviation_max = deviation_filter_rdd.max()
    # merge_deviation_min = deviation_min = deviation_filter_rdd.min()
    #
    # # print("滚动角均值: " + str(roll_mean) + " 俯仰角均值：" + str(pitch_mean)
    # #       + " 统计(偏航角偏执量-偏航角)的均值：" + str(deviation_mean))
    # # print("滚动角最大值: " + str(roll_max) + " 俯仰角最大值：" + str(pitch_max)
    # #       + " 统计(偏航角偏执量-偏航角)的最大值：" + str(deviation_max))
    # # print("滚动角最小值: " + str(roll_min) + " 俯仰角最小值：" + str(pitch_min)
    # #       + " 统计(偏航角偏执量-偏航角)的最小值：" + str(deviation_min))
    # # print("滚动角数量: " + str(roll_count) + " 俯仰角数量：" + str(pitch_count)
    # #       + " 统计(偏航角偏执量-偏航角)的数量：" + str(deviation_count))
    #
    # # 融合
    # if last_update_time:  # 存在历史融合数据，则与本次delta时间内的计算结果进行融合
    #     print(" -------------------------> 融合 <---------------------------------")
    #     merge_roll_max = max(merge_roll_max, last_update_time.get('merge_roll_max'))
    #     merge_roll_min = min(merge_roll_min, last_update_time.get('merge_roll_min'))
    #     merge_roll_mean = dcu.get_mean_value(last_update_time.get('merge_roll_mean'),
    #                                          last_update_time.get('merge_roll_count'), roll_mean, roll_count)
    #     merge_roll_count = last_update_time.get('merge_roll_count') + roll_count
    #
    #     merge_pitch_max = max(merge_pitch_max, last_update_time.get('merge_pitch_max'))
    #     merge_pitch_min = min(merge_pitch_min, last_update_time.get('merge_pitch_min'))
    #     merge_pitch_mean = dcu.get_mean_value(last_update_time.get('merge_pitch_mean'),
    #                                           last_update_time.get('merge_pitch_count'), pitch_mean, pitch_count)
    #     merge_pitch_count = last_update_time.get('merge_pitch_count') + pitch_count
    #
    #     merge_deviation_max = max(merge_deviation_max, last_update_time.get('merge_deviation_max'))
    #     merge_deviation_min = min(merge_deviation_min, last_update_time.get('merge_deviation_min'))
    #     merge_deviation_mean = dcu.get_mean_value(last_update_time.get('merge_deviation_mean'),
    #                                               last_update_time.get('merge_deviation_count'),
    #                                               deviation_mean, deviation_count)
    #     merge_deviation_count = last_update_time.get('merge_deviation_count') + deviation_count
    #
    # # 打分，使用的是融合后的数据进行打分
    # roll_score = dcu.get_roll_score(merge_roll_mean)
    # pitch_score = dcu.get_pitch_score(merge_pitch_mean)
    # deviation_score = dcu.get_deviation_score(merge_deviation_mean)
    # total_score = dcu.get_total_score(roll_score, pitch_score, deviation_score)
    # # print("滚动角分数: " + str(roll_score) + " 俯仰角分数：" + str(pitch_score)
    # #       + " 统计偏航分数：" + str(deviation_score) + " 项目分数：" + str(total_score))
    #
    # # 插入数据到数据库
    # values = list()
    # values.append(
    #     (update_time, roll_max, roll_min, roll_mean, roll_count, pitch_max, pitch_min, pitch_mean, pitch_count,
    #      deviation_max, deviation_min, deviation_mean, deviation_count, merge_roll_max, merge_roll_min, merge_roll_mean,
    #      merge_roll_count, merge_pitch_max, merge_pitch_min, merge_pitch_mean, merge_pitch_count, merge_deviation_max,
    #      merge_deviation_min, merge_deviation_mean, merge_deviation_count, total_score))
    # posture_dao.insert_stat_data_with_merge_data(values)

    # 统计运行时间
    end = datetime.datetime.now()
    print("结束时间：", end)
    print("运行时间：", end - start)

    # time.sleep(2000)
