# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 16:35:34 2018

@author: 小周

"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


df = pd.DataFrame([['green', 'M', 10.1, 'class1'],
                   ['red', 'L', 13.5, 'class2'],
                   ['blue', 'XL', 15.3, 'class1']])
df.columns = ['color', 'size', 'price', 'classlabel']
'''
Out[1]: 
   color size  price classlabel
0  green    M   10.1     class1
1    red    L   13.5     class2
2   blue   XL   15.3     class1
'''

# Mapping ordinal features
def Mapping_ordinal_features():
    size_mapping = {'XL':3,
                    'L':2,
                    'M':1}
    df['size'] = df['size'].map(size_mapping)
    '''
    Out[2]: 
       color  size  price classlabel
    0  green     1   10.1     class1
    1    red     2   13.5     class2
    2   blue     3   15.3     class1
    '''
    
    #inv_size_mapping = {v: k for k, v in size_mapping.items()}
    #print(df['size'].map(inv_size_mapping))
    '''
    Out[3]:
    0     M
    1     L
    2    XL
    Name: size, dtype: object
    '''
    return df

# Encoding class labels
def Encoding_class_labels():
    
    class_mapping = {label: idx for idx, label in enumerate(np.unique(df['classlabel']))}
    '''
    Out[4]:
    {'class1': 0, 'class2': 1}
    '''
    df['classlabel'] = df['classlabel'].map(class_mapping)
    '''
    Out[5]:
       color size  price  classlabel
    0  green    M   10.1           0
    1    red    L   13.5           1
    2   blue   XL   15.3           0
    '''
    
    inv_class_mapping = {v: k for k, v in class_mapping.items()}
    df['classlabel'] = df['classlabel'].map(inv_class_mapping)
    
    #class_le = LabelEncoder()
    #y = class_le.fit_transform(df['classlabel'].values)
    # [0,1,0]
    
    #print(class_le.inverse_transform(y))

    '''
    Performing one-hot encoding on nominal features
    '''
    
    X = df[['color', 'size', 'price']].values
    
    color_le = LabelEncoder()
    X[:, 0] = color_le.fit_transform(X[:, 0])
    
    ohe = OneHotEncoder(categorical_features=[0])
    #print(ohe.fit_transform(X).toarray())
    
    print(pd.get_dummies(df[['price', 'color', 'size']]))

#df = Mapping_ordinal_features()
Encoding_class_labels()







