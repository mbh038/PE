# -*- coding: utf-8 -*-
"""

PE_0144

Investigating multiple reflections of a laser beam

Created on Mon Jan 30 07:21:45 2017
@author: mbh
"""

import time
import math

def p144(apertureWidth=0.02):
    
    t=time.clock()
   
    a=(0,10.1)
    b=(1.4,-9.6)    
    mi=gradient(a,b) #initial gradient of beam
    
    n=0
    while 1:
        n+=1        
        c=beamc(a,mi) #intercept of beam, as in y=mx+c
        a=nextImpactAt(a,mi,c) #next point of impact
        if abs(a[0])<apertureWidth/2 and a[1]>0: #has the beam struck the aperture
            n-=1
            break
        mi=reflectedBeamGradient(a,mi) #gradient of reflected beam

    print (n)
    print (time.clock()-t)

def gradient(a,b):
    """a,b are both 2-tuples of points on the line"""
    x1,y1=a[0],a[1]
    x2,y2=b[0],b[1]
    return (y2-y1)/(x2-x1)

def beamc(a,m):
    """return intercept coefficient of line equation for beam given that it passes through a=(x0,y0) and has gradient m"""
    x0,y0=a[0],a[1]
    return y0-m*x0
    
def nextImpactAt(a,m,c):
    """find next point of impact given line has gradient m, intercept c and comes from a=x0,y0"""
    epsilon=0.000001    
    discriminant=((m**2*c**2-(4+m**2)*(c**2-100)))**0.5    
    x1a=(-m*c+discriminant)/(4+m**2)
    x1b=(-m*c-discriminant)/(4+m**2)    
    y1a=m*x1a+c
    y1b=m*x1b+c    
    if abs(x1a-a[0])<epsilon:
        return (x1b,y1b)
    else:
        return (x1a,y1a)
    
def reflectedBeamGradient(a,mi):
    """returns exit slope of beam if impacts at a and arrives with slope mi"""
    x,y=a[0],a[1]
    ms=-4*x/y #gradient of surface at point of impact
    mb=math.tan(2*math.atan(ms)-math.atan(mi))
    return mb


def reflectedBeamVector(a,Vi):
    """returns exit slope of beam if impacts at a and arrives with vector Vi"""
    x,y=a[0],a[1]
    m=-4*x/y


    return Vr
    
#vector version
#R=I-2(I.N)N
def p144v(apertureWidth=0.02):
    pass
    
    