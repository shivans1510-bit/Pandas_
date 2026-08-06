import pandas as pd
import numpy as np

# d1 = {'Tutor' : ['Tahira', 'Gurjyot', 'Anusha', 'Jacob', 'Venkat'],
#         'Classes' : [28, 36, 41, 32, 40], 
#         'Country' : ['USA', 'UK', 'Japan', 'USA', 'Brazil']
#     }
# dfd = pd.DataFrame(d1)
# print(dfd)
# print(dfd.pivot(index = 'Country', columns = 'Tutor', values = 'Classes'))

d2 = {'Name': ['Rabia', 'Evan', 'Jia', 'Lalit', 'Jaspreet', 'Suji'], 
      'Sex': ['F', 'M', 'F', 'M', 'M', 'F'],
      'Position': ['Manager', 'Programmer', 'Manager', 'Manager', 'Programmer', 'Programmer'],
      'City': ['Bangalore', 'New Delhi', 'Chennai', 'Mumbai', 'Chennai', 'Bangalore'], 
      'Age': [30, 27, 32, 40, 28, 32], 
      'Projects': [13, 17, 16, 20, 21, 14]}
ndf = pd.DataFrame(d2)
print(ndf)
print("_____________________________________________________________________")
print(ndf.pivot(index = 'Position', columns = 'City', values = 'Projects').fillna(0))




