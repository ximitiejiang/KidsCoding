#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 15:54:29 2018

@author: suliang
"""

from kc.tool import PAPER,DRAW
size = 10
paper = PAPER(size=[size,size])
draw = DRAW(paper)
draw.rectangle([0,0],w=size, h=size,color='k')

#for i in range(1,6,1):
#    draw.circle([5,5],r=6-i)


#for i in range(1,6,1):
#    draw.rectangle([0,0],w=3*i,h=i)
    
    
for i in range(1,6,1):
    draw.rectangle([2*i-1,9-2*i],w=3,h=3,color='g')
    draw.line([2*i-1,8-2*i],[2*i-1,9-2*i])
    draw.line([2*i+2,12-2*i],[2*i+3,12-2*i])
    draw.circle([2,9],r=0.5,color='b')




