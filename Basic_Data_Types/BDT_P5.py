# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 22:58:12 2017

@author: pavantej
"""

marksheet = []

for _ in range(int(input())):
    marksheet.append((input(),float(input())))

marks = [b for (a,b) in marksheet]
marks = sorted(list(set(marks)))
ind = marks.index(min(marks))
second_lowest_marks = marks[ind+1]

req_names = [a for (a,b) in marksheet if b == second_lowest_marks]
req_names.sort()

for i in range(len(req_names)):
    print (req_names[i])
                     