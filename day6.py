# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 14:59:04 2022

@author: bskal
"""

a=[10,15,3,7]
k=17
h=0

for j in range(len(a)):
    for l in range(len(a)):
        
        if(a[j]+a[l]==k):
            h=h+1
            break
        else:
            h=-1
if(h>=0):
    print('true')
else:
    print('false')



