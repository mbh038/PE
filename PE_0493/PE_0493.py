# -*- coding: utf-8 -*-
"""

PE_0493

Under the Rainbow

#6.818741802

Created on Wed Apr 19 10:26:00 2017
@author: mbh
"""
import itertools as it
import numpy as np
import scipy as sc
import time


# the neat combinatoric way
def p493comb(nColours=7,perColour=10,picks=20):
    
    t=time.clock()

    #consider one colour after p picks:
    #number of ways to not pick that colour:
    nNotPickOneColour=int(sc.misc.comb((nColours-1)*perColour,picks))
    #number of ways to pick any colour:
    nAnyColour=int(sc.misc.comb(nColours*perColour,picks))    
    #probability of not picking that colour
    probNotPickoneColour=nNotPickOneColour/nAnyColour    
    #probability that that colour is picked
    probPickoneColour=1-probNotPickoneColour
    
    #so for all balls...
    #expectation value of number of colours picked
    expColours=nColours*probPickoneColour
    
    print(round(expColours,9))
    print(time.clock()-t)  #0.1 ms

#counting possibilities
def p493(n=7,b=10,p=20):
    
    t=time.clock()

    nCks=[int(sc.misc.comb(b,k)) for k in range(b+1)]
    colours={k:0 for k in range(n+1)}
    
    for a in it.product([x for x in range(b+1)],repeat=n):
        if(sum(a)==p):
            valid=np.array(a)
            valid=valid[valid>0]
            newWays=np.prod(np.array([nCks[x] for x in valid]))
            colours[len(valid)]+=newWays
    meancol=sum([k*v for k,v in colours.items()])/sum([v for k,v in colours.items()])
    print(round(meancol,9),time.clock()-t)

    
#Markov chain 
import random as rd
import matplotlib.pyplot as plt
def p493v2(n=7,b=10,p=20):

    trialsum=0
    newave,oldave=1,0
    aves=[]
    dps=8
    count=0
    while (abs(newave-oldave)>10**(-dps)):
        count+=1
#        print("Count: ",count)
        newColour=n*b
        noChange=0    
        picks=0
        ncols=0   
        while (picks<p):
            prob_np=newColour/(newColour+noChange)
#            print(b,prob_np,np,nc)
            if rd.random()<prob_np:
                ncols+=1
                newColour -= b
                noChange +=(b-1)
            else :
                noChange-=1
            picks+=1
#            print(picks,ncols,newColour,noChange)
        trialsum+=ncols
        oldave=newave
        newave=trialsum/count
        aves.append(newave)
#        if not count%10000:
#            print(ncols,newave)
#        print(ncols,newave)
        if count > 200000:
            break
    print(newave)   
    plt.plot(aves)
            

