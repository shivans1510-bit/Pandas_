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

print(d1.count(axis = 1))   #counting the number of terms in a row or a column
print(d1.sum())             #adding up the terms 