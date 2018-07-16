import tensorflow as tf


def add_layer(inputs, in_size, out_size, activation_function=None):
    weights = tf.Variable(tf.random_normal([in_size, out_size]))  # in_size:行; out_size列
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)  # 1行out_size列
    wx_plus_b = tf.matmul(inputs, weights) + biases
    if activation_function is None:  # 线性关系
        outputs = wx_plus_b
    else:
        outputs = activation_function(wx_plus_b)
    return outputs
