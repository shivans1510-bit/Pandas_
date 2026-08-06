import pandas as pd
import numpy as np
rtSer = pd.Series([11, np.nan, 30.5, np.nan, 17])
print(rtSer)
print(rtSer.isnull())                           #to find out the null values in a table
print(rtSer.notnull())                          #to find out the not null value in the table
print(rtSer.dropna())                           #it drops the value with nan value and print the one with no nan value

