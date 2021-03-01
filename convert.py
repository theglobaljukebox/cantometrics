import os.path
import pandas as pd
import csv
import numpy as np
import json

with open('./conversion/code_mappings.json') as f:
    mapping_data = json.load(f)

def continuous(key, line_num):
    '''
    input: a key from the cantometrics codings and a line number
    output: the correspoinding value in a continuous range from 0 to the number of discrete codings
    desc: refer to conversion/code_mappings.json for the complete mapping of values
    '''
    return mapping_data[line_num-1][str(key)]

def main():
    # Data sheet
    print("Converting coding to a continuous range")
    print(continuous(1,1))
main()
