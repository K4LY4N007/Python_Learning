# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:03:35 2021

@author: bskal
"""


import pandas as pd


df = pd.read_csv(r"C:\Users\bskal\Downloads\AXISBANK.csv")

df.std() < 2.5
sp=2.5

df=df.drop(df.std()[df.std()<sp].index.values, axis=1)

df.std() < 2.5

df = df['Prev Close']

df.std()

df.max()
df.min()

ub = df.std()*2.5
#lb = df.mean()-df.std()*2.5


x = df[df<ub]



