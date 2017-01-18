# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:05:20 2017

@author: pavantej
"""

n = int(input())

l = len(str(bin(n)[2:]))

for i in range(1,n+1):
    print (str(i).rjust(l) , str(oct(i)[2:]).rjust(l) , (str(hex(i)[2:])).upper().rjust(l) , str(bin(i)[2:]).rjust(l))