#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:test_scipy_optimize.py
@time:2018/7/11 17:07
@desc:指定函数拟合
"""
# 使用非线性最小二乘法拟合
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# 用指数形式来拟合
x = np.arange(1, 17, 1)
print(0.00000000000000000002 * x ** 2 + 0.10323 * x + 3)
y = np.array(
    [3.10323, 3.20646, 1.30969, 5.41292, 3.51615, 3.61938, 3.72261, 3.82584, 3.92907, 4.0323, 4.13553, 4.23876, 4.34199,
     4.44522, 4.54845, 4.65168])


# def func(x, a, b):
#     return a * np.exp(b / x)


def func(x, a, b, c):
    return a * x ** 2 + b * x + c


popt, pcov = curve_fit(func, x, y)
print(popt)
# yvals = func(x, popt[0], popt[1], popt[2])
yvals = func(x, *popt)
# a = popt[0]  # popt里面是拟合系数，读者可以自己help其用法
# b = popt[1]
# yvals = func(x, a, b)
# yvals = func(x, a, b)
plot1 = plt.plot(x, y, '*', label='original values')
plot2 = plt.plot(x, yvals, 'r', label='curve_fit values')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4)  # 指定legend的位置,读者可以自己help它的用法
plt.title('curve_fit')
plt.savefig('p2.png')  # 放在show()方法之前才可以保存有内容
plt.show()
