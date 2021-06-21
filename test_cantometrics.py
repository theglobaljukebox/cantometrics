import pytest
import pandas as pd
import datatest as dt 

from helper import conversion


@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def df_raw():
    return pd.read_csv('raw/data.csv')

@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def song_cldf():
    return pd.read_csv('cldf/songs.csv')


## Testing that all codes are valid

# Test for single value
def is_coding_allowed(integer, n=13):
    for i in range(n,0,-1):
        if integer >= 2**i:
            integer -= 2**i
    return True if integer == 0 else False

def test_codings(df_raw):
    for col in df_raw.columns:
        if 'line_' in col:
            print(col)
            assert all([is_coding_allowed(x) == True for x in df_raw[col]])


def test_conversion():
    # single codings
    print("singles")
    single_1 = (conversion(2**1, [1,4,7,10,13])) == (1,)
    single_2 = (conversion(2, [1,4,7,10,13])) == (1,)
    single_3 = (conversion(2**10, [1,4,7,10,13])) == (10,)

    print("twos")
    # two codings
    double_1 = (conversion(20,[4, 2, 1])) == (4, 2)# 4 , 2
    double_2 = (conversion(1028,[4, 2, 10])) == (2, 10) # 10, 2

    print('threes')
    # # # three codings
    triple_1 = (conversion(8336,[13, 7, 4, 2, 6])) == (13, 7, 4) # 13, 7 , 4
    triple_2 = (conversion(8464,[13, 8, 4, 2, 6])) == (13, 8, 4) # 13, 8, 4

    assert all([single_1, single_2, single_3, double_1, double_2, triple_1, triple_2])

def test_rownums(df_raw, song_cldf):
    assert df_raw.index[0] == song_cldf.index[0]

