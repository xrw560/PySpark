#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:sgd.py
@time:2018/6/12 9:13
"""

from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession
from pyspark.mllib.regression import LabeledPoint, IsotonicRegression, IsotonicRegressionModel
from pyspark.mllib.util import MLUtils
from pyspark import SparkContext
import math

sc = SparkContext(appName="PythonIsotonicRegressionExample")


# $example on$
# Load and parse the data
def parsePoint(labeledData):
    return (labeledData.label, labeledData.features[0], 1.0)


data = MLUtils.loadLibSVMFile(sc, "file:///home/runisys/sample_isotonic_regression_libsvm_data.txt")

# Create label, feature, weight tuples from input data with weight set to default value 1.0.
parsedData = data.map(parsePoint)
print(parsedData.take(1))

# Split data into training (60%) and test (40%) sets.
training, test = parsedData.randomSplit([0.6, 0.4], 11)

# Create isotonic regression model from training data.
# Isotonic parameter defaults to true so it is only shown for demonstration
model = IsotonicRegression.train(training)

# Create tuples of predicted and real labels.
predictionAndLabel = test.map(lambda p: (model.predict(p[1]), p[0]))

# Calculate mean squared error between predicted and real labels.
meanSquaredError = predictionAndLabel.map(lambda pl: math.pow((pl[0] - pl[1]), 2)).mean()
print("Mean Squared Error = " + str(meanSquaredError))
