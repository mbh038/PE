#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0285

Pythagorean odds

Created on Mon Dec 25 18:58:55 2017
@author: mbh
"""

import time
import numpy as np
import mpmath
import random as rd
import matplotlib.pyplot as plt


def p285(limit):
    
    t=time.clock()
    
    score =0
    for k in range(1,limit+1):
        score+=k*(cdf((k+0.5)**2,k)-cdf((k-0.5)**2,k))
        
    print (limit,round(score,5))
    print(time.clock()-t)

def cdf(x,k):
    
    if x>=2*(k+1)**2:
        return 1
    if x>=(k+1)**2+1 and x<2*(k+1)**2:
        return (1/(4*k**2))*(-4-8*k+4*(k+1)*(-(k+1)**2+x)**0.5-np.pi*x+4*x*np.arctan((k+1)/(-(k+1)**2+x)**0.5))
    if x>=2 and x <(k+1)**2+1:
        return (1/(2*k**2))*(2-2*(-1+x)**0.5-x*float(mpmath.acsc(x**0.5))+x*np.arctan((-1+x)**0.5))
    else:
        return 0

def simul(k,trials):

    nbin=1000

    rs=[]
    for i in range(trials):
        r=((k*rd.random()+1)**2+(k*rd.random()+1)**2)
        rs.append(r)
    
    pdf, bin_edges = np.histogram(rs, bins=nbin)
    bin_centres = 0.5*(bin_edges[1:] + bin_edges[:-1])
    pdf = np.float_(pdf)
    pdf=pdf*(nbin/(bin_centres[-1]-bin_centres[0]))/trials
    print('Total pdf:',sum(pdf)/(nbin/(bin_centres[-1]-bin_centres[0])))
    F = np.zeros(pdf.shape)
    F=np.cumsum(pdf)/(nbin/(bin_centres[-1]-bin_centres[0]))

    fig, ax1 = plt.subplots()
    plt.xlim([1,2*(k+1)**2+1])
    plt.grid(True)
    ax2 = ax1.twinx()
    ax1.plot(bin_centres[:nbin], pdf, 'g-')  
    ax2.plot(bin_centres[:nbin], F, 'b+')     
    Ftrial=[cdf(x,k) for x in bin_centres[:nbin]]
    ax2.plot(bin_centres[:nbin], Ftrial, 'r-')
    
    ax1.set_xlabel('X')
    ax1.set_ylabel('pdf f', color='g')
    ax2.set_ylabel('cdf F', color='b')
    
    plt.show()
        
def f(x,k,a,d):
    'pdf'
    x = np.asarray(x)
    f = np.zeros(x.shape)
    f += ((x >= d**2) & (x < (k+d)**2+d**2)) * ((1/a)*(1/k)*x**(1/a-1))
    return f

def F(x,k):
    'cdf'
    x = np.asarray(x)
    F = np.zeros(x.shape)
    F += (x>=2*(k+1)**2) * 1
    F += ((x>=(k+1)**2+1) & (x<2*(k+1)**2)) * (1/(4*k**2))*(-4-8*k+4*(k+1)*(-(k+1)**2+x)**0.5-np.pi*x+4*x*np.arctan((k+1)/(-(k+1)**2+x)**0.5))
    F += ((x >= 2) & (x < (k+1)**2+1)) * (1/(2*k**2))*(2-2*(-1+x)**0.5-x*float(mpmath.acsc(x**0.5))+x*np.arctan((-1+x)**0.5))
    return F