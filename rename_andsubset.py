import pandas as pd
import numpy as np

data 		= pd.read_csv('cldf/data.csv')
songs 		= pd.read_csv('cldf/songs.csv')
societies 	= pd.read_csv('cldf/societies.csv')

data["ID"]  = np.arange(len(data))

# Put society_id as the first column
societies = societies[['society_id'] + [c for c in societies if c not in ['society_id']]]

# Only need metadata on songs that have been coded
songs = songs[~songs["song_id"].str.contains("NC")]
# strip newlines and commas from all columns
strip_songcolumns = ["Lyrics", "Song_notes", "Living_metadata", "Performers", "Metadata_notes", "Instruments", "Society_location",
	"Publcation_collection", "Audio_file", "Repository", "Sources", "Recorded_by"]
for column in strip_songcolumns:
    songs[column] = [ str(y).replace("\n", " ").replace(",", " ").replace("\r", " ") for y in songs[column]] 

# Only need metadata on cultures that exist in Cantometrics data
## While I wait to have some values fixed in the cultures metadata, I need this workaround
societies["society_id"]     = societies["society_id"].astype(str)
songs["society_id"]         = songs["society_id"].astype(str)
data["society_id"]          = data["society_id"].astype(str)
keep_societies              = data["society_id"].unique()
societies                   = societies[societies.society_id.isin(keep_societies)]

# Manually remove these songs because AW wants to keep the metadata in googlesheets
remove_songs = open("removed_songs.txt").read().splitlines()
songs = songs[np.logical_not(songs.song_id.isin(remove_songs))]

data.to_csv('cldf/data.csv', index=False, na_rep='')
songs.to_csv('cldf/songs.csv', index=False, na_rep='')
songs.to_csv('raw/songs.csv', index=False, na_rep='')
societies.to_csv('cldf/societies.csv', index=False, na_rep='')