# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 22:59:58 2017

@author: pavantej
"""

s_original = input()

s_swap_asc = []
s_swap = []
s_original_asc = [ord(i) for i in s_original]

for j in s_original_asc:
    if 65 <= j <= 90:
        j = j + 32
        s_swap_asc.append(j)
    elif 97 <= j <= 122:
        j = j - 32
        s_swap_asc.append(j)
    else:
        s_swap_asc.append(j)
        
for k in range(len(s_swap_asc)):
    s_swap.append(chr(s_swap_asc[k]))
    
print (''.join(s_swap))