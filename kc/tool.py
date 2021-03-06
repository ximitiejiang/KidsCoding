#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 11:36:23 2018

@author: ubuntu

"""

import matplotlib.pyplot as plt
import numpy as np

class PAPER():
    def __init__(self,size=[6,8]):
        self.figsize=size
        self.fig1 = plt.figure(figsize=self.figsize)
        self.ax1 = self.fig1.add_subplot(111)

class DRAW():
    """绘图类：适合于结合坐标的绘图方式
    可用于绘制直线，圆，矩形，三角形    
    1. color定义：
        'r' red红色
        'g' green绿色
        'b' blue蓝色
        'y' yellow黄色
        'm' magenta品红
        'c' cyan蓝绿色
        'k' black黑色
    
    """
    def __init__(self, paper):
        self.paper = paper
        
    def line(self, x1=[0.,0.], x2=[1.,1.], color='r'):
        x = [x1[0],x2[0]]
        y = [x1[1],x2[1]]
        plt.plot(x,y,color=color)
    
    
    def circle(self, c=[0.,0.],r=1.0,color = 'b',fill_in=None):
        from matplotlib.patches import Circle
        cir = Circle(xy = c, radius=r, color=color, fill = fill_in)
        self.paper.ax1.add_patch(cir)
        
        
    def ellipse(self, c=[0.,0.],h=2.0,w=1.0,color = 'c', fill_in=None,angle=0):
        from matplotlib.patches import Ellipse
        ell = Ellipse(xy = c, width=w, height=h, color=color,fill=fill_in,angle=angle)
        self.paper.ax1.add_patch(ell)

    
    def fourpoints(self, x1,x2,x3,x4,color='b'):
        self.line(x1,x2,color=color)
        self.line(x2,x3,color=color)
        self.line(x3,x4,color=color)
        self.line(x4,x1,color=color)
    
    
    def rectangle(self,x=[0.,0.], h=1.0, w=1.0, color='k',fill_in=None):
        '''x为左下角坐标，h为高，w为宽
        '''
        xlb = [x[0],x[1]]
        xlt = [x[0],x[1]+h]
        xrt = [x[0]+w,x[1]+h]
        xrb = [x[0]+w,x[1]]
        
        self.line(xlb,xlt,color=color)
        self.line(xlt,xrt,color=color)
        self.line(xrt,xrb,color=color)
        self.line(xrb,xlb,color=color)
        
        if fill_in:
            plt.fill_between([x[0],x[0]+w],
                             [x[1],x[1]],
                             [x[1]+h,x[1]+h], facecolor=color)        
        
    
    def cal_triangle_midy(self,x):
        '''input = ndarray (3x1) with x cordinate sorted.
           output:
               输出三角形中间点垂直切到对应边的切割点y坐标，该切割点x坐标与中间点相同
        '''
        x1 = x[0,0]
        x2 = x[1,0]
        x3 = x[2,0]
        y1 = x[0,1]
        y3 = x[2,1]
        mid_y = (y3*(x2-x1) + y1*(x3-x2))/(x3-x1)
        return mid_y
        
    
    def triangle(self, x1,x2,x3,color='m',fill_in=None):
        self.line(x1,x2,color=color)
        self.line(x2,x3,color=color)
        self.line(x3,x1,color=color)
        
        if fill_in:
            import numpy as np
            x = np.vstack((x1,x2,x3))
            index = np.argsort(x[:,0])                 # x坐标从小到大排序
            x_new = x[(index[0],index[1],index[2]),:]  # 调换坐标顺序
            mid_y = self.cal_triangle_midy(x_new)
            plt.fill_between(x_new[:,0],
                             [x_new[0,1],mid_y,x_new[2,1]],
                             x_new[:,1], 
                             facecolor=color)    
    
class ANT():
    """蚂蚁类：适合于更简单直观的绘图方式
    """
    def __init__(self,paper, x0=[1,1]):
        self.home = [x0[0],x0[1]]              # 避免浅拷贝
        self.x0 = [self.home[0],self.home[1]]     
        self.x1 = [x0[0],x0[1]]
        self.angle = 0
        self.paper = paper
    
    def line(self, x1=[0.,0.], x2=[1.,1.], color='r'):
        x = [x1[0],x2[0]]
        y = [x1[1],x2[1]]
        plt.plot(x,y,color=color)
        
    def move(self,l,color='r'):
        self.x1[0] = self.x0[0] + l*np.cos(self.angle)
        self.x1[1] = self.x0[1] + l*np.sin(self.angle)
        
        self.line(self.x0, self.x1, color=color)
        
        self.x0[0]=self.x1[0]
        self.x0[1]=self.x1[1]
    
    def turn_left(self,turnleft):
        self.angle += turnleft*np.pi/180
        
    def turn_right(self,turnright):
        self.angle -= turnright*np.pi/180
    
    def turn_round(self):
        self.angle += 180*np.pi/180
    
    def jump_back(self, x=[1,1]):
        self.x0 = [self.home[0],self.home[1]]     
        self.x1 = [self.x0[0],self.x0[1]]
        self.angle = 0
        
    def jump_to(self, x):
        self.x0[0]=x[0]
        self.x0[1]=x[1]
        self.angle=0
    
if __name__ == '__main__':
    paper = PAPER()
    draw = DRAW(paper)
    ant = ANT(paper)
#    plt.xlim(-1,8)
#    plt.ylim(0,6)

    draw.rectangle([1,1],w=3,h=4,color='g',fill_in=True)    
    draw.triangle([1,1],[4,2],[2,5],color='b',fill_in=True)
    
    ant.jump_back()
    for i in range(10):
        ant.move(i+1)
        ant.turn_right(90)
        ant.move(i+1)
        ant.turn_right(90)
        ant.move(i+1)
        ant.turn_right(90)
        ant.move(i+1)
        ant.turn_right(90)
    
        
        
        