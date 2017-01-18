# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:01:44 2017

@author: pavantej
"""

s = input()

i = input().split()

t = s[:(int(i[0]))] + i[1] + s[(int(i[0])+1):]

print (t)