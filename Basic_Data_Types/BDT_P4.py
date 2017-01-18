# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 22:57:37 2017

@author: pavantej
"""

n = input()

l = sorted(map(int,input().split()))
ind = l.index(max(l))
print (l[ind-1])
