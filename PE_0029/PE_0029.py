# -*- coding: utf-8 -*-
"""

PE_0029

Distinct Powers

How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and
 2 ≤ b ≤ 100?
 
Created on Sun Jun 26 11:42:41 2016

@author: Mike
"""
import time
import numpy as np
times=[]
for i in range(100):
    import time
    start_time = time.time()
    
    aas=range(2,101)
    bbs=range(2,101)
    terms=[]
    for a in aas:
        for b in bbs:
            terms.append(a**b)
    uterms=set(terms)
#    print len(uterms)
    times.append(time.time() - start_time)
print len(uterms)
print("--- %s seconds ---" % np.mean(times)) 



