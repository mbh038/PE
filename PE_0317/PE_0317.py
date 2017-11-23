#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0317

Firecracker

1856532.8455

pi*(2gvh+v^3)^2 / 4g^3

Created on Thu Sep 28 10:45:54 2017
@author: mbh
"""
import time
import math
import numpy as np
import matplotlib.pyplot as plt

def p317(v0=20,y0=100):
    t=time.clock()
    g=9.81
    xmax=ranges(v0,y0)
    ymax=v0**2/(2*g)    
    k=(y0+ymax)/xmax**2    
    vol=(np.pi/(2*k))*(y0**2+y0*v0**2/g+v0**4/(4*g**2))    
    print(vol,time.clock()-t)

#find maximum range for given v0 and yo
def ranges(v0,y0,thetaMax=45,thetaRange=45):
    
    res=0.00000000001
    xmax=100
    xmaxLast=0
    while abs(xmax-xmaxLast)>res:
        xmaxLast=xmax
        xmax=0
        for theta in np.arange(thetaMax-thetaRange,thetaMax+thetaRange,2*thetaRange/100):
            x=xRange(v0,y0,theta)
            if x>xmax:
                xmax=x
                thetaMax=theta
        thetaRange/=10
        
    return xmax

def xRange(v0,y0,theta):
    
    g=9.81
    thetaRad=math.radians(theta)
    vx0=v0*math.cos(thetaRad)
    vy0=v0*math.sin(thetaRad)
    tRise=vy0/g
    yRise=vy0*tRise-0.5*g*tRise**2
    if y0<0 and yRise<abs(y0):
        return 0
    h=y0+yRise
    tFall=(2*h/g)**0.5
    tFlight=tRise+tFall
    x_Range=vx0*tFlight
    
    return x_Range
    

def trajectory(v0,h,theta):
    
    g=-9.81
    thetaRad=math.radians(theta)
    
    dt=0.0001    
    xs,ys=[],[]
    
    t=-dt
    y=100
    while y>-h:
        t+=dt
        y=v0*math.sin(thetaRad)*t+(g*t**2)/2
        if y<-h:
            break
        x=v0*math.cos(thetaRad)*t
        xs.append(x)
        ys.append(y)
        
    plt.plot(xs,ys)
    
    print((theta,xs[-1]))

    

    
    

        