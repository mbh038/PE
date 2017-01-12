# -*- coding: utf-8 -*-
"""

PE_0504

Squares on the inside

Created on Sat Jan  7 09:08:16 2017
@author: mbh
"""

import time
import itertools as it
import numpy as np
import math


#returns the number of lattice points strictly inside the triangle
#(0,0), (a,0), (0,b).
def lpsi(a,b,gcds):       
    return ((a-1)*(b-1)-gcds[(a,b)]+1)//2    

#returns the number of lattice points strictly inside the polygon
#(0,a), (0,b), (-c,0), (0,-d).
def lpsi4(a,b,c,d):       
    return (a*b+b*c+c*d+d*a-math.gcd(a,b)-math.gcd(b,c)-math.gcd(c,d)-math.gcd(d,a))//2+1
   

def p504(m):
        
    t=time.clock()
    
    #pre-calculate squares, products and gcds
    sqs={x**2 for x in range(1,4*m**2+1)}
    prods={(a,b):a*b for a in range(1,2*m+1) for b in range(1,2*m+1)}
    gcds={(a,b):math.gcd(a,b) for a in range(1,m+1) for b in range(1,m+1)} 
   
    issq=0
    for a,b,c,d in it.product(range(1,m+1),repeat=4):
        if (prods[(a+c),(b+d)]-gcds[(a,b)]-gcds[(b,c)]-gcds[(c,d)]-gcds[(a,d)])//2+1 in sqs:
            issq+=1
    print (issq)

    print(time.clock()-t)

# I also tried using nested lists and numy arrays for storage of pre-calculated
#values, but dictionaries were quicker
#    prods= [[i*j for i in range(m+1)] for j in range(m+1)]
#    prods= np.array([[i*j for i in range(m+1)] for j in range(m+1)])


def squares(limit):
    """return array of square numbers p: 2<=p<=n"""
    sf=np.zeros(limit+1,dtype=bool)        
    for i in range(1, int((limit+1)**0.5+1)):
        sf[i**2]=True
    return np.nonzero(sf)[0]
    
def pfdic(n):
    """returns the distinct prime factors of n as {prime1:exponent1,...}"""   
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i]=factors.get(i,0)+1
    if n > 1:
        factors[n]=factors.get(n,0)+1
    return factors
    
#Euclid algorithm for gcd
def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b
    
def gcd2(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x