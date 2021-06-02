import pandas as pd
import numpy as np

data 		= pd.read_csv('cldf/data.csv')
songs 		= pd.read_csv('cldf/songs.csv')
societies 	= pd.read_csv('cldf/societies.csv')

data["ID"] = np.arange(len(data))

# Put society_id as the first column
societies = societies[['society_id'] + [c for c in societies if c not in ['society_id']]]

# Only need metadata on songs that have been coded
songs = songs[~songs["song_id"].str.contains("NC")]
# strip newlines and commas from all columns
strip_songcolumns = ["Lyrics", "Song_notes", "Living_metadata", "Performers", "Metadata_notes", "Instruments", "Society_location",
	"Publcation_collection", "Audio_file", "Repository", "Sources", "Recorded_by"]
for column in strip_songcolumns:
    songs[column] = [ str(y).replace("\n", " ").replace(",", " ").replace("\r", " ") for y in songs[column]] 


strip_societycolumns = ["Society_summary",  "Language", "Koppen_climate_terrain", "Region", "Division", 
                        "Subregion", "Area", "society", "alternative_names", "People", "People2", "People3",
                        "Arensberglomax_taxon", "Language_nearsubfamily", "Language_largersubfamily", "Language_family", "Country"]
for column in strip_societycolumns:
    societies[column] = [ str(y).replace("\n", " ").replace(",", " ").replace("\r", " ") for y in societies[column]] 

societies["Culture Sources"] = [str(y).strip() for y in societies["Culture Sources"]]

# Only need metadata on cultures that exist in Cantometrics data
## While I wait to have some values fixed in the cultures metadata, I need this workaround
societies["society_id"]     = societies["society_id"].astype(str)
songs["society_id"]         = songs["society_id"].astype(str)
data["society_id"]          = data["society_id"].astype(str)
keep_societies = data["society_id"].unique()
societies = societies[societies.society_id.isin(keep_societies)]
songs = songs[songs.society_id.isin(keep_societies)]

# Manually remove these songs because AW wants to keep the metadata in googlesheets
remove_songs = open("removed_songs.txt").read().splitlines()
# songs = songs[np.logical_not(songs.song_id.isin(remove_songs))]

data.to_csv('cldf/data.csv', index=False)
songs.to_csv('cldf/songs.csv', index=False)
societies.to_csv('cldf/societies.csv', index=False)