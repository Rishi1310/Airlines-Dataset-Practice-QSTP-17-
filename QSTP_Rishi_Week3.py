# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 16:12:29 2017

@author: Rishi Raj
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

sat=pd.read_excel('sat.xls')
sat=pd.DataFrame(sat)
sat.drop(['math_SAT','verb_SAT','comp_GPA'],axis=1,inplace=True)

X=sat.drop('univ_GPA',axis=1)
lm=LinearRegression()
lm.fit(X, sat.univ_GPA)

sat2=pd.DataFrame(list(zip(X.columns,lm.coef_)),columns=['fearutes','estimated coefficoents'])

plt.plot(X, sat.univ_GPA,'bo', label='Actual')
plt.plot(X, lm.predict(X) , 'r-', label='Predicted' )
plt.xlabel("High School GPA")
plt.ylabel("University GPA")
plt.show()