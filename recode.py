import pandas as pd
import numpy as np
import itertools

data = pd.read_csv("cldf/data.csv")
coding_conversions = pd.read_csv("conversion/metadata.csv")

def conversion(value, value_set):
	single_codes = value
	possible_value = -99 
	i = 0
	while(possible_value != value):
		i += 1
		for p in itertools.combinations(value_set, i):
			possible_value = np.power(2, p).sum()
			# print([value, possible_value])
			# print(value == possible_value)			
			if(possible_value == value):
				single_codes = p
				break
	return single_codes

# two codings
# print(conversion(20,[4, 2, 1])) # 4 , 2
# print(conversion(1028,[4, 2, 10])) # 10, 2

# # three codings
# print(conversion(8336,[13, 7, 4, 2, 6]))
# print(conversion(8464,[13, 8, 4, 2, 6]))

def main():
	for index, row in data.iterrows():
	    line = row['var_id']
	    print(line)
	    #value_set = coding_conversions[]

main()