import pandas as pd
import numpy as np
import itertools
import sys

# Function to take a value and a set of values to transform form a multicoding to a multiple single codings. 
def conversion(value, value_set):
	single_codes = value
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
			if(possible_value == value):
				running = False
				single_codes = p
				break
			# We know there are max. 3 codings in the dataset, therefore, if we can't find a combination of codes 
			# in the set that match the value, then the code must be incorrect. 
			if(i == 4):
				sys.exit("An impossible value has been found")
	return single_codes

# single codings
print(conversion(2**1, [1,4,7,10,13]))
print(conversion(2, [1,4,7,10,13]))
print(conversion(2**10, [1,4,7,10,13]))

# two codings
print(conversion(20,[4, 2, 1])) # 4 , 2
print(conversion(1028,[4, 2, 10])) # 10, 2

# # # three codings
print(conversion(8336,[13, 7, 4, 2, 6])) # 13, 7 , 4
print(conversion(8464,[13, 8, 4, 2, 6])) # 13, 8, 4



# Iterate through the long data file and re-create it with multiple single codings. 
def main():
	
	# read in data
	data = pd.read_csv("cldf/data.csv")
	coding_conversions = pd.read_csv("etc/codes.csv")
	
	# create new dataframe to fill in
	new_data = pd.DataFrame(columns=["song_id", "society_id", "var_id", "code", "ID"])
	
	# for logging
	line_lag = "line_0"
	
	data = data.loc[data['var_id'] == "line_7"]
	for index, row in data.iterrows():
	# for index, row in data.head(5).iterrows():
		if(pd.isnull(row["code"])):
			print(line + " - " + str(row["song_id"]) + " - " + str(row["society_id"]) + " is missing a value")
			continue

		split_df = pd.DataFrame(columns=["song_id", "society_id", "var_id", "code", "ID"])
		line = row['var_id']
		
		if(line_lag != line):
			print("Recoding "+ line + "...")
			line_lag = line
		print(line, row["song_id"], row["society_id"])

		value_set = coding_conversions.loc[coding_conversions["var_id"] == line, "code"]
		value = row['code']
		new_codes = conversion(value, value_set)
		split_df = split_df.append([row]*len(new_codes), ignore_index=True)
		split_df['code'] = new_codes
		new_data = new_data.append(split_df)

	# recreate IDs
	new_data["ID"] = str(new_data["song_id"]) +"_"+ str(new_data["society_id"]) +"_"+ new_data["var_id"] +"_"+ str(new_data["code"])
	new_data.to_csv("cldf/decoded_data.csv", index=False)


# main()