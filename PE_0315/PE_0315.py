#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

P_0315

Digital root clocks

Created on Tue Jan 16 20:00:17 2018
@author: mbh
"""

import numpy as np
import time

def p315(N):
    
    t=time.clock()
    
    ps=primeSieve(2*10**N)
    ps=ps[ps>10**N]
        
    d1dic={p:sum([int(d) for d in str(p)]) for p in ps}    
    d1dests=set([v for k,v in d1dic.items()])
    d2dic={p:sum([int(d) for d in str(p)]) for p in d1dests}
    d1dic.update(d2dic)
    d2dests=set([v for k,v in d2dic.items()])
    d3dic={p:sum([int(d) for d in str(p)]) for p in d2dests}
    d1dic.update(d3dic)
   
    bars={0:[1,1,1,1,1,1,0],1:[1,1,0,0,0,0,0],2:[0,1,1,0,1,1,1],3:[1,1,1,0,0,1,1],4:[1,1,0,1,0,0,1],
          5:[1,0,1,1,0,1,1],6:[1,0,1,1,1,1,1],7:[1,1,1,1,0,0,0],8:[1,1,1,1,1,1,1],9:[1,1,1,1,0,1,1]}
    barsums={k:sum(v) for k,v in bars.items()}
    barDiffs={}
    for k in bars:
        barDiffs[k]=[]
        for j in bars:
            barDiffs[k].append(7-sum([a == b for a,b in zip(bars[k],bars[j])]))

    #Sam
    samSum=0
    for p in ps:
        psum=0
        dest=p
        trail=[p]
        while dest>=10:
            dest=d1dic[dest]
            trail.append(dest)
        for n in trail:
            for d in str(n):
                psum+=2*barsums[int(d)]
        samSum+=psum
    print(samSum)
  
    #Max
    maxSum=0
    for p in ps:
        psum=0
        dest=p
        trail=[p]
        while dest>=10:
            dest=d1dic[dest]
            trail.append(dest)
        psum=sum([barsums[int(d)] for d in str(trail[0])])+sum([barsums[int(d)] for d in str(trail[-1])])
        for i in range(len(trail)-1):
            l0=len(str(trail[i]))
            l1=len(str(trail[i+1]))
            nextDigit=['0']*(l0-l1)+[d for d in str(trail[i+1])]
            for d in str(trail[i])[:l0-l1]:
                psum+=barsums[int(d)]
            for j in range(l0-l1,len(str(trail[i]))):
                psum+=barDiffs[int(str(trail[i])[int(j)])][int(nextDigit[j])]
        maxSum+=psum
    print(maxSum)
    
    print(samSum-maxSum)
    print(time.clock()-t)

def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]


