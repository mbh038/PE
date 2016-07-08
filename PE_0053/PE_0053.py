# -*- coding: utf-8 -*-
"""

PE_0053

Combinatoric selections

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater
than one-million?
 
Created on Wed Jul 06 13:53:09 2016

@author: Mike
"""

from timeit import default_timer as timer
from math import factorial

def ncr(n,r):
    return factorial(n)/(factorial(n-r)*factorial(r)) 
    


def cs1():
    start=timer()
    f={}
    f[0]=1
    for n in range(1,101):
        f[n]=f[n-1]*n
    count=0
    for n in range(23,101):
        for r in range(n/2+1):
            if f[n]/(f[r]*f[n-r])>1e6:
                if r!=n/2.:
                    count +=2
                else:
                    count+=1             
    print count   
    print 'Elapsed time: ',timer()-start


def cs2():
    start=timer()
    f={}
    f[0]=1
    for n in range(1,101):
        f[n]=f[n-1]*n
        
    print len([f[n]/f[n-r]*f[r] for n in range(1,101) for r in range(1,n) if ncr(n,r)>1e6])
    print 'Elapsed time: ',timer()-start

def cs3():
    start=timer()
    count = 0 
    C=[]
    C [0:2] = [1,1]
    for n in range(2,101):
        C.append(1)
        for r in range(n -1,0,-1):
            C[r] = C[r] + C[r -1]
            if C[r] > 1000000:
                count += 1
                C[r] = 1000000
    print count
    print 'Elapsed time: ',timer()-start
    
    