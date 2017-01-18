# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:03:01 2017

@author: pavantej
"""

l = input()

p1 = p2 = p3 = p4 = p5 = False
for i in l:
    p1 = p1 or i.isalnum()
    p2 = p2 or i.isalpha()
    p3 = p3 or i.isdigit()
    p4 = p4 or i.islower()
    p5 = p5 or i.isupper()

print (p1)
print (p2)
print (p3)
print (p4)
print (p5)