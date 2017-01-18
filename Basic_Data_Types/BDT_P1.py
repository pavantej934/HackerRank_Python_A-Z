# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 22:55:20 2017

@author: pavantej
"""

a = input()
l = []

for i in range(int(a)):
    b = input().split()
    c = b[0]
    d = b[1:]
    e = ','
    if c != 'print':
       c = c+'('+ e.join(d) + ')'
       eval('l.'+c)
    else:
        print (l)