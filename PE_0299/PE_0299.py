#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0299

Three similar triangles

Created on Sat Oct 28 06:33:01 2017
@author: mbh
"""

import math
import time

def bdList(limit=10**8):
    
    t=time.clock()
    
    pairs=[]
    for m in range(1,int(limit**0.5+1)):
        for n in range(1,m):
            if math.gcd(m,n)!=1:
                continue
            if m%2 ==n%2:
                continue
            b=m*m-n*n
            d=2*m*n
            if b+d>limit:
                break
            k=1
            while (k*(b+d)<limit):
                pairs.append((k*b,k*d))
                pairs.append((k*d,k*b))
                k+=1
                
    print(time.clock()-t)
    return pairs

