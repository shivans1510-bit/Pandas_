import pandas as pd
import numpy as np

A = pd.Series([99, 90, 95, 94, 97])
B = pd.Series([94, 94, 89, np.nan, 100])
C = pd.Series([92, 92, 91, 99, 99])
D = pd.Series([97, 97, 89, 95, np.nan])

index = ['Acct', 'Eco', 'Eng', 'IP', 'Math']
org = {'A':A, 'B':B, 'C':C, 'D':D}

d1 = pd.DataFrame(org)
d1.index = index
print(d1)
print(d1.max(axis = 1))
print(d1.max(axis = 1, skipna = True))              #for max value in columns
print(d1.max())                                     #for max value in rows
print(d1.idxmin())                                  #for the index with the minimum value
print(d1.idxmax())                                  #for the index with the maximum value
print(d1.mode(axis = 0, numeric_only = False))      #for mode value
print(d1.mean(axis = 0, numeric_only = False))      #for mean
print(d1.median(axis = 0, numeric_only = False))    #for median