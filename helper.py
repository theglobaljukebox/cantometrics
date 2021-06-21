import itertools
import pandas as pd
import numpy as np
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
			if(possible_value == value):
				running = False
				single_codes = p
				break
			# We know there are max. 3 codings in the dataset, therefore, if we can't find a combination of codes 
			# in the set that match the value, then the code must be incorrect. 
			if(i == 5):
				single_codes = (float("NaN"),)
				running = False
				warnings.warn("WARNING: An impossible value has been found")
				break
	return single_codes