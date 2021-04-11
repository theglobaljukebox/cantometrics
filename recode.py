import pandas as pd
import numpy as np
import itertools
import sys
import warnings
from helper import conversion



# single_1 = (conversion(2**1, [1,4,7,10,13])) == (1,)
# single_2 = (conversion(2, [1,4,7,10,13])) == (1,)
# single_3 = (conversion(2**10, [1,4,7,10,13])) == (10,)
# single_4 = (conversion(64, [1,4,6,7,10,13])) == (10,)

# # two codings
# double_1 = (conversion(20,[4, 2, 1])) == (4, 2)# 4 , 2
# double_2 = (conversion(1028,[4, 2, 10])) == (2, 10) # 10, 2

# # # # three codings
# triple_1 = (conversion(8336,[13, 7, 4, 2, 6])) == (13, 7, 4) # 13, 7 , 4
# triple_2 = (conversion(8464,[13, 8, 4, 2, 6])) == (13, 8, 4) # 13, 8, 4


# Iterate through the long data file and re-create it with multiple single codings. 
def main():
	
	# read in data
	data = pd.read_csv("cldf/data.csv")
	data = data.sort_values(by=['var_id']) # ensure data is ordered by line for future filtering
	coding_conversions = pd.read_csv("etc/codes.csv")
	
	# create new dataframe to fill in
	new_data = pd.DataFrame(columns=["song_id", "society_id", "var_id", "code", "ID"])
	
	# for logging
	line_lag = "line_0"
	
	for index, row in data.iterrows():
	# for index, row in data.head(5).iterrows():
		split_df = pd.DataFrame(columns=["song_id", "society_id", "var_id", "code", "ID"])
		line = row['var_id']
	
		if(pd.isnull(row["code"])):
			print(line + " - " + str(row["song_id"]) + " - " + str(row["society_id"]) + " is missing a value")
			continue
	
		# Data was ordered in line order, so we only need the line set once.
		# Print the line being analysed for logging purposes
		if(line_lag != line):
			print("Recoding "+ line + "...")
			line_lag = line
			value_set = coding_conversions.loc[coding_conversions["var_id"] == line, "code"].to_numpy()
			# print(value_set)
		

		# print(line, row["song_id"], row["society_id"])
		value = row['code']
		new_codes = conversion(value, value_set)

		## If new codes are -99 then they were invalid codes and we need to correct them
		if(new_codes[0] == -99):
			with open("logs/invalid_codes.txt", "a") as invalid_file:
				invalid_file.write(line + " - " + str(row["song_id"]) + " - " + str(row["society_id"]) + " is an invalid code\n")

		split_df = split_df.append([row]*len(new_codes), ignore_index=True)
		split_df['code'] = new_codes
		new_data = new_data.append(split_df)

	# save file
	new_data.to_csv("cldf/data.csv", index=False)


main()
