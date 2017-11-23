# -*- coding: utf-8 -*-
"""

PE_0063

Powerful digit counts

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number,
 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

Created on Wed Jul 13 17:13:54 2016

@author: Mike
"""

import time
import math

def p63():
    t=time.clock()
    a={1: range(1,10)}
    n=1
    while len(a[n])>0:
        n+=1
        a[n]=[x for x in range(1,10) if math.log10(x)>(n-1.0)/n]
    print (sum(len(x) for x in a.values()))
    print (time.clock()-t)