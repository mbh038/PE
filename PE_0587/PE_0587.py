# -*- coding: utf-8 -*-
"""

PE_0587

Concave triangle

Created on Sun Jan 29 12:22:59 2017
@author: mbh
"""

import time
import math
import numpy as np

def p587(target):
    t=time.clock()
    nmin=1
    nmax=5000
    n=(nmax+nmin)//2
    r=ratio(n)
    lastn=nmax
    while abs(lastn-n)>1:
        lastn=n
        if r>target:
            nmin=n
        else:
            nmax=n
        n=(nmax+nmin)//2
        r=ratio(n)
        print(nmin,nmax,r)
    i=0
    while ratio(n+i)>target:
        i+=1
    print((n+i-1,ratio(n+i-1)),(n+i,ratio(n+i)))
    print(time.clock()-t)

def ratio(n):
    """analytically find orange area/blue area"""
    x0,y0=xcross(n),ycross(n)
    theta=math.atan((1-x0)/(1-y0))   
    AC=(y0-theta+math.sin(theta))/2
    AL=1-np.pi/4    
    return AC/AL
    
def xcross(n):
    """returns lowest x value where diagonal line and leftmost circle cross"""
    return n*((n+1)-(2*n)**0.5)/(n**2+1)
    
def ycross(n):
    """returns lowest y value where diagonal line and leftmost circle cross"""
    return xcross(n)/n
    
def f(x):
    """y value of the the concave side, as a function of x""" 
    return 1-(1-(x-1)**2)**0.5
 
#not used
#find the area numerically, using the trapezium rule
def ratio_ni(n):
    """returns ratio of area of orange concave triangle to blue area L"""
    x0,y0=xcross(n),ycross(n)
    CTarea=integrate(x0,1)
    Tarea=0.5*x0*y0
    orange=CTarea+Tarea
    L=1-np.pi/4
    return orange/L
    
def integrate(a,b,nsteps):
    """find area of concave triangle to left of xzero"""
    nsteps=100
    dx=(b-a)/nsteps
    integral=0
    for i in range(1,nsteps):
        xi=a+i*dx
        integral+=2*(f(xi))
    integral+=f(a)+f(b)
    integral*=(b-a)/(2*nsteps)
    return integral
    


    
    
    

    

