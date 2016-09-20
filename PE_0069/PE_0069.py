# -*- coding: utf-8 -*-
"""

PE_0069

Totient maximum: Euler's totient function

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

Created on Mon Jul 18 04:04:58 2016
@author: mbh
"""

from primes import prime_factors,primesfrom2to,erat2a
from timeit import default_timer as timer

def tlist():
    
    hands=[]
    fhand = open('et100000.txt')
    for line in fhand.read().split('\n'):
        hands.append(line.split(' '))   
    ratio= {int(x[0]):[int(x[1]),float(int(x[0]))/int(x[1])] for x in hands[:100000]}      
    print (ratio[100])    
    print (keywithmaxval(ratio),ratio[keywithmaxval(ratio)])
    
def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=[x[1] for x in d.values()]
     k=list(d.keys())
     return k[v.index(max(v))]

def p69(n):
    
    start=timer()
    
    et={}
    phis={}

    for i in primorial(n):
        et[i]=list(set(prime_factors(i)))
        
    for i in et:
        phi=i
        for x in et[i]:
            phi*=(1-1/float(x))
        phis[i]=[phi,float(i)/phi]
  
    v=[x[1] for x in phis.values()]
    k=list(phis.keys())
    kmax= k[v.index(max(v))]
       
    print (kmax,phis[kmax])
    print ('Elapsed time: ',timer()-start,'s')


def primorial(n):
    p = erat2a()
    
    primorial=[1]
    while primorial[-1]<n:
        primorial.append(primorial[-1]*next(p))
    return primorial[:-1]
        
