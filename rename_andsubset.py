import pandas as pd

data 		= pd.read_csv('cldf/data.csv')
songs 		= pd.read_csv('cldf/songs.csv')
societies 	= pd.read_csv('cldf/societies.csv')


# data file links to songs and soceity metadata
data.rename(columns={
	'canto_coding_id':'song_id',
	'C_cid':'society_id'}, 
	inplace = True)

# songs metadata links to data file and soceity metadata
songs.rename(columns={
	'C-id':'song_id',
	'C_cid':'society_id'}, 
	inplace = True)

# soceity metadata links to data
societies.rename(columns={
	'All_cid':'society_id'}, 
	inplace = True)

# Only need metadata on societies that exist in Cantometrics data
societies = societies[pd.notna(societies["C_cid"])]

# Only need metadata on songs that have been coded
songs = songs[~songs["song_id"].str.contains("NC")]

data.to_csv('cldf/data.csv', index=False)
songs.to_csv('cldf/songs.csv', index=False)
societies.to_csv('cldf/societies.csv', index=False)