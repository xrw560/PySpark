#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:kmeans_demo1.py
@time:2018/7/27 19:24
@desc:
"""

from skimage import io
from sklearn.cluster import KMeans
import numpy as np

image = io.imread('test2.jpg')
# io.imshow(image)
# io.show()

rows = image.shape[0]
cols = image.shape[1]
print(rows, cols)

image = image.reshape(image.shape[0] * image.shape[1], 3)

kmeans = KMeans(n_clusters=128, n_init=10, max_iter=200)
kmeans.fit(image)
clusters = np.asarray(kmeans.cluster_centers_, dtype=np.uint8)
print(kmeans.cluster_centers_.shape)
labels = np.asarray(kmeans.labels_, dtype=np.uint8)
print(labels.shape)
labels = labels.reshape(rows, cols)

print(clusters.shape)  # 128,3
np.save('codebook_test.npy', clusters)
io.imsave('compressed_test.jpg', labels)
