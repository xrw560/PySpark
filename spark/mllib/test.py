from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import os

spark = SparkSession.builder \
    .appName("test") \
    .getOrCreate()
sc = spark.sparkContext

path = "F:\github\mine\PySpark\data\Bike-Sharing-Dataset\hour_noheader.csv"
raw_data = sc.textFile(path)  # 加载数据
records = raw_data.map(lambda x: x.split(","))
num_data = raw_data.count()  # 得到总记录数
first = records.first()  # 得到第一行


# print(first)
# print(num_data)

def get_mapping(rdd, idx):
    return rdd.map(lambda fields: fields[idx]).distinct().zipWithIndex().collectAsMap()


# 以上定义了一个映射函数：首先将第idx列的特征值去重，然后对每个值使用zipWithIndex函数映射到一个唯一的索引，这样就组成了一个RDD的键值映射
# 键是变量，值是索引

# print(records.map(lambda fields: fields[2]).distinct().collect())
# 输出结果为['4', '1', '3', '2']
# 表明第三列(季节)只有4，1，3，2四种取值

# print("Mapping of first categorical fasture columns:%s" % get_mapping(records, 2))
# Mapping of first categorical fasture columns:{'2': 3, '1': 1, '3': 2, '4': 0}
# 将4,1,3,2映射到0,1,2,3

mapping = [get_mapping(records, i) for i in range(2, 10)]  # 将记录中的每一列都这样映射
cat_len = sum(map(len, mapping)) # 类型变量的长度
num_len = len(records.first()[11:15])  # 实数变量的长度
total_len = num_len + cat_len  # 总长度
# print("Feature vector length for categorical features: %d " % cat_len)
# print("Feature vector length for numerical features: %d " % num_len)
# print("Total feature vector length: %d" % total_len)

