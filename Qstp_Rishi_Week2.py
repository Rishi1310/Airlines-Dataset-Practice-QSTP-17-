# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:21:24 2017

@author: Rishi Raj
"""

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

database = pd.read_csv("database.csv",low_memory=False)

#1st Answer
weapon_groups=pd.crosstab(database.Year,database.Weapon,margins=True)
weapon_groups=weapon_groups.iloc[0:len(weapon_groups)-1]
handgun=weapon_groups['Handgun']
knife=weapon_groups['Knife']
blunt=weapon_groups['Blunt Object']
firearm=weapon_groups['Firearm']
handgun.plot(kind='line',label='Handgun',legend=True)
knife.plot(kind='line',label='Knife',legend=True)
blunt.plot(kind='line',label='Blunt Object',legend=True)
firearm.plot(kind='line',label='Firearm',legend=True)
plt.show()

#2nd Answer
relationship_groups=pd.crosstab(database.Year,database.Relationship,margins=True)
relationship_groups=relationship_groups.iloc[0:len(relationship_groups)-1]
Acquaintance=relationship_groups['Acquaintance']
Stranger=relationship_groups['Stranger']
handgun.plot(kind='line',label='Acquaintance',legend=True)
knife.plot(kind='line',label='Stranger',legend=True)
plt.show()

#3rd Answer
db2=database[database["Weapon"] != "Unknown"]
sb.boxplot(x=db2['Year'],y=db2['Weapon'])
plt.show()