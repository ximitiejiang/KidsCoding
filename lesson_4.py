#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 21:24:28 2018

@author: ubuntu

for

"""

# 复习range
list(range(10))

# learn ant draw
from kc.tool import PAPER, ANT

paper = PAPER(size=[6,8])
ant = ANT(paper)

# draw steps
ant.move(2)
ant.turn_left(90)
ant.move(2)
ant.turn_right(90)
ant.move(2)
ant.turn_left(90)
ant.move(2)
ant.turn_right(90)
ant.move(2)

# draw rectangle
ant.move(2)
ant.turn_left(90)
ant.move(2)
ant.turn_left(90)
ant.move(2)
ant.turn_left(90)
ant.move(2)
ant.turn_left(90)

# cycle learning
for i in range(12):
    ant.move(2)
    ant.turn_left(30)
    
# cycle learning: change dimension
for i in range(12):
    ant.move(i)
    ant.turn_left(90)
    ant.move(i)
    ant.turn_left(90)
    ant.move(i)
    ant.turn_left(90)
    ant.move(i)
    ant.turn_left(90)    
