import pandas as pd

data 		= pd.read_csv('cldf/data.csv')
songs 		= pd.read_csv('cldf/songs.csv')
cultures 	= pd.read_csv('cldf/cultures.csv')


# data file links to songs and soceity metadata
data.rename(columns={
	'canto_coding_id':'song_id',
	'C_cid':'culture_id'}, 
	inplace = True)

# songs metadata links to data file and soceity metadata
songs.rename(columns={
	'C-id':'song_id',
	'C_cid':'culture_id'}, 
	inplace = True)

# soceity metadata links to data
cultures.rename(columns={
	'All_cid':'culture_id'}, 
	inplace = True)

# Only need metadata on cultures that exist in Cantometrics data
## While I wait to have some values fixed in the cultures metadata, I need this workaround
cultures["culture_id"] 	= cultures["culture_id"].astype(str)
data["culture_id"] 		= data["culture_id"].astype(str)
keep = data["culture_id"].unique()
cultures = cultures[cultures.culture_id.isin(keep)]

# Only need metadata on songs that have been coded
songs = songs[~songs["song_id"].str.contains("NC")]

data.to_csv('cldf/data.csv', index=False)
songs.to_csv('cldf/songs.csv', index=False)
cultures.to_csv('cldf/cultures.csv', index=False)