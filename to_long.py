import pandas as pd
import numpy as np
from pandas import read_csv, melt

data = read_csv("raw/data.csv")
long_df = melt(data, id_vars = ['canto_coding_id', 'C_cid'], var_name='var_id', value_name = 'code')
long_df['ID'] = long_df['canto_coding_id'].astype(str) + "_" + long_df['C_cid'].astype(str) + long_df['var_id'].astype(str)

# make all 0 values NA 
long_df = long_df.replace(0, np.nan)

long_df.to_csv("cldf/data.csv", index=False)
