#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0349

Langton's Ant

An ant moves on a regular grid of squares that are coloured either black or white.
The ant is always oriented in one of the cardinal directions (left, right, up or down) 
and moves from square to adjacent square according to the following rules:
    
- if it is on a black square, it flips the color of the square to white, rotates 
90 degrees counterclockwise (left) and moves forward one square.

- if it is on a white square, it flips the color of the square to black, rotates 
90 degrees clockwise (right) and moves forward one square.

Starting with a grid that is entirely white, how many squares are black after 
10^18 moves of the ant?

Created on Fri Sep 22 15:45:07 2017

@author: mbh
"""

import matplotlib.pyplot as plt
import numpy as np
import time

#how many squares are black after n steps?
def p349(n,width=150,height=150):
    
    t=time.clock()
    
    dir=0  #up
    nsteps=12000
    
    x=width//2
    y=height//2
    
    M=[[0]*width for _ in range(height)]
    
    i=0
    
    blackSum=np.array([0])
    
    while i<nsteps and 0 <=x<width and 0<= y <height:
        
        #what new direction?
        #[0,1,2,3] mean [up,left,down,right]
        if M[y][x]==0:
            dir=(dir-1)%4
        else:
            dir=(dir+1)%4
            
        #what colour to make the new cell?
        if M[y][x]==1:
            M[y][x]=0
            blackSum=np.append(blackSum,-1)
        else:
            M[y][x]=1
            blackSum=np.append(blackSum,1)
            
        #what change in coordinates?
        if dir==0:
            y-=1
        elif dir==1:
            x-=1
        elif dir==2:
            y+=1
        elif dir==3:
            x+=1
            
        i+=1
        
#    plt.contourf(M)

    #bc[n] gives the number of black cells after n steps
    bc=np.cumsum(blackSum)
    
    #calculate how many balck cells for any n>10,000, given the value at n=10,000
    #and given an increment of 12 every 104 steps once on the highway.
    print(12*((n-10000)//104)+bc[10000+(n-10000)%104])
    print(time.clock()-t)
    
    return bc

#The oop version I found on RosettaCode
class Dir: up, right, down, left = range(4)
class Turn: left, right = False, True
class Colour: white, black = 0,1#'.', '#'

def p349Rosetta(n,width=100,height=100):
    
    t=time.clock()
    
    nsteps=11000
    dir=Dir.up
    
    M=[[Colour.white] *width for _ in range(height)]
    
#    print ("/n".join("".join(row) for row in M))
    
    x=height//2
    y=width//2
    
    i=0
    blackSum=[0]
    
    while i<nsteps and 0 <=x<width and 0<= y <height:
        turn=Turn.left if M[y][x]==Colour.black else Turn.right
        if M[y][x]==Colour.black:
            M[y][x]=Colour.white
            blackSum.append(-1)
        else:
            M[y][x]=Colour.black
            blackSum.append(1)
        
        dir=(4+dir+(1 if turn else -1))%4
        dir=[Dir.up,Dir.right,Dir.down,Dir.left][dir]
        if dir==Dir.up: y-=1
        elif dir==Dir.right: x-=1
        elif dir ==Dir.down: y+=1
        elif dir == Dir.left: x+=1
        else: assert False
        i+=1
        
        
    plt.contourf(M)
    bc=np.cumsum(np.array(blackSum))
    print(12*((n-10000)//104)+bc[10000+(n-10000)%104])
    print(time.clock()-t)
#    print ("/n".join("".join(str(row)) for row in M))
        
    
    
def bcalc(n,bc):
    
#    return bc[10000]+58*((n-10000)//104)+bc[10000+(n-10000)%104]-bc[10000]

    return 12*((n-10000)//104)+bc[10000+(n-10000)%104]

#code by Peter de Rivaz
import collections as cl
def euler349():
   x,y=0,0
   dx,dy=1,0
   D=cl.defaultdict(int)   # white=0
   for i in range(20000):
      key=x,y
      if D[key]==0:
         D[key]=1
         dx,dy=-dy,dx
      else:
         D[key]=0
         dx,dy=dy,-dx
      x+=dx
      y+=dy