import os.path
import pandas as pd
import csv
from collections import Counter 
import numpy as np
import json
import math
import json

DATA_PATH = './raw/data.csv'
metadata = pd.read_csv('./conversion/metadata.csv')

with open('./conversion/code_mappings.json') as f:
    mapping_data = json.load(f)


def camel_case_split(str): 
    '''
    input: multi-variable shortname
    output: description of a multi-coded variable
    '''
    words = [[str[0]]] 
    txt = ''
    
    for c in str[1:]: 
        if words[-1][-1].islower() and c.isupper(): 
            words.append(list(c)) 
        else: 
            words[-1].append(c) 
    word_list = [''.join(word) for word in words] 
    for i in range(len(word_list)):
        if i==0:
            txt += word_list[i]+' '
        else:
            txt += word_list[i].lower()+' '
    return txt.rstrip()


def continuous(key, line_num):
    '''
    input: a key from the cantometrics codings and a line number
    output: the correspoinding value in a continuous range from 0 to the number of discrete codings
    desc: refer to conversion/code_mappings.json for the complete mapping of values
    '''
    return mapping_data[line_num-1][str(key)]

def get_metadata(l, oc):
    filtered_data = metadata[metadata['line_num']==l]
    original_codes = list(filtered_data['original_code'])
    descriptions = list(filtered_data['code_description'])
    shortnames = list(filtered_data['shortname'])
    for i in range(len(filtered_data)):
        if int(original_codes[i])==oc:
            return shortnames[i], descriptions[i]
    return 'Shortname Not Found', 'Description Not Found'

def encode_data(line_num, data):
    row = []
    description = ''
    shortname = ''
    column_name = "cv_"+str(line_num)
    
    tmp_short = ''
    tmp_dsc = ''
 
    column = data[column_name]
    column_counter = dict(Counter(column))
    
    keys = list(column_counter.keys())
    values = list(column_counter.values())
    
    for i in range(len(keys)):
        original_1 = 0
        original_2 = None
        original_3 = None
        code_1 = 0
        code_2 = None
        code_3 = None
        display_code = 0
        var_id = ''
        if (keys[i] is None):
            continue
        elif(int(keys[i])==0):
            shortname = 'No Reading'
            description = 'No Reading'
        else:
            log = math.log2(int(keys[i]))
            if(log.is_integer()==False):
                closest = math.floor(log)
                diff = int(keys[i]) - (2**closest)
                if(math.log2(diff).is_integer()== False):
                    diff_2 = diff-(2**(math.floor(math.log2(diff))))
                    original_1 = int(closest)
                    original_2 = int(math.floor(math.log2(diff)))
                    original_3 = int(math.log2(diff_2))
                    display_code = round((original_1+original_2+original_3)/3,2)
                    var_id = str(line_num)+'_'+str(original_1)+'_'+str(original_2)+'_'+str(original_3)
                    
                    shortname = ''
                    description = ''
                    
                    tmp_short, tmp_dsc = get_metadata(line_num, original_1)
                    shortname += tmp_short+'And'
                    tmp_short, tmp_dsc = get_metadata(line_num, original_2)
                    shortname += tmp_short+'And'
                    tmp_short, tmp_dsc = get_metadata(line_num, original_3)
                    shortname += tmp_short
                    description = camel_case_split(shortname)
                    
                else:
                    original_1 = int(closest)
                    original_2 = int(math.log2(diff))
                    display_code = (original_1 + original_2)/2
                    var_id = str(line_num)+'_'+str(original_1)+'_'+str(original_2)
                    
                    shortname = ''
                    description = ''
                    
                    tmp_short, tmp_dsc = get_metadata(line_num, original_1)
                    shortname += tmp_short +'And'
                    tmp_short, tmp_dsc = get_metadata(line_num, original_2)
                    shortname += tmp_short
                    description = camel_case_split(shortname)
            else:
                original_1 = int(log)
                display_code = log
                var_id = str(line_num)+'_'+str(original_1)
                shortname, description = get_metadata(line_num, original_1)
        try:
            code_1 = mapping_data[line_num-1][str(original_1)]
        except KeyError as e:
            print("LINE:", line_num, " KEY:", e)
        
        if(original_2):
            try:
                code_2 = mapping_data[line_num-1][str(original_2)]
            except KeyError as e:
                print("CODE_2 LINE:", line_num, " KEY:", e)
        if(original_3):
            try:
                code_3 = mapping_data[line_num-1][str(original_3)]
            except KeyError as e:
                print("CODE_4 LINE:", line_num, " KEY:", e)
        
        row.append(
            {
                "code":keys[i],
                "count": values[i], 
                "var_id_code": str(line_num)+"_"+str(keys[i]), 
                "original_1": original_1, 
                "original_2":original_2, 
                "original_3": original_3, 
                "code_1": code_1, 
                "code_2": code_2, 
                "code_3": code_3, 
                "display_code": round(display_code/13,2),
                "var_id": var_id,
                "code_description": description,
                "shortname": shortname
            })
        
    row.sort(key=lambda x: x["display_code"])
    return(row)

def main():
    lines = {} #modify this for structure
    
    try: 
        os.path.exists(DATA_PATH)
    except:
        print("Data not found")
        exit()

    data = pd.read_csv(DATA_PATH)
    for i in range(37):
        print("Converting line ",(i+1))
        line_key = "line_"+str(i+1)
        lines[line_key] = encode_data(i+1, data)
    with open('./conversion/conversion_guide.json', 'w') as f:
        json.dump(lines, f)
main()



