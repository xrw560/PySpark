#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:demo2.py
@time:2018/8/8 19:44
@desc:多项logistic回归解决多分类问题
对于多分类问题，我们需要多项式logistic进行多分类胡桂。
这里我们用全部的iris数据集，即有3个类别。
多项式logistic与二项logistic回归类似，只是模型设置上把family参数设置成multinomial。
"""

from pyspark.sql import SparkSession, Row, functions
from pyspark.ml.linalg import Vectors
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml import Pipeline
from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer
from pyspark.ml.classification import LogisticRegression


def f(x):
    rel = {}
    rel['features'] = Vectors.dense(float(x[1]), float(x[2]), float(x[3]), float(x[4]))
    rel['label'] = str(x[5]).strip("\"")
    return rel


spark = SparkSession.builder.appName("logistic_regression").getOrCreate()

data = spark.sparkContext.textFile("iris.txt").map(lambda line: line.split(",")).map(lambda p: Row(**f(p))).toDF()

data.createOrReplaceTempView("iris")
# data.show()
df = spark.sql("select * from iris")
rel = df.rdd.map(lambda t: str(t[1]) + ":" + str(t[0])).collect()
# for item in rel:
#     print(item)

"""构建ML的pipeline"""
## 分别获取标签列和特征列，并进行了重命名
label_indexer = StringIndexer().setInputCol("label").setOutputCol("indexedLabel").fit(df)
feature_indexer = VectorIndexer().setInputCol("features").setOutputCol("indexedFeatures").fit(df)
"""把数据集分成训练集和测试集"""
training_data, test_data = df.randomSplit([0.7, 0.3])
mlr = LogisticRegression().setLabelCol("indexedLabel").setFeaturesCol("indexedFeatures").setMaxIter(10).setRegParam(0.3).setElasticNetParam(0.8) \
    .setFamily("multinomial")

# print("LogisticRegression parameters:\n" + lr.explainParams)
"""设置lebelConverter,目的是把预测的类别重新转成字符型"""
label_converter = IndexToString().setInputCol("prediction").setOutputCol("predictionLabel").setLabels(label_indexer.labels)
mlr_pipeline = Pipeline().setStages([label_indexer, feature_indexer, mlr, label_converter])
mlr_pipeline_model = mlr_pipeline.fit(training_data)
"""pipeline本质上是一个Estimator,当pipeline调用fit()的时候就产生了一个PipelineModel，本质上是一个Transformer。
然后这个PipelineModel就可以调用transform()来进行预测，生成一个新的DataFrame，即利用训练得到的模型对测试集进行验证。"""

mlr_predictions = mlr_pipeline_model.transform(test_data)
pre_rel = mlr_predictions.select("predictionLabel", "label", "features", "probability").collect()
for item in pre_rel:
    print(str(item['label']) + "," + str(item['features']) + "-->prob" + str(item['probability']) + ",predictedLabel " + str(item['predictionLabel']))

"""创建一个MulticlassClassificationEvaluator实例，用setter方法把预测分类的列名和真实分类的列名进行设置，然后计算预测准确率和错误率"""
evaluator = MulticlassClassificationEvaluator().setLabelCol("indexedLabel").setPredictionCol("prediction")
mlr_accuracy = evaluator.evaluate(mlr_predictions)
print("Test Error = " + str(1.0 - mlr_accuracy))

"""通过model获取训练的logistic模型。前面说过model是一个pipelineModel，因此可以通过调用它的stages来获取模型"""
mlr_model = mlr_pipeline_model.stages[2]
print("Coefficients: " + str(mlr_model.coefficientMatrix) + " Intercept: " + str(mlr_model.interceptVector) + " numClasses: " + str(mlr_model.numClasses) + " numFeatures: " + str(
    mlr_model.numFeatures))
spark.stop()
