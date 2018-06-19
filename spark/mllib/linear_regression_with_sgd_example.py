#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:linear_regression_with_sgd_example.py
@time:2018/6/11 17:12
"""
from __future__ import print_function

from pyspark import SparkContext
# $example on$
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD, LinearRegressionModel

# $example off$

if __name__ == "__main__":
    sc = SparkContext(appName="PythonLinearRegressionWithSGDExample")


    # $example on$
    # Load and parse the data
    def parsePoint(line):
        values = [float(x) for x in line.replace(',', ' ').split(' ')]
        return LabeledPoint(values[0], [values[1] * values[1]])


    data = sc.textFile("file:///home/runisys/lpsa.data")
    parsedData = data.map(parsePoint)
    print("-->", parsedData.take(1))

    # Build the model
    # model = LinearRegressionWithSGD.train(parsedData, iterations=100, step=0.00000001)
    model = LinearRegressionWithSGD.train(parsedData, iterations=1000, step=0.1)
    print(model.weights)
    print(model.intercept)

    # Evaluate the model on training data
    valuesAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
    MSE = valuesAndPreds \
              .map(lambda vp: (vp[0] - vp[1]) ** 2) \
              .reduce(lambda x, y: x + y) / valuesAndPreds.count()
    print("Mean Squared Error = " + str(MSE))
    print(valuesAndPreds.collectAsMap())

    # Save and load model
    # model.save(sc, "target/tmp/pythonLinearRegressionWithSGDModel")
    # sameModel = LinearRegressionModel.load(sc, "target/tmp/pythonLinearRegressionWithSGDModel")
    # $example off$
