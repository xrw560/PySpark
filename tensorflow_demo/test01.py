import tensorflow as tf

import tensorflow.examples.tutorials.mnist.input_data as input_data

mnist = input_data.read_data_sets('data/', one_hot=True)

trainimg = mnist.train.images
trainlable = mnist.train.labels
testimg = mnist.test.images
testlabel = mnist.test.labels
print('MNIST loaded')

