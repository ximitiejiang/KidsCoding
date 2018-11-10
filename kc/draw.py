#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 11:36:23 2018

@author: ubuntu

? 是否支持self.a = 1的内部全局变量定义操作
? 调用类里边其他函数，是否需要self.func()的形式，还是func()就可以了

"""

import matplotlib.pyplot as plt

class DRAW():
    """绘图类：可用于绘制直线，圆，矩形，三角形
    
    1. color定义：
        'r' red红色
        'g' green绿色
        'b' blue蓝色
        'y' yellow黄色
        'm' magenta品红
        'c' cyan蓝绿色
        'k' black黑色
    2. line定义：
    3. fill定义：
    4.
    
    """
    
    def __init__(self, figsize=[6,8], ax=None):
        """如果不传进来ax,则默认画在一张图上
           如果需要画在一张新图ax上，需要在创建对象时传进来，所以一个对象只能一个figure
           新图对应新对象
        """
        self.fg1 = plt.figure(figsize=figsize)
        if ax == None: 
            self.ax1 = self.fg1.add_subplot(111)
        else:
            self.ax1 = ax
    
    
    def line(self, x1=[0.,0.], x2=[1.,1.], color='r'):
        x = [x1[0],x2[0]]
        y = [x1[1],x2[1]]
        plt.plot(x,y,color=color)
    
    
    def circle(self, c=[0.,0.],r=1.0,color = 'b',color_in=None):
        from matplotlib.patches import Circle
        cir = Circle(xy = c, radius=r, color=color, fill = color_in)
        self.ax1.add_patch(cir)
        
        
    def ellipse(self, c=[0.,0.],h=2.0,w=1.0,color = 'c', color_in=None,angle=0):
        from matplotlib.patches import Ellipse
        ell = Ellipse(xy = c, width=w, height=h, color=color,fill=color_in,angle=angle)
        self.ax1.add_patch(ell)

    
    def fourpoints(self, x1,x2,x3,x4,color='b'):
        self.line(x1,x2,color=color)
        self.line(x2,x3,color=color)
        self.line(x3,x4,color=color)
        self.line(x4,x1,color=color)
    
    def rectangle(self,x=[0.,0.], h=1.0, w=1.0, color='k',color_in=None):
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
        
        
        
    
    def triangle(self, x1,x2,x3,color='m'):
        self.line(x1,x2,color=color)
        self.line(x2,x3,color=color)
        self.line(x3,x1,color=color)
        

    
if __name__ == '__main__':
    draw = DRAW()
#    draw.rectangle([1,1], 2, 2)
    
#    plt.figure()
#    draw.line([-2,-2], [3,3])
    
    draw.line([-2,-2],[4,4],color='r')
    draw.ellipse([2,2],w=6,h=1.5,color='y',color_in=False,angle=45)
   
#    draw.circle([1,1],1,color='r',color_in=True)
#    plt.figure()
#    draw.rectangle([1,1],[2,1],[2,2],[1,2])
#    draw.triangle([1,1],[3,1],[2,2])