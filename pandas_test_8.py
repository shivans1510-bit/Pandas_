import pandas as pd
import numpy as np
ontutD = {'Tutor' :['Tahira', 'Gurjyot', 'Anusha', 'Jacob', 'Venkat',
                    'Tahira', 'Gurjyot', 'Anusha', 'Jacob', 'Venkat',
                    'Tahira', 'Gurjyot', 'Anusha', 'Jacob', 'Venkat',
                    'Tahira', 'Gurjyot', 'Anusha', 'Jacob', 'Venkat'],
        'Classes' :[28, 36, 41, 32, 40, 36, 40, 36, 40, 46, 24, 30, 44, 40, 32, 36, 32, 36, 42, 38],
        'Quarter': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],
        'Country' : ['USA', 'UK', 'Japan', 'USA', 'Brazil', 'USA', 'USA', 'Japan', 'Brazil', 
                     'USA', 'Brazil', 'USA', 'UK', 'Brazil', 'USA', 'Japan', 'Japan', 'Brazil', 
                     'UK', 'USA']}
df1 = pd.DataFrame(ontutD)
print(df1.pivot_table(index = 'Tutor', columns = 'Country', values = 'Classes', aggfunc = 'mean')) #printing a small amount of data from a large table.
print(df1.sort_values("Country"))                                                                  #Sorting a catigory in a table in ascending or descending order.
print(df1.sort_index(ascending = False))                                                            #Arranging the table's index.
print(df1.mad())                                                                                    #findinf the mean absolute deviation
