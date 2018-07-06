#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:datetime_test.py
@time:2018/7/5 14:18
@desc:
"""

import datetime

now = datetime.datetime.now()

end = now + datetime.timedelta(hours=839)

print((end - now).days)