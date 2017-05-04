# -*- coding: utf-8 -*-
"""

PE_0323

 
6.3551758451
Bitwise-OR operations on random integers

Created on Sun Apr 23 07:01:29 2017
@author: mbh
"""

import random as rd
import scipy as sc
import matplotlib.pyplot as plt
import time


def ros(a,b):
    return a*b
    
def p323(n):
    t=time.clock()
    print(round(sum([1-(1-1/2**m)**n for m in range(100)]),10))
    print(time.clock()-t)
    

# in terms of pdf and cdf of gemoetric probabiities  

#cdf is expected values of trials needed for first success (all ones)  
def cdf(n,m):
    return 1-(1-1/2**m)**n

def pdf(n,m):
    return cdf(n,m-1)-cdf(n,m)
    
#expected value
def E(n):
    print( round(sum([m*pdf(n,m) for m in range(1,100)]),10))

#rest not used

def plotter(n):
    aves=[]
    for k in range(2,n+1):
        aves.append(p323sim(k))
    plt.plot(aves)


def p323ran(n) :

    count=0
    Nsum=0
    f='0'+str(n)+'b'
    while 1:
        count+=1
        x=0
        N=0
        while 1:
            N+=1
            y=rd.randint(0,2**n-1)
            x= x|y
#            print(N,y,x)
            if count<100:
                print (N,format(y, f),format(x, f))
            if x==2**n-1:
                Nsum+=N
                break
        ave=Nsum/count
        if count<100:
            print()
#        if not count%1000:
#            print(ave)
        if count>10000000:
            print(n,ave)
            break
    print(ave)
    return (ave)   
    
def p323sim(n):
    
    count=0
    Nsum=0
    f='0'+str(n)+'b'
    while 1:
        count+=1
        x=0
        N=0
        while 1:
            N+=1
            y=rd.randint(0,2**n-1)
            x= x | y
            print (N,format(y, f),format(x, f),sum([int(d) for d in format(x, f)]))
            if x==2**n-1:
                Nsum+=N
                break
        ave=Nsum/count
        print()
#        if not count%1000:
#            print(ave)
        if count>1000000:
            print(n,ave)
            break
    return (ave)
#expectation value of number of batches required if draw  from n coupons in
#batches of m
def p323ros(n,m):
    exp=0
    for l in range(n):
        exp+=(-1)**(n-l+1)*int(sc.misc.comb(n,l))*1/(1-(l/n)**m)
    print(ros(n,m))
    return(exp)
    
#Harmonic number    
def H(n):
    return sum([1/n for n in range (1,n+1)])
    
def ppath(path):
    p=1
    for i in range(len(path)-1):
        p*=(sc.misc.comb(path[i],path[i+1]))/2**path[i]
    return p
    
def npath(path):
    n=1
    for i in range(len(path)-1):
        n*=(sc.misc.comb(path[i],path[i+1]))
    return n
    
def pnm(n,m,turns=False):
    if turns:
        return (2**n)/sc.misc.comb(n,m)
    return sc.misc.comb(n,m)/2**n
    
def allPaths(n):
    paths=[[0]]
    
    for k in range(1,n+1):
        newpaths=[]
        for p in paths:
            newpaths.append(p+[k])
        for p in newpaths:
            paths.append(p)
    for p in newpaths:
        p.reverse()        
    return newpaths
    
def p323main(n):
    nsum,E=0,0
    paths=allPaths(n)
    for path in paths:
        N=len(path)-1
        n=npath(path)
        nsum+=n
        dNp=N*n
        E+=dNp
#        print(path,N,n,dNp)
    return(E,nsum,E/nsum)
        
#    print(paths)


def p323(n):
    t=time.clock()
    print(round(sum([1-(1-1/2**m)**n for m in range(100)]),10))
    print(time.clock()-t)

        
        
            
            
    
        
        

