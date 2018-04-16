#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
    如何安装Python中第三方提供的库(模块)
    - pip 命令进行安装
        1. 在线安装
            pip install [第三方包的名称]
        2. 离线安装
            将第三方包下载下来()
                在https://www.lfd.uci.edu/~gohlke/pythonlibs/中搜索mysql
                找到MySQL_python‑1.2.5‑cp27‑none‑win_amd64.whl，下载下来
            pip install xxx.whl

    mysql模块
        - mysql-python对应Python2
        - pymysql对应Python3(资料：https://www.cnblogs.com/JayeHe/p/7518222.html)


    流程：
        -1. 从HDFS读取数据
        -2. 分析(词频统计，TopKey)
        -3. 数据插入到数据库中
"""
# 导入模块 pyspark
from pyspark import SparkConf, SparkContext
# 导入系统模块
import os
import time

if __name__ == '__main__':

    # 设置SPARK_HOME环境变量, 非常重要, 如果没有设置的话,SparkApplication运行不了
    os.environ['SPARK_HOME'] = 'E:/spark-1.6.1-bin-2.5.0-cdh5.3.6'

    # HADOOP在Windows的兼容性问题
    os.environ['HADOOP_HOME'] = 'G:/OnlinePySparkCourse/pyspark-project/winuntil'

    # Create SparkConf
    sparkConf = SparkConf() \
        .setAppName('Python Spark WordCount') \
        .setMaster('local[2]')

    # Create SparkContext
    """
        在使用pyspark编程运行程序时,依赖于py4j模块，为什么？？？？
        由于在运行的时候，SparkContext Python API创建的对象 通过 py4j(python for java)转换
    为JavaSparkContext，然后调度Spark Application.
    """
    sc = SparkContext(conf=sparkConf)
    # 设置日志级别
    # sc.setLogLevel('WARN')

    """
        创建RDD
            方式一：从本地集合进行并行化创建
            方式二：从外部文件系统读取数据（HDFS，Local）
    """
    # # 第一种方式：从集合并行化创建RDD
    # # 列表list
    # datas = ['hadoop spark', 'spark hive spark sql', 'spark hadoop sql sql spark']
    # # Create RDD
    # rdd = sc.parallelize(datas)

    # 第二种方式：从HDFS分布式文件系统读取数据，创建RDD
    """
        需要将HDFS Client 配置文件当到 ${SPARK_HOME}/conf 下面，以便程序运行读取信息
    """
    rdd = sc.textFile("/datas/wc.input")

    # 测试, 获取总数count及第一条数据
    print(rdd.count())

    print(rdd.first())

    # ===============================================================
    # 词频统计，针对SCALA编程 flatMap\map\reduceByKey
    word_count_rdd = rdd \
        .flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)
    # output
    for x in word_count_rdd.collect():
        print(x[0] + ", " + str(x[1]))

    # Save Result To HDFS
    # word_count_rdd.saveAsTextFile("/datas/pyspark-wc-output")

    # =============================================================
    # 获取词频出现次数最多的单词，前三个单词
    sort_rdd = word_count_rdd \
        .map(lambda word, count: (count, word)) \
        .sortByKey(ascending=False)
    # output
    for x in sort_rdd.take(3):
        print(x[1] + ", " + str(x[0]))

    # =============================================================
    # 使用RDD#top进行获取topKey
    top_rdd = word_count_rdd \
        .top(3, key=lambda word, count: count)
    # 输出方式一：打印在控制台
    for (top_word, top_count) in top_rdd:
        print("%s: %i" % (top_word, top_count))

    # 输出方式二：保存数据到MySQL数据库表中
    """
        需要安装MySQL-Python包，此处使用Anaconda自带的命令行
            -1，检查是否安装了MySQL的Python模块
                conda list MySQL-python
            -2, 使用conda进行安装MySQL-Python模块
                conda install MySQL-python
    """
    # 导入模块
    import MySQLdb

    # 创建连接
    conn = MySQLdb.connect(host='192.168.0.190', user='root', password='root', port=3306)
    # 游标的概念，通过游标操作数据库
    cur = conn.cursor()

    # 如果表存在的话，进行删除
    # cur.execute('DROP TABLE IF EXISTS test.tb_word_count')
    # 创建表
    # cur.execute('CREATE TABLE test.tb_word_count(word VARCHAR(255), count INT)')

    # 插入数据 第一种方式
    # for (top_word, top_count) in top_rdd:
    #     insert_sql = "INSERT INTO test.tb_word_count VALUES('" + str(top_word) + "'," + str(top_count) + ")"
    #     cur.execute(insert_sql)

    # 插入数据 第二种方式 防止SQL注入
    # for (top_word, top_count) in top_rdd:
    #     insert_sql = "INSERT INTO test.tb_word_count VALUES(%s, %s)"
    #     cur.execute(insert_sql, (str(top_word), str(top_count)))

    # 插入数据 第三种方式 批量插入
    insert_sql = "INSERT INTO test.tb_word_count VALUES(%s, %s)"
    values = []
    for (top_word, top_count) in top_rdd:
        values.append((str(top_word), str(top_count)))
    cur.executemany(insert_sql, values)

    # 提交
    conn.commit()

    # 关闭游标和连接
    cur.close()
    conn.close()

    # WEB UI 4040, 让线程休眠一段时间
    time.sleep(100000)

    # SparkContext Stop
    sc.stop()
