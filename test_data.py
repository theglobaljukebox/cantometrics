import pytest
import pandas as pd

data  		= pd.read_csv('raw/data.csv')
songs 		= pd.read_csv('raw/songs.csv') 
societies 	= pd.read_csv('raw/societies.csv')

def test_fkdatasongs():
	data_id 	= data['canto_coding_id'].to_numpy().astype(str)
	songs_id 	= songs['C-id'].to_numpy().astype(str)

	print(data_id)
	print(songs_id)

	[print("WARNING: Data ID " + str(x) + " is not a recognised song id") for x in data_id if x not in songs_id]

	assert all([x in songs_id for x in data_id])

def test_fkdataculture():
	data_id 		= data['C_cid'].to_numpy().astype(str)
	societies_id 	= societies['All_cid'].to_numpy().astype(str)

	print(data_id)
	print(societies_id)

	[print("WARNING: Data ID " + str(x) + " is not a recognised society id") for x in data_id if x not in societies_id]

	assert all([x in societies_id for x in data_id])