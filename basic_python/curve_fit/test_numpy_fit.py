#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:test_numpy_fit.py
@time:2018/7/11 17:16
@desc:多项式拟合范例：
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 17, 1)
y = np.array(
    [3.10323, 3.20646, 3.30969, 5.41292, 3.51615, 3.61938, 3.72261, 3.82584, 3.92907, 4.0323, 4.13553, 4.23876, 4.34199,
     4.44522, 4.54845, 4.65168])
z1 = np.polyfit(x, y, 2)  # 用2次多项式拟合

p1 = np.poly1d(z1)

print(p1)  # 在屏幕上打印拟合多项式
# yvals = p1(x)  # 也可以使用yvals=np.polyval(z1,x)
yvals = np.polyval(z1, x)  # 也可以使用yvals=np.polyval(z1,x)
print(type(yvals))
plot1 = plt.plot(x, y, '*', label='original values')
plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4)  # 指定legend的位置,读者可以自己help它的用法
plt.title('polyfitting')
plt.show()
plt.savefig('p1.png')
