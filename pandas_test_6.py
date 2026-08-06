import pandas as pd
import numpy as np
Fruits = pd.Series([7830, 11950, 113.1, 7152, 44.1, 140169.2])
Pulses = pd.Series([931, 818, 1.7, 33, 23.2, 2184.4])
Rice = pd.Series([7452.4, 1930, 2604.8, 11586.2, 814.6, 13754])
Wheat = pd.Series([np.nan, 2737, np.nan, 16440, 0.5, 30056])
org = {'Fruits':Fruits, 'Pulses':Pulses, 'Rice':Rice, 'Wheat':Wheat}
index = ["Andhra P.", "Gujarat", "Kerala", "Punjab", "Tripura", "Uttar P."]
prodf = pd.DataFrame(org)
prodf.index = index
print(prodf)
print("__________________________________________")
print(prodf[['Wheat', 'Rice']].count())                   #count the number of terms present in the table
print("__________________________________________")
print(prodf[['Rice']].sum())                              #add the number of terms present in the table
print("__________________________________________")
print(prodf.loc[['Kerala']].count())                      #count the number of terms in a table(rows)
print("__________________________________________")
print(prodf.loc[['Tripura']].sum())                         #add the number of terms present in the table(rows)
print("__________________________________________")
print(prodf.loc[:,:].count(axis = 1))                       #counting entire row/column in a table
print("__________________________________________")