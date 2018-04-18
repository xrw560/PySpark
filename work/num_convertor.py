#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:num_convertor.py
@time:2018/4/16 15:18
"""
'''
str_num的类型必需是可被str转换的整数，如：‘111’、‘123’
16进制中str_num可以是‘123456789abcdef’，且必须是0-9及a-f之间
8进制中str_num可以是‘1234567’，且必须是0-7之间的数
'''


def hex2bin(str_num):
    """十六进制to二进制"""
    num = int(str_num, 16)  # 将16进制转换为10进行
    bit = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)  # 10进制转换2进制，使用除2取余
        bit.append(str(rem))  # 默认加入列表是filo（先进后出）方式
    return ''.join(bit[::-1])  # 需要反向排列，即为正确的2进制


def dec2bin(str_num):
    """十进制to二进制"""
    num = int(str_num, 10)
    bit = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        bit.append(str(rem))
    return ''.join(bit[::-1])


def oct2bin(str_num):
    """八进制to二进制"""
    num = int(str_num, 8)
    bit = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        bit.append(str(rem))
    return ''.join(bit[::-1])
