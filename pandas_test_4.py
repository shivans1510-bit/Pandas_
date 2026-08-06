import pandas as pd
import numpy as np

s1 = pd.Series([99, 94, 95, 94, 97])
s2 = pd.Series([94, 94, 89, 87, 100])
s3 = pd.Series([81, 72, 71, 79, 65])
s4 = pd.Series([70, 67, 65, 69, 65])
s5 = pd.Series([88, 82, 82, 89, 86])
s6 = pd.Series([90, 81, 79, 81, 84])
s7 = pd.Series([41, 36, 51, 42, 40])
s8 = pd.Series([61, 54, 60, 63, 55])
s9 = pd.Series([42, 42, 45, 43, 40])
s10 = pd.Series([68, 67, 66, 64, 60])
sections = {'_1_':s1, '_2_':s2, '_3_':s3, '_4_':s4, '_5_':s5, '_6_':s6, '_7_':s7, '_8_':s8, '_9_':s9, '_10_':s10}
index = ['Acct', 'Eco', 'Eng', 'IP', 'Math']
d1 = pd.DataFrame(sections)
d1.index = index
print(d1)

print("____________________________________________________")
# print("Performance of student, subject wise :-")
# print(d1.quantile([0.25, 0.5, 0.75, 1.0], axis = 1))                #part of a term in the table (quintile) 
# print(d1.std(axis = 1))                                             #standard deviation of the table
# print(d1.var(axis = 1))                                             #for the varience of the table
print(d1.describe())                                                #table's entire information