#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:20:32 2018

@author: ubuntu
"""
# learn tkint

from kc.tool import PAPER, ANT
paper = PAPER()
eason = ANT(paper)
    
eason.jump_back()

for i in range(50):
    eason.move(i)
    eason.turn_left(90)

#    eason.move(i)
#    eason.turn_left(90)
#    eason.move(2)
#    eason.turn_left(90)
#    eason.move(2)
#    eason.turn.left(90)
