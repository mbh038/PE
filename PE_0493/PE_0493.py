# -*- coding: utf-8 -*-
"""

PE_0493

under the Rainbow

#6.818741802

Created on Wed Apr 19 10:26:00 2017
@author: mbh
"""
import itertools as it
import numpy as np
import random as rd
import time

def p493(n=7,b=10,p=20):
    t=time.clock()
    print(n*b)
    balls=list(range(b+1))
    print(balls)
    ways,count=0,0
    colours={k:0 for k in range(n+1)}
    for a in it.product(balls,repeat=n):
        count+=1
        if(sum(a)==p):
            ways+=1
            bb=np.array(a)
            bb=bb[bb>0]
            print(a,bb,len(bb))
            colours[len(bb)]+=1
    print(count,ways) 
    print(colours)
#    ways=sum([v for k,v in colours.items()])
    meancol=sum([k*v for k,v in colours.items()])/ways
    print(round(meancol,9))
    print(meancol)
    print(time.clock()-t)
    
    
def p493v2(n=7,b=10,p=20):

    trialsum=0
    newave,oldave=1,0
    dps=11
    count=0
    while (abs(newave-oldave)>10**(-dps)):
        count+=1
        np=n*b
        nc=0    
        picks=0
        ncols=0   
        while (picks<p):
            prob_np=np/(np+nc)
#            print(b,prob_np,np,nc)
            if rd.random()<=prob_np:
                ncols+=1
                np -= b
                nc +=(b-1)
            else :
                nc-=1
            picks+=1
        trialsum+=ncols
        oldave=newave
        newave=trialsum/count
        if not count%1000000:
            print(ncols,newave)
            
        

