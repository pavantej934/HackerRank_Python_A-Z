# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:04:18 2017

@author: pavantej
"""

import textwrap

s = input()
w = int(input())

print (textwrap.fill(s,w))