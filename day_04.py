# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 18:50:19 2021

@author: bskal
"""

import pandas as pd
import json
import csv
json_path_file=r"C:\Users\bskal\OneDrive\Desktop\icc_results.json"
with open(json_path_file,"r") as f:
    data = json.load(f)

print(data)

content=pd.read_json(json_path_file)
for k in content.columns:
    print (k)

reviewed = content.groupby(['label','timestamp','tournamentLabel','resultOnly'])
print(reviewed)

with open(r"C:\Users\bskal\OneDrive\Desktop\file.csv","w") as h:
    
    csvwriter = csv.writer(h) 
        
    # writing the fields 
    for i in reviewed:
        csvwriter.writerows(i) 



df = pd.DataFrame(data)


df['tournamentLabel']





df = pd.read_csv(r"C:\Users\bskal\Downloads\archive\AXISBANK.csv")


df.describe()




def d_t_b(decimal):
    return bin(decimal)


d_t_b(100)


func = lambda x,y: bin(x)+bin(y)
func(10,100)

