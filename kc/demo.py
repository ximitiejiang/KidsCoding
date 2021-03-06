#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 11:44:20 2018

@author: ubuntu
"""
from tool import PAPER, DRAW, ANT
import matplotlib.pyplot as plt

def draw_robot():
    
    paper = PAPER(size=[6,8])
    draw = DRAW(paper)
    
    plt.xlim(-1,6)
    plt.ylim(0,6)

    # draw hat
    draw.triangle([2.4,5.75],[1.85,5],[2.85,5],fill_in=True)
    
    # draw head
    draw.rectangle([1.75,4],h=1,w=1.2)
    draw.circle([2.7,4.5],r=0.1,color='r',fill_in=True)
    draw.circle([2.0,4.5],r=0.1,color='r',fill_in=True)
    draw.line([2.25,4.2],[2.5,4.2])
        
    # draw boday
    draw.rectangle([1.5,1.5],h=2.45,w=1.8,color='c',fill_in=True)
    
    # draw legs
    draw.rectangle([1.5,0], h=1.5,w=0.5,color='m',fill_in=True)
    draw.rectangle([2.8,0], h=1.5,w=0.5,color='m',fill_in=True)
    
    #draw arms
    draw.ellipse([0.6,3],w=3,h=1,color='g',fill_in=True,angle=60)
    draw.ellipse([4.2,3],w=3,h=1,color='g',fill_in=True,angle=120)   
    

def ant_dance():
    paper = PAPER(size=[6,8])
    ant = ANT(paper)
    
    ant.jump_to([2,2])
    for i in range(40):
        ant.move(5)
        ant.turn_left(160)
        ant.move(5)
        ant.turn_round()
        ant.turn_left(30)
      

draw_robot()

ant_dance()
