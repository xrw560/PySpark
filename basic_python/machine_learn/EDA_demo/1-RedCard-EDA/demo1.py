from __future__ import absolute_import, division, print_function
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.pyplot import GridSpec
import seaborn as sns
import numpy as np
import pandas as pd
import os, sys
from tqdm import tqdm
import warnings

warnings.filterwarnings('ignore')
sns.set_context("poster", font_scale=1.3)

# import missingno as msno
import pandas_profiling

from sklearn.datasets import make_blobs
import time

# Uncomment one of the following lines and run the cell:

df = pd.read_csv("redcard.csv.gz", compression='gzip')

print(df.shape)
# print(df.head())
# print(df.describe().T)
# print(df.dtypes)
all_columns = df.columns.tolist()
# print(all_columns)
print(df['height'].mean())
print(np.mean(df.groupby('playerShort').height.mean()))

# df2 = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
#                     'key2': ['one', 'two', 'one', 'two', 'one'],
#                     'data1': np.random.randn(5),
#                     'data2': np.random.randn(5)})
# print(df2)
# grouped = df2['data1'].groupby(df2['key1'])
# print(grouped.mean())

"""数据切分"""



