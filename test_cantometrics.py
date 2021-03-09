import pytest
import pandas as pd
import datatest as dt 


@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def df():
    return pd.read_csv('raw/data.csv')

## Testing that all codes are valid

# Test for single value
def is_coding_allowed(integer, n=13):
    for i in range(n,0,-1):
        if integer == 0:
            return False
        if integer >= 2**i:
            integer -= 2**i
    return True if integer == 0 else False

def test_column(df):
    for col in df.columns:
        if 'cv_' in col:
            print(col)
            assert all([is_coding_allowed(x) == True for x in df[col]])



# def test_runtime(df):
#     dt.validate(df['canto_coding_id'], int)

