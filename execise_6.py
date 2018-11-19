#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 15:59:40 2018

@author: suliang
"""

from kc.tool import PAPER, DRAW
size = 10
paper = PAPER(size=[size, size])
draw = DRAW(paper)
draw.rectangle([0,0],w=size, h=size,color='k')

for i in range(1,6,1):
    draw.line([2*i-1,i],[2*i+1,i])
    draw.line([2*i,i+1],[2*i,i-1])
