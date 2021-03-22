import pandas as pd
import numpy as np
from pandas import read_csv, melt

data = read_csv("raw/data.csv")
long_df = melt(data, id_vars = ['song_id', 'society_id'], var_name='var_id', value_name = 'code')
# long_df['ID'] = long_df['song_id'].astype(str) + "_" + long_df['society_id'].astype(str) + long_df['var_id'].astype(str)

# make all 0 values NA 
print((long_df['code'] == 0).sum(), "values were 0 and replaced as NA values")
long_df = long_df.replace(0, np.nan)

long_df.to_csv("cldf/data.csv", index=False)
