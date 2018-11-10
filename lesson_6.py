#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:20:32 2018

@author: ubuntu
"""
from kc.draw import DRAW
import matplotlib.pyplot as plt
draw = DRAW(figsize=[6,13])

    
plt.xlim(-1,6)
plt.ylim(0,16)

for i in range(10):
    draw.circle([3,3+1*i],r=2)
    
