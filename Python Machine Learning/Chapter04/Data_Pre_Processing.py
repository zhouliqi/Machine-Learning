# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 15:25:43 2018

@author: 小周

"""

import pandas as pd
from io import StringIO

csv_data = '''A, B, C, D
1.0, 2.0, 3.0, 4.0
5.0, 6.0,, 8.0
10.0,11.0, 12.0,'''

df = pd.read_csv(StringIO(csv_data))
#print(df)
'''
Out[4]:
      A     B     C    D
0   1.0   2.0   3.0  4.0
1   5.0   6.0   NaN  8.0
2  10.0  11.0  12.0  NaN
'''


#====================================================
# Eliminating samples or features with missing values
def missing_value():
    df.isnull().sum()
    
    # 丢弃所以带NaN的数据(默认按行处理)
    df.dropna()
    '''
    Out[5]:
         A    B    C    D
    0  1.0  2.0  3.0  4.0
    '''
    
    # 丢弃所以列包含NaN的数据(axis=1)
    df.dropna(axis=1)
    
    # Only drop rows where all colnmns are NaN
    df.dropna(how='all')
    
    # drop rows that have not at least 4 non-NaN values
    df.dropna(thresh=4)
    
    #  only drop rows where NaN appear in specific columns (here: 'C')
    print(df.dropna(subset=['C']))

def imputing_missing_values():
    from sklearn.preprocessing import Imputer
    
    # 把有NaN的数据用这一列的均值替换
    imr = Imputer(missing_values='NaN', strategy='mean', axis=0)
    imr = imr.fit(df)
    imputed_data = imr.transform(df.values)
    #print(df.values)
    print(imputed_data)

if __name__ == '__main__':
    
    #missing_value()
    imputing_missing_values()













