import pandas as pd
import numpy as np

A = pd.Series([9, 36, 63, 90, 91, 91, 91, 91, 91, 91, 91, 91])
B = pd.Series([18, 45, 72, 99, 99, 99, 99, 99, 99, 99, 99, 99])
C = pd.Series([27, 54, 81, 108, 18, 18, 18, 18, 18, 18, 18, 18])
D = pd.Series(['This', 'This', 'string', 'is', 'string', 'this', 'This is fun', 'string', 'hello', 'hello', 'hello', 'string hello'])
org = {'A':A, 'B':B, 'C':C, 'D':D}

d1 = pd.DataFrame(org)
print(d1)
print(d1.info())
print(d1.head(n=4))                              # n terms from the beginning
print(d1.tail(n = 4))                           # n terms from the end
print(d1.cumsum())                                 #cumelative sum of numbers
print(d1.cumsum(axis = 'rows'))                 #cumsum row wise
print(d1.cumsum(axis = 'column'))               # cumsum column wise
print(d1.cummax())                              #cumelative maximum value
print(d1.cummin())                               #cumelative minimum value
