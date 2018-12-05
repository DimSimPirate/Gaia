#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tools for use with pandas

Created on Wed Sep 20 00:21:15 2017

@author: dan
"""

def rows_as_series(df):
    '''
    iterate rows of a DataFrame, yielding each as a Series
    
    Example:
        >>> import pandas as pd
        >>> df = pd.DataFrame.from_items([('A', ['a0', 'a1']), ('B', ['b0', 'b1'])])
        >>> next(rows_as_series(df))
        A    a0
        B    b0
        Name: 0, dtype: object
    '''
    for ndx in range(len(df)):
        yield df.iloc[ndx, ]
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()