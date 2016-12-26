# -*- coding: utf-8 -*-
"""

PE_0148

Exploring Pascal's triangle

Created on Thu Dec 22 08:56:49 2016
@author: mbh
"""

import numpy as np
import time
   
def p148(n,base=7):
    t=time.clock()
    s=str(np.base_repr(n,base))
    m=sum([x for x in range(1,base+1)])
    bsum=0
    smult=1
    for i in range(len(s)):
        if i>0:
            smult*=(int(s[i-1])+1)
        bsum+=m**(len(s)-i-1)*smult*sum([x for x in range(int(s[i])+1)])
    print(bsum,time.clock()-t)

def p148bf(n,base=7):
    t=time.clock()
    sum7=0
    for i in range(n):
        sum7+=np.prod([int(x)+1 for x in str(np.base_repr(i,base))])
    print(n,sum7,time.clock()-t)
    return sum7
    
    
#to see number odd numbers mod n) in first m rows
#sum([sum([nCk(y,x)%n!=0 for x in range(y+1)]) for y in range(m)])