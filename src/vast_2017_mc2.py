"""
Helpers and settings for VAST 2017 Mini Challenge 2

Created on Tue Sep 12 22:02:01 2017

@author: dan
"""

import pathlib
import pandas as pd

src_path = pathlib.Path(__file__).parent
root_path = src_path.parent
dat_path = root_path/'data'
out_path = root_path/'out'
cache_path = root_path/'cache'

source_file_excel = dat_path/'modified/all.xlsx'
source_file_pickle = source_file_excel.with_suffix('.pickle')

def load_cleaned_data(filter_and_index=True):
    dtype = {col: 'category' for col in ['chemical', 'hour_category', 'hour_subcategory']}
    result = pd.read_csv(dat_path/'data.csv', dtype=dtype)
    for col, fmt in [('timestamp', '%d/%m/%Y %H:%M'), ('date', '%d/%m/%Y')]:
        result[col] = pd.to_datetime(result[col], format=fmt)
    if filter_and_index:
        result = result[(result['missing_sensor'] == 0) & (result['has_duplicate'] == 0) & (result['missing_wind'] == 0)]
        result.set_index(['chemical', 'monitor', 'timestamp'], inplace=True)
    return result

