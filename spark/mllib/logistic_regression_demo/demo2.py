#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:demo2.py
@time:2018/8/8 19:44
@desc:
"""

from pyspark.sql import SparkSession, Row, functions
from pyspark.ml.linalg import Vectors, Vector
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml import Pipeline
from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer, HashingTF, Tokenizer
from pyspark.ml.classification import LogisticRegression, LogisticRegressionModel, BinaryLogisticRegressionSummary


def f(x):
    rel = {}
    rel['features'] = Vectors.dense(float(x[1]), float(x[2]), float(x[3]), float(x[4]))
    rel['label'] = str(x[5]).strip("\"")
    return rel


spark = SparkSession.builder.appName("logistic_regression").getOrCreate()

data = spark.sparkContext.textFile("iris.txt").map(lambda line: line.split(",")).map(lambda p: Row(**f(p))).toDF()

data.createOrReplaceTempView("iris")
# data.show()
df = spark.sql("select * from iris where label !='setosa'")
rel = df.rdd.map(lambda t: str(t[1]) + ":" + str(t[0])).collect()
# for item in rel:
#     print(item)

"""构建ML的pipeline"""
label_indexer = StringIndexer().setInputCol("label").setOutputCol("indexedLabel").fit(df)
feature_indexer = VectorIndexer().setInputCol("features").setOutputCol("indexedFeatures").fit(df)
"""把数据集分成训练集和测试集"""
training_data, test_data = df.randomSplit([0.7, 0.3])
lr = LogisticRegression().setLabelCol("indexedLabel").setFeaturesCol("indexedFeatures").setMaxIter(10).setRegParam(0.3).setElasticNetParam(0.8)

# print("LogisticRegression parameters:\n" + lr.explainParams)
"""设置lebelConverter,目的是把预测的类别重新转成字符型"""
label_converter = IndexToString().setInputCol("prediction").setOutputCol("predictionLabel").setLabels(label_indexer.labels)
lr_pipeline = Pipeline().setStages([label_indexer, feature_indexer, lr, label_converter])
lr_pipeline_model = lr_pipeline.fit(training_data)
"""pipeline本质上是一个Estimator,当pipeline调用fit()的时候就产生了一个PipelineModel，本质上是一个Transformer。
然后这个PipelineModel就可以调用transform()来进行预测，生成一个新的DataFrame，即利用训练得到的模型对测试集进行验证。"""

lr_predictions = lr_pipeline_model.transform(test_data)
pre_rel = lr_predictions.select("predictionLabel", "label", "features", "probability").collect()
for item in pre_rel:
    print(str(item['label']) + "," + str(item['features']) + "-->prob" + str(item['probability']) + ",predictedLabel " + str(item['predictionLabel']))

"""创建一个MulticlassClassificationEvaluator实例，用setter方法把预测分类的列名和真实分类的列名进行设置，然后计算预测准确率和错误率"""
evaluator = MulticlassClassificationEvaluator().setLabelCol("indexedLabel").setPredictionCol("prediction")
lr_accuracy = evaluator.evaluate(lr_predictions)
print("Test Error = " + str(1.0 - lr_accuracy))

"""通过model获取训练的logistic模型。前面说过model是一个pipelineModel，因此可以通过调用它的stages来获取模型"""
lr_model = lr_pipeline_model.stages[2]
print("Coefficients: " + str(lr_model.coefficients) + " Intercept: " + str(lr_model.intercept) + " numClasses: " + str(lr_model.numClasses) + " numFeatures: " + str(
    lr_model.numFeatures))

training_summary = lr_model.summary
objective_history = training_summary.objectiveHistory
for item in objective_history:
    print(item)

print("areaUnderROC: ", training_summary.areaUnderROC)  # 通过获取ROC，可以判断模型的好坏
"""通过最大化fMeasure来选取最合适的阈值，其中fMeasure是一个综合了召回率和准确率的指标，通过最大化fMeasure，可以选取到用来分类的最合适的阈值"""
f_measure = training_summary.fMeasureByThreshold
max_f_measure = f_measure.select(functions.max("F-Measure")).head()[0]
print("maxFMeasure: ", max_f_measure)
best_threshold = f_measure.where(f_measure["F-Measure"] == max_f_measure).select("threshold").head()[0]
print("best_threshold: ", best_threshold)
lr.setThreshold(best_threshold)
spark.stop()
