# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 22:58:41 2017

@author: pavantej
"""

dicn = {}

for _ in range(int(input())):
    temp = input().split()
    dicn[temp[0]] = (temp[1],temp[2],temp[3])
  
desr_marks = dicn[input()]
avg_desr = ((float(desr_marks[0])+float(desr_marks[1])+float(desr_marks[2]))/3)
print ('{0:.2f}'.format(avg_desr))