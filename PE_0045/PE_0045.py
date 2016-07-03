# -*- coding: utf-8 -*-
"""

PE_0045

Triangular, pentagonal, and hexagonal

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
Created on Sat Jul 02 02:56:50 2016

@author: Mike
"""
import math as m
def tph(nmin=285,nmax=100000):
    n=nmin
    delta=0.0001
    while n<nmax:
        n+=1
        T=n*(n+1)/2
        pmin,pmax=int(n*(1-delta)/m.sqrt(3)),int(n*(1+delta)/m.sqrt(3))
        for p in range (pmin,pmax):
            P=p*(3*p-1)/2
            if P==T:
                hmin,hmax=int(n*(1-delta)/2),int(n*(1+delta)/2)
                for h in range (hmin,hmax):
                    H=h*(2*h-1)
                    if H==T:
                        print 'Found it !!'
                        print 'n,T ',n,T
                        print 'p,P ',p,P
                        print 'h,H ',h,H
                        break
                
        
import time 
#def main ():
#    start_time = time.time()
#    tph()
#    print("--- %s seconds ---" % (time.time() - start_time))
    
#main()
       
        
#from Sevilla

from time import time
from math import sqrt

def hexagonal_numbers(n=1):
    if n < 1: n == 1
    while True:
        yield n*(2*n-1)
        n+=1

def is_pentagonal(num):
    n = (sqrt(24*num+1)+1)/6
    return n == int(n) 

    
def main():
    gen = hexagonal_numbers(144)
    while True:
        H = next(gen)
        if is_pentagonal(H):
            print(H)
            break
        
#if __name__ == '__main__':
#    t0 = time()
#    main()
#    print('Elapsed time:', time()-t0)

    

# from nupri - this is brilliant
t0 = time()
from itertools import count

pentagonal_delta = count(1, 5-2)
hexagonal_delta = count(1, 6-2)
p = 0
h = 0
while not p == h > 40755:
    if p <= h:
        p += next(pentagonal_delta)
    if h < p:
        h += next(hexagonal_delta)

print(p)
print('Elapsed time:', time()-t0)