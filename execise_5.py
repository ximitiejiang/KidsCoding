#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:31:21 2018

@author: suliang
"""

from kc.tool import PAPER, ANT

paper = PAPER(size=[5,5])
leo = ANT(paper)

leo.move(5)
leo.turn_left(90)
leo.move(5)
leo.turn_left(90)
leo.move(5)
leo.turn_left(90)
leo.move(5)
leo.turn_left(90)

leo.jump_to([2,2])

leo.move(3)
leo.turn_left(90)
leo.move(3)
leo.turn_left(90)
leo.move(3)
leo.turn_left(90)
leo.move(3)
leo.turn_left(90)

leo.jump_to([3,3])

leo.move(1)
leo.turn_left(90)
leo.move(1)
leo.turn_left(90)
leo.move(1)
leo.turn_left(90)
leo.move(1)
leo.turn_left(90)











