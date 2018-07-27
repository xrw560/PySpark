from pyspark.sql import SparkSession, Row
from pyspark.sql.types import *


def rdd_to_tuple(x):
    return [(x, 1), (x, 2), (x, 3)]


spark = SparkSession.builder \
    .appName("test") \
    .getOrCreate()
sc = spark.sparkContext


# rdd = sc.parallelize([1, 2, 3]).flatMap(lambda x: rdd_to_tuple(x))
# for x in rdd.collect():
#     print(x[0])

# stringJSONRDD = sc.parallelize((('''{'id':'123','name':'Katie','age':19,'eyeColor':'brown'}''',
#                                  '''{'id':'234','name':'Michael','age':22,'eyeColor':'green'}''',
#                                  '''{'id':'345','name':'Simone','age':23, 'eyeColor':'blue'}''')))
#
# swimmersJSON = spark.read.json(stringJSONRDD)
# swimmersJSON.createOrReplaceTempView("swimmersJSON")
# swimmersJSON.show()
# spark.sql("select * from swimmersJSON").collect()
# swimmersJSON.printSchema()

# Generate comma delimited data
# stringCSVRDD = sc.parallelize([(123, 'Katie', 19, 'brown'), (234, 'Michael', 22, 'green'), (345, 'Simone', 23, 'blue')])
# schema = StructType(
#     [StructField('id', LongType(), True), StructField('name', StringType(), True), StructField('age', LongType(), True),
#      StructField('eyeColor', StringType(), True)])
# # Apply the schema to the RDD and Create DataFrame
# swimmers = spark.createDataFrame(stringCSVRDD, schema)
# # # Creates a temporary view using the DataFrame
# swimmers.createOrReplaceTempView('swimmers')
# swimmers.printSchema()
# # print(swimmers.count())
# # df = stringCSVRDD.toDF(("id", "name", "age", "eyeColor"))
# rdd = stringCSVRDD.map(lambda p: Row(id=p[0], name=p[1], age=p[2], eyeColor=p[3]))
# print(type(rdd))
# df = spark.createDataFrame(rdd)
# df.printSchema()
spark.stop()
