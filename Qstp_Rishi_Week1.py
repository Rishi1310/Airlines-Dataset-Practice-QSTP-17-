# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 15:40:06 2017

@author: Rishi Raj
"""

import pandas as pd
import seaborn as sb

database = pd.read_csv("database.csv",low_memory=False)

#1st Answer
print ("1st Ans: \nNo. of crimes solved = %d\n"%(database["Crime Solved"].value_counts().Yes))
print ("\n\n")

#2nd Answer
db2=database[database["Weapon"] != "Unknown"]
a=db2["Weapon"].value_counts().index.tolist()[0:5]
print ("2nd Ans: \nThe top five weapons used are")
for i in range(len(a)):
    print (a[i])
print ("\n\n")

#3rd Answer
b=pd.crosstab(database.State,database.Weapon,margins=True)
d=len(b.iloc[0])-1

for i in range(0,len(b)-1):
      c=(b.iloc[i]/b.iloc[i][d]).sort_values(ascending=False)*100
      print ("For the state, " + b[i:i+1].index[0] + ", the most commonly used weapon is, " + c.keys()[1] + ", with a useage of, " + str(c[1]) +"%")
print ("\n\n")
      
#4th Answer
print ("The barplot for the number of homcides by the year is as follows:")
m=database["Year"].value_counts()
n=pd.DataFrame({'Year':m.keys(),'Frequency':m}).sort_values(by=['Year'],ascending=True)
sb.barplot(n['Year'],n['Frequency'])