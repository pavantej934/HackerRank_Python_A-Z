# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:02:34 2017

@author: pavantej
"""

s_org,s_sub = input(),input()
count = 0

for i in range(len(s_org)):
    if s_org[i:i+len(s_sub)] == s_sub:
        count += 1
        
print (count)
    
