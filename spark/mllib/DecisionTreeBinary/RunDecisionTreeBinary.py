#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:RunDecisionTreeBinary.py
@time:2018/4/27 14:54
"""
from pyspark import SparkConf, SparkContext
import numpy as np
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.evaluation import BinaryClassificationMetrics
from time import time
from pyspark.mllib.tree import DecisionTree
import sys
import pandas as pd
import matplotlib.pyplot as plt


def set_path(sc):
    global Path
    if sc.master[0:5] == "local":
        Path = "file:/home/runisys/pythonCode/zn/spark/mllib/DecisionTreeBinary/"
    else:
        Path = "hdfs://master:9000/user/runisys/"


def extract_label(record):
    """
    提取label标签字段
    @param record: 单项数据
    @return: label
    """
    label = (record[-1])
    return float(label)


def extract_features(field, categories_map, feature_end):
    """
        提取数据的feature特征字段
    @param field: 每一项数据
    @param categories_map:  字典
    @param feature_end: 提取特征字段结尾
    @return:
    """
    # 提取分类特征字段
    category_idx = categories_map[field[3]]  # 网页分类转换为数值
    """
    初始化category_features,命令执行后会创建一个新的category_features list，其中的值都是0，
    list的大小是14，也就是0,0,0,0,0,0,0,0,0,0,0,0,0,0
    """
    category_features = np.zeros(len(categories_map))
    """
        # 设置list相对应的位置是1，其余位置默认是0,list的位置是从0开始的。
        若字段3的值是businesss，则经过字典转换后category_idx=2。
        所以会设置category_features list中从0算起第2个位置是1，结果是0,0,1,0,0,0,0,0,0,0,0,0,0,0
    """
    category_features[category_idx] = 1
    # 提取数值字段
    """
        读取文本文件，数据类型是string,所以每一个字段必须转换为float
        自第4个字段到feature_end字段，执行convert_float函数，转换为float
        feature_end是参数，调用extract_features时会传入参数len(r)-1，也就是倒数第二个字段
    """
    numerical_features = [convert_float(field) for field in field[4:feature_end]]
    # 返回“分类特征字段”+“数值特征字段”
    # 使用np.concatenate将list相加并返回
    return np.concatenate((category_features, numerical_features))


def convert_float(x):
    """
        文本文件中有很多字段数据没有数值，会以“？”代表。
    """
    return 0 if x == "?" else float(x)


def prepare_data(sc):
    # ------------------------1. 导入并转换数据--------------
    print("开始导入数据...")
    raw_data_with_header = sc.textFile(Path + "data/train.tsv")
    # tsv文件第一项数据是字段名而不是数据，删除第一项字段名
    header = raw_data_with_header.first()
    rawData = raw_data_with_header.filter(lambda x: x != header)
    rData = rawData.map(lambda x: x.replace("\"", ""))  # 删除双引号
    lines = rData.map(lambda x: x.split("\t"))  # 获取每一个字段
    print("共计：" + str(lines.count()) + "项")  # 显示数据项数
    # ------------------------2. 建立训练评估所需数据 RDD[LabeledPoint]-----------------
    # 建立categories_map网页分类字典
    categories_map = lines.map(lambda fields: fields[3]).distinct().zipWithIndex().collectAsMap()
    """
        进行Decision Tree的训练必须提供LabeledPoint格式的数据
        LabelPoint是由label与feature组成的。
    """
    labelpoint_rdd = lines.map(lambda r: LabeledPoint(
        extract_label(r),
        extract_features(r, categories_map, len(r) - 1)  # 因为最后一个字段是label，所以需要传入len(r)-1
    ))
    # print("labelpointRDD=", labelpointRDD.first(), "\n")

    # ------------------------3. 以随机方式将数据分为3个部分并且返回------------------------
    # 以randomSplit随机方式按照8:1:1的比例分割为3部分
    (train_data, validation_data, test_data) = labelpoint_rdd.randomSplit([8, 1, 1])
    print("将数据分为trainData:" + str(train_data.count()) + "    validationData:" + str(validation_data.count())
          + "    testData:" + str(test_data.count()))
    return train_data, validation_data, test_data, categories_map  # 返回数据


def evaluate_model(model, validation_data):
    """
    计算AUC
    @param model:模型
    @param validation_data:验证数据
    @return:
    """
    """
        使用model.predict进行预测，传入参数validation_data的features部分进行预测，预测结果存在score中
        建立score_and_labels，score(预测的结果)使用.zip方法结合validation_data验证数据的label标签字段
        使用BinaryClassificationMetrics传入参数score_and_labels建立二元分类metrics
        使用metrics的areaUnderROC方法计算AUC
    """
    score = model.predict(validation_data.map(lambda p: p.features))
    score_and_labels = score.zip(validation_data.map(lambda p: p.label))
    metrics = BinaryClassificationMetrics(score_and_labels)
    AUC = metrics.areaUnderROC
    return AUC


def train_evaluate_model(trainData, validation_data, impurity_param, max_depth_param, max_bins_param):
    """
    训练和评估，并且计算训练评估所需的时间
    """
    start_time = time()  # 记录开始时间
    """
        input:输入的训练数据
        numClasses:分类数目，=2是二元分类
        categoricalFeaturesInfo:设置分类特征字段信息
        impurity:决策树的impurity评估方法有两种方式:gini基尼系数、entropy熵
        maxDepth:决策树的最大深度
        maxBins:决策树每一个节点最大分支数
        
    """
    # 采用OneHotEncoding转换分类特征字段，所以设置为空的dict{}
    model = DecisionTree.trainClassifier(trainData, numClasses=2, categoricalFeaturesInfo={},
                                         impurity=impurity_param, maxDepth=max_depth_param, maxBins=max_bins_param)
    AUC = evaluate_model(model, validation_data)
    duration = time() - start_time
    print(" 训练评估：使用参数" + " impurity=" + str(impurity_param) + " maxDepth=" + str(max_depth_param)
          + " maxBins=" + str(max_bins_param) + " 所需时间=" + str(duration) + " 结果AUC=" + str(AUC))
    return AUC, duration, impurity_param, max_depth_param, max_bins_param, model


def eval_parameter(train_data, validation_data, eval_param, impurity_list, max_depth_list, max_bins_list):
    metrics = [train_evaluate_model(train_data, validation_data, impurity, max_depth, max_bins)
               for impurity in impurity_list
               for max_depth in max_depth_list
               for max_bins in max_bins_list]
    if eval_param == "impurity":
        index_list = impurity_list[:]
    elif eval_param == "max_depth":
        index_list = max_depth_list[:]
    elif eval_param == "max_bins":
        index_list = max_bins_list[:]
    """
        将metrics转换为pandas data frame
        metrics: 要转换的list
        index: 设置pandas data frame的索引
        columns: 设置pandas data frame的字段
    """
    df = pd.DataFrame(metrics, index=index_list,
                      columns=["AUC", "duration", "impurity", "max_depth", "max_bins", "model"])
    show_chart(df, eval_param, "AUC", "duration", 0.5, 0.7)


def show_chart(df, eval_param, bar_data, line_data, y_min, y_max):
    """
    使用matplot绘图，显示图表
    @param df: metrics产生的data frame
    @param eval_param:  此次评估的参数
    @param bar_data: 绘出barchart数据
    @param line_data: 绘出linechart数据
    @param y_min: y轴的打印区域
    @param y_max:
    @return:
    """
    """
        以data frame的bar_data进行绘图
        kind="bar": 图形是bar chart
        title=eval_param: 设置标题
        figsize: 设置图形的宽与高
        legend: 设置显示图标
        fontsize: 设置字号
    """
    ax = df[bar_data].plot(kind="bar", title=eval_param, figsize=(10, 6), legend=True, fontsize=12)
    ax.set_xlabel(eval_param, fontsize=12)  # 设置图形x轴是eval_param参数，并设置字号
    ax.set_ylabel(bar_data, fontsize=12)  # 设置图形y轴是bar_data参数
    ax.set_ylim([y_min, y_max])  # 设置y轴的打印区域
    ax2 = ax.twinx()  # 建立另外一个图形ax2
    """
        以ax2绘图
        df[line_data].values： 以dataframe的duration(运行时间)字段进行绘图
        linestyle='-': line chart的样式
        marker='o': line chart 数值点是圆形
        linewidth: line的宽度
        color='r': line的颜色
    """
    ax2.plot(df[line_data].values, linestyle="-", marker="o", linewidth=2.0, color="r")
    plt.show()  # 开始绘图


def parameter_eval(train_data, validation_data):
    print("----------评估impurity参数使用---------")
    eval_parameter(train_data, validation_data, "impurity",
                   impurity_list=["gini", "entropy"],
                   max_depth_list=[10],
                   max_bins_list=[10])
    print("---------评估max_depth参数使用----------")
    eval_parameter(train_data, validation_data, "max_depth",
                   impurity_list=["gini"],
                   max_depth_list=[3, 5, 10, 15, 20, 25],
                   max_bins_list=[10])
    print("---------评估max_depth参数使用----------")
    eval_parameter(train_data, validation_data, "max_bins",
                   impurity_list=["gini"],
                   max_depth_list=[10],
                   max_bins_list=[3, 5, 10, 50, 100, 200])


def eval_all_parameter(train_data, validation_data, impurity_list, max_depth_list, max_bins_list):
    metrics = [train_evaluate_model(train_data, validation_data, impurity, max_depth, max_bins)
               for impurity in impurity_list
               for max_depth in max_depth_list
               for max_bins in max_bins_list]
    smetrics = sorted(metrics, key=lambda k: k[0], reverse=True)
    best_parameter = smetrics[0]
    print("调校后最佳参数：impurity:" + str(best_parameter[2])
          + "    ,max_depth:" + str(best_parameter[3])
          + "    ,max_bins:" + str(best_parameter[4])
          + "    ,结果AUC= " + str(best_parameter[0]))
    return best_parameter[5]


def predict_data(sc, model, categories_map):
    """

    @param sc: SparkContext
    @param model: 之前训练完成的模型
    @param categories_map: 之前建立的网页分类字典
    @return:
    """
    print("开始导入数据....")
    raw_data_with_header = sc.textFile(Path + "data/test.tsv")
    header = raw_data_with_header.first()
    raw_data = raw_data_with_header.filter(lambda x: x != header)
    r_data = raw_data.map(lambda x: x.replace("\"", ""))
    lines = r_data.map(lambda x: x.split("\t"))
    print("共计：" + str(lines.count()) + "项")
    """
        因为希望能显示网页网址与预测网页的结果，所以编写data_rdd由网页网址 与特征字段组成。
        r[0]:网址
        test.tsv只有feature字段，没有label字段，所以传入参数len(r)而是不是len(r)-1
    """
    data_rdd = lines.map(lambda r: (r[0], extract_features(r, categories_map, len(r))))
    """
        原本label的值是0,1，后续我们希望能在程序中显示0和1所代表的意义。所以简历desc_dict字典，后续可用此字典转换预测结果
    """
    desc_dict = {
        0: "暂时性网页(ephemeral)",
        1: "长青网页(evergreen)"
    }
    for data in data_rdd.take(10):
        predict_result = model.predict(data[1])  # data[1]：feature特征字段。predict_result:预测结果
        print("网址：" + str(data[0]) + "\n"
              + "    ==>预测：" + str(predict_result)
              + " 说明：" + desc_dict[predict_result] + "\n")


def create_spark_context():
    spark_conf = SparkConf() \
        .setAppName("RunDecisionTreeBinary") \
        .set("spark.ui.showConsoleProgress", "false")
    sc = SparkContext(conf=spark_conf)
    print("master=" + sc.master)
    set_path(sc)
    return sc


if __name__ == "__main__":
    print("RunDecisionTreeBinary")
    sc = create_spark_context()
    print("========================数据准备阶段==========================")
    (train_data, validation_data, test_data, categories_map) = prepare_data(sc)
    train_data.persist()
    validation_data.persist()
    test_data.persist()
    print("========================训练评估阶段==========================")
    # 如果不输入参数，执行训练评估
    (AUC, duration, impurity_param, max_depth_param, max_bins_param, model) \
        = train_evaluate_model(train_data, validation_data, "entropy", 10, 200)
    # 如果输入参数"-e"，执行参数评估，以图表显示参数与准确率及训练时间的关系
    if (len(sys.argv) == 2) and (sys.argv[1] == "-e"):
        parameter_eval(train_data, validation_data)
    # 如果输入参数"-a"，所有参数训练评估找出最好的参数组合
    elif (len(sys.argv) == 2) and (sys.argv[1] == "-a"):
        print("----------所有参数训练评估找出最好的参数组合-------------")
        model = eval_all_parameter(train_data, validation_data,
                                   ["gini", "entropy"],
                                   [3, 5, 10, 15, 20, 25],
                                   [3, 5, 10, 50, 100, 200])
    print("==============测试阶段==================")
    auc = evaluate_model(model, test_data)
    print("使用test data测试最佳模型，结果AUC: " + str(auc))
    print("==============预测数据==================")
    predict_data(sc, model, categories_map)
    print(model.toDebugString())
