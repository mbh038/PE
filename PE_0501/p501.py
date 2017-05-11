# -*- coding: utf-8 -*-
"""

p501

Created on Tue May  9 23:53:13 2017
@author: mbh
"""

import time
from my_math import *

def p501(n):
    
    t=time.clock()
    
    #3 factors
    count3=0
    p=2
    while p<=n/6:
        q=next_prime(p,proof=False)
        while q<=(n/p)**0.5:
            r=next_prime(q)
            while p*q*r<=n:
#                if p !=q and p !=r and q !=r:
                count3+=1
#                    print(p,q,r)
                r=next_prime(r)
            q=next_prime(q)
        p=next_prime(p)
    print(count3)    

    count2=0
    p=2
    while p<=n**(1/4):
        q=next_prime(p)
        while q<=(n/p)**(1/3):
#            if p*q**3<= n:#  and p != q):
            count2+=1
            q=next_prime(q)
        p=next_prime(p)
    print(count2)
#    return
    p=2
    while p<=n**(1/4):
        q=next_prime(p)
        while q<=n/(p**3):
#            if q*p**3<= n:#  and p != q):
            count2+=1
            q=next_prime(q)
        p=next_prime(p)
    print(count2)
    
    count1=0           
    p=2
    while p<=n**(1/7):
#        if p**7<n:
        count1+=1
        p=next_prime(p)
    print(count1)
         
    print(count1+count2+count3)
    print(time.clock()-t)
    


