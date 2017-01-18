# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 22:53:07 2017

@author: pavantej
"""

def is_leap(year):
    leap = False
    
    # Write your logic here
    
    leap = any ([year % 4 == 0 and year % 100 != 0, year % 400 == 0])
    
    return leap