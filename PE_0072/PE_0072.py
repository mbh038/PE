# -*- coding: utf-8 -*-
"""

PE_0072

Counting fractions

How many elements would be contained in the set of reduced proper fractions
for d ≤ 1,000,000?

Created on Wed Jul 20 20:59:59 2016
@author: mbh
"""

from timeit import default_timer as timer
def myfarey(n):
    start=timer()
    a,b=1,1    
    c=n-1
    d=n

    
    count=0
    while a>0:
        k=int((n+b)/d)
        a,b,c,d=c,d,k*c-a,k*d-b
        count+=1
    
#        print count-1, a,b
    print 'Elapsedtime: ',timer()-start,'s'