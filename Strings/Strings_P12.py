# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:06:21 2017

@author: pavantej
"""

def capitalize(string):
    temp_list = list(string)
    for i in range(1 , len(temp_list)):
        if temp_list[i - 1] == ' ' and temp_list[i] != ' ':
            temp_list[i] = temp_list[i].upper()
    temp_list[0] = temp_list[0].upper()        
    return (''.join(temp_list)) 
        