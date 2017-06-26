# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 21:49:29 2017

@author: Rishi Raj
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

db = pd.read_csv("database.csv",low_memory=False)

db2=db[db['Perpetrator Age']!='0']
db2=db2[db['Victim Age']!=0]
db2=db2[db['Victim Age']!=998]

x=db2['Victim Age']
y=db2['Perpetrator Age'].convert_objects(convert_numeric=True)

a=LinearRegression()
a.fit(x,y)

x1=db[db['Perpetrator Age']=='0']['Victim Age']

plt.plot(x, y,'bo', label='Actual')
plt.plot(x1, a.predict(x1) , 'ro', label='Predicted' )
plt.xlabel("Victim Age")
plt.ylabel("Perpetrator Age")
plt.show()