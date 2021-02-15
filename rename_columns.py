import pandas as pd

data 		= pd.read_csv('cldf/data.csv')
songs 		= pd.read_csv('cldf/songs.csv')
societies 	= pd.read_csv('cldf/societies.csv')

data.rename(columns={
	'canto_coding_id':'song_id',
	'C_cid':'society_id'}, 
	inplace = True)

songs.rename(columns={
	'C-id':'song_id',
	'C_cid':'society_id'}, 
	inplace = True)

societies.rename(columns={
	'All_cid':'society_id'}, 
	inplace = True)

data.to_csv('cldf/data.csv', index=False)
songs.to_csv('cldf/songs.csv', index=False)
societies.to_csv('cldf/societies.csv', index=False)