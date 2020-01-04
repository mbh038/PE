#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0686

Powers of Two

Created on Sun Dec 22 08:28:11 2019

@author: mbh
"""

# find a few

import numpy as np
import time
        
def digit_reverse(number):
    reverse=0
    while number>0:
        lastdigit=number%10
        reverse = 10*reverse+lastdigit
        number =number//10
    print (reverse)
    
def p686(L=123,n=678910):
    # first digit is L
    # want the nth candidate
    t0=time.perf_counter()
    dL=int(np.log10(L))
    
    lower=np.log10(L)-dL
    upper= np.log10(L+1)-dL
    
    dL=int(np.log10(L))
    counts=np.zeros(n+1,dtype=int)
    counts[0]=7
    count=1
    logsums=np.array([90,90,90]) # the first power is 90
    found=1
#    print(found,logsums[1],(logsums[1]*np.log10(2)-dL) % 1)
    while found<n:
        logsums+=np.array([196, 289, 485]) # subsequent powers increment by one of these values
#        print(found,count,(logsum-dL) % 1)
        count+=1
        
        for logsum in logsums:
            if (logsum*np.log10(2)-dL) % 1 >= lower and (logsum*np.log10(2)-dL) % 1 <upper:
                found+=1
                logsums=np.array([logsum,logsum,logsum])
#                print(found,logsum,(logsum*np.log10(2)-dL) % 1)
                
                break
    print (logsum)
    print(time.perf_counter()-t0)

        

def leading_digits(n,k):
    # find leading k digits  in 2^n:
    print(n*np.log10(2)-int(n*np.log10(2))+k-1)


    return int(pow(10,n*np.log10(2)-int(n*np.log10(2))+k-1))

## For L=123, first one is 2^90, the differences are one of 289,196,465
