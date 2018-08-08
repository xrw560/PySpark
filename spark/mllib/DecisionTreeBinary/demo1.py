#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:demo1.py
@time:2018/8/8 20:49
@desc:决策树分类
"""

from pyspark.sql import SparkSession, Row, functions
from pyspark.ml.linalg import Vectors
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml import Pipeline
from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer
from pyspark.ml.classification import LogisticRegression

"""2 读取数据，简要分析"""


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

"""3 进一步处理特征和标签，以及数据分组"""
## 分别获取标签列和特征列，并进行了重命名
label_indexer = StringIndexer().setInputCol("label").setOutputCol("indexedLabel").fit(df)
feature_indexer = VectorIndexer().setInputCol("features").setOutputCol("indexedFeatures").setMaxCategories(4).fit(df)

# print("LogisticRegression parameters:\n" + lr.explainParams)
"""设置lebelConverter,目的是把预测的类别重新转成字符型"""
label_converter = IndexToString().setInputCol("prediction").setOutputCol("predictionLabel").setLabels(label_indexer.labels)

"""把数据集分成训练集和测试集"""
training_data, test_data = df.randomSplit([0.7, 0.3])

"""4 构建决策树分类模型"""
# 导入需要的包
from pyspark.ml.classification import DecisionTreeClassificationModel, DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# 训练决策树模型，这里我们可以通过setter的方法来设置决策树的参数，也可以用ParamMap来设置(具体的可以查看spark mllib官网)。
# 具体的可以设置的参数可以通过explainParams()来获取
dt_classifier = DecisionTreeClassifier().setLabelCol("indexedLabel").setFeaturesCol("indexedFeatures")
# 在pipeline中进行设置
pipeline_classifier = Pipeline().setStages([label_indexer, feature_indexer, dt_classifier, label_converter])
# 进行决策树模型
model_classifier = pipeline_classifier.fit(training_data)
# 进行预测
predictions_classifier = model_classifier.transform(test_data)
# 查看部分预测的结果
predictions_classifier.select("predictionLabel", "label", "features").show(20)

"""5 评估决策树分类模型"""
evaluator_classifier = MulticlassClassificationEvaluator().setLabelCol("indexedLabel").setPredictionCol("prediction").setMetricName("accuracy")
accuracy = evaluator_classifier.evaluate(predictions_classifier)
print("Test Error: ", str(1.0 - accuracy))
tree_model_classifier = model_classifier.stages[2]
print("Learned classification tree model:\n", str(tree_model_classifier.toDebugString))
spark.stop()
