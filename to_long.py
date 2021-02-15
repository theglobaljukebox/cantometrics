import pandas as pd
from pandas import read_csv, melt

data = read_csv("raw/data.csv")
long_df = melt(data, id_vars = ['canto_coding_id', 'Culture', 'C_cid'], var_name='var_id', value_name = 'code')
long_df['ID'] = long_df['canto_coding_id'].astype(str) + "_" + long_df['C_cid'].astype(str) + long_df['var_id'].astype(str)
long_df.to_csv("cldf/data.csv", index=False)