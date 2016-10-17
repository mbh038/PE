# -*- coding: utf-8 -*-
"""
P_0104

Pandigital Fibonacci ends

Given that Fk is the first Fibonacci number for which the first nine digits AND 
the last nine digits are 1-9 pandigital, find k.

Created on Mon Sep 26 15:50:18 2016

@author: mbh
"""
import time
import numpy as np

def p104():
    t=time.clock()
    digits=set('123456789')
    n=0
    last,b=0,1 
    logphi=np.log10((1+np.sqrt(5))/2)
    logroot5=0.5*np.log10(5)
    while 1:       
        n+=1
        last,b=(last+b)%1000000000,last
        if last%9 !=0:
            continue
        if set(str(last))==digits:
            c=10**((n*logphi-logroot5)%1)
            first=str(c)[0]+str(c)[2:11]
            if set(first)==digits:
                break
    print(n,time.clock()-t)
   
#from aolea
def F():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

def aolea():
    t=time.clock()
    n = 0
    target = ['1','2','3','4','5','6','7','8','9']
    
    for i in F():
        a = list(str(i))
        a1 = a[:9]
        a2 = a[-9:]
        a1 = sorted(a1)
        a2 = sorted(a2)
#        print(n,a1,a2,len(a))
        if a1 == target and a2 == target:
            print(n,a1,a2,time.clock()-t)
            break
        n = n + 1
