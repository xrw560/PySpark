#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:demo1.py
@time:2018/8/9 15:19
@desc:
"""
import configparser

cf = configparser.ConfigParser()
file_path = "../../resources/system.ini"
cf.read(file_path)
secs = cf.sections()
print("sections: ", secs)

opts = cf.options("db")
print("options: ", opts)
kvs = cf.items("db")
print("dbs: ", kvs)

#
db_host = cf.get("db", "db_host")
db_port = cf.get("db", "db_port")
db_user = cf.get("db", "db_user")
db_pass = cf.get("db", "db_pass")

threads = cf.getint("concurrent", "thread")
processors = cf.getint("concurrent", "processor")
print("db_host: ", db_host)
print("db_port: ", db_port)
print("db_user: ", db_user)
print("db_pass: ", db_pass)

print("thread: ", threads)
print("processor: ", processors)

# """modify cf """
# cf.set("test", "count", "1")
# cf.remove_option("test1", "name")
# cf.remove_section("test1")
# with open(file_path, "w+") as f:
#     cf.write(f)

"""add section / set option & key"""
# cf.add_section("test")
cf.set("test", "count", "1")  # 以字符串形式写入value
cf.add_section("test1")
cf.set("test1", "name", "aaa")

with open(file_path, "w+") as f:
    cf.write(f)

print(cf.getint("test", "count"))
