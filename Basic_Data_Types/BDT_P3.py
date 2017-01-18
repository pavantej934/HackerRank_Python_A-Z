# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 22:57:06 2017

@author: pavantej
"""

x,y,z,n = (input() for i in range(4))
x,y,z,n = map(int,(x,y,z,n))

result = ([[a,b,c] for a in range(0,x+1) for b in range (0,y+1) for c in range (0,z+1) if a+b+c != n])

print (result)