#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:config_test.py
@time:2018/7/13 11:53
@desc:
"""

import logging.config

# 读取日志配置文件内容
logging.config.fileConfig('logging.conf')
# 创建一个日志器logger
logger = logging.getLogger('simpleExample')
# 日志输出
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
