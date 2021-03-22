import pandas as pd
import numpy as np
import itertools
import sys
import warnings

# Function to take a value and a set of values to transform form a multicoding to a multiple single codings. 
def conversion(value, value_set):
	single_codes = -99
	possible_value = -99 
	i = 0
	running = True
	while(running):
		i += 1
		for p in itertools.combinations(value_set, i):
			# codes are the sum of each value as an exponent of 2. 
			# Here we take the set of possible codes, and check combinations to match the original code.
			# when the original code is matched, we return the combination of codes which create the combination. 
			possible_value = np.power(2, p).sum()	
			# print(value, possible_value, p, possible_value==value)	
			# pdb.set_t#race()
			if(possible_value == value):
				running = False
				single_codes = p
				break
			# We know there are max. 3 codings in the dataset, therefore, if we can't find a combination of codes 
			# in the set that match the value, then the code must be incorrect. 
			if(i == 4):
				single_codes = (float("NaN"),)
				running = False
				warnings.warn("WARNING: An impossible value has been found")
				break
				# sys.exit("An impossible value has been found")
	return single_codes


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
	
	#data = data.loc[data['var_id'] == "line_7"]
	for index, row in data.iterrows():
	# for index, row in data.head(5).iterrows():
		if(pd.isnull(row["code"])):
			print(line + " - " + str(row["song_id"]) + " - " + str(row["society_id"]) + " is missing a value")
			continue

		split_df = pd.DataFrame(columns=["song_id", "society_id", "var_id", "code", "ID"])
		line = row['var_id']
		
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

	# recreate IDs
	new_data.to_csv("cldf/decoded_data.csv", index=False)


main()