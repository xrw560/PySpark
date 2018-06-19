from pyspark.sql import SparkSession, Row
from pyspark.sql.types import *
import pyspark.sql.functions as fn

spark = SparkSession.builder \
    .appName("test") \
    .getOrCreate()
sc = spark.sparkContext

# df = spark.createDataFrame([
#     (1, 144.5, 5.9, 33, 'M'),
#     (2, 167.2, 5.4, 45, 'M'),
#     (3, 124.1, 5.2, 23, 'F'),
#     (4, 144.5, 5.9, 33, 'M'),
#     (5, 133.2, 5.7, 54, 'F'),
#     (3, 124.1, 5.2, 23, 'F'),
#     (5, 129.2, 5.3, 42, 'M'), ],
#     ['id', 'weight', 'height', 'age', 'gender'])
# print('count of rows: {0}'.format(df.count()))
# print('count of distinct rows: {0}'.format(df.distinct().count()))
# df = df.dropDuplicates()
# df.show()
#
# print('count of ids: {0}'.format(df.count()))
# print('count of distinct ids: {0}'.format(df.select([c for c in df.columns if c != 'id']).distinct().count()))
#
# df = df.dropDuplicates(subset=[c for c in df.columns if c != 'id'])
# df.show()
# spark.stop()

# df.agg(fn.count('id').alias('count'), fn.countDistinct('id').alias('distinct')).show()

# df.withColumn('new_id', fn.monotonically_increasing_id()).show()

# df_miss = spark.createDataFrame([
#     (1, 143.5, 5.6, 28, 'M', 100000),
#     (2, 167.2, 5.4, 45, 'M', None),
#     (3, None, 5.2, None, None, None),
#     (4, 144.5, 5.9, 33, 'M', None),
#     (5, 133.2, 5.7, 54, 'F', None),
#     (6, 124.1, 5.2, None, 'F', None)], ['id', 'weight', 'height', 'age', 'gender', 'income'])
#
# df_miss_no_income = df_miss.select([c for c in df_miss.columns if c != 'income'])
# df_miss_no_income.dropna(thresh=3).show()
# means = \
#     df_miss_no_income.agg(
#         *[fn.mean(c).alias(c) for c in df_miss_no_income.columns if c != 'gender']).toPandas().to_dict(
#         'records')
# print(means)
# means['gender'] = 'missing'
# df_miss_no_income.fillna(means).show()

df_outliers = spark.createDataFrame([
    (1, 143.5, 5.3, 28),
    (2, 154.2, 5.5, 45),
    (3, 342.3, 5.1, 99),
    (4, 144.5, 5.5, 33),
    (5, 133.2, 5.4, 54),
    (6, 124.1, 5.1, 21),
    (7, 129.2, 5.3, 42)],
    ['id', 'weight', 'height', 'age']
)
cols = ['weight', 'height', 'age']
bounds = {}
for col in cols:
    quantiles = df_outliers.approxQuantile(col, [0.25, 0.75], 0.05)
    IQR = quantiles[1] - quantiles[0]
    bounds[col] = [quantiles[0] - 1.5 * IQR, quantiles[1] + 1.5 * IQR]

outliers = df_outliers.select(
    *['id'] + [((df_outliers[c] < bounds[c][0]) | (df_outliers[c] > bounds[c][1])).alias(c + '_o') for c in cols])
outliers.show()
df_outliers = df_outliers.join(outliers, on='id')
df_outliers.filter('weight_o').select('id', 'weight').show()
df_outliers.filter('age_o').select('id', 'age').show()
spark.stop()
