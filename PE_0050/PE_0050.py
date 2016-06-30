# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:27:52 2016

@author: michael.hunt
"""

from primes import gen_primes,isprime
           
def cp(n):
    psums=[]
    for p in gen_primes():
        print p
        psum=p
        for p in gen_primes():
            print q
            psum+=q
            if not isprime(psum):
                break
            psum-=q
            psums.append(psum)
#            print  p,psums

#        print  p,psums
        if p>n:
            break