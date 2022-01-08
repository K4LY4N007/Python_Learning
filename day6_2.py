# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 14:48:32 2022

@author: bskal
"""

a=[]
n=int(input("enter the number of list elements: "))
for i in range(0,n):
    a.append(int(input("enter the elements: ")))
print("\nyour input is: ",a)
k=[]
result=1

for i in range(len(a)):
    for j in range(0,len(a)):
        if(i==j):
            continue
        result=result*a[j]
    k.append(result)
    result=1

print("\nyour expected output is: ", k)
        
        