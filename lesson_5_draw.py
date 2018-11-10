#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:27:05 2018

@author: ubuntu
"""

from kc.draw import DRAW
import matplotlib.pyplot as plt

draw=DRAW(figsize=[6,8])

draw.line([0,1.75],[4,0],color='c')


draw.triangle([0,2],[4,1],[4,0],color='g')


draw.triangle([0,2],[3,0],[4,0],color='y')

draw.rectangle([0,0],h=2,w=1,color='m')


