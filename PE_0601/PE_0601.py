# -*- coding: utf-8 -*-
"""

PE_601

Divisibility streaks

P(i,4**i)=[0,1,5,5,17,0,59,20,52,0,379,0,559,0,0,1490,5609,0,5313,0,0]

[(0, 0),
 (1, 1),
 (2, 5),5
 (3, 5),5
 (4, 17),17
 (5, 0),
 (6, 59),59
 (7, 20),20
 (8, 52),52
 (9, 0),
 (10, 379),379
 (11, 0),
 (12, 559),559
 (13, 0),
 (14, 0),
 (15, 1490),1490
 (16, 5609),5608
 (17, 0),
 (18, 5313),5314
 (19, 0),
 (20, 0)]
 
 [[1,]
 [2,3,2,2],
 [3,7,12,1],
 [4,13,12,4],
 [6,61,60,6],
 [7, 421, 840,1],
 [8, 841, 840,2],
 [10, 2521, 2520,10],
 [12 , 27721,27720,12],
 [15, 360361,720720,1],
 [16,720721,720720,16],
 [18,12252241,12252240,18],
 [22, 232792561, 232792560,22],
 [24,5354228881,5354228880,4],
 [26,26771144401,26771144400,2],
 [28,80313433201,80313433200,28]
 [30,2329089562801,2329089562800,30]]

Created on Mon May  1 07:05:31 2017
@author: mbh
"""

import math
import time

def lcm(a):
    
    lcm=int(a[0]*a[1]/math.gcd(a[0],a[1]))
    for i in range(2,len(a)):
        lcm*=a[i]//math.gcd(lcm,a[i])
    return lcm

def p601(n):
    t=time.clock()
    Psum=1
    for s in range(2,n+1):
        N=4**s
        Psum+=(N-2)//lcm([i for i in range(1,s+1)])-(N-2)//lcm([i for i in range(1,s+2)])        
    print(Psum)
    print(time.clock()-t)
        

def seeker(n):
    count,countnp1=0,0
    ns=[]
    np1s=[]
    for i in range(2,4**n):
        if streak(i)==n:
            count+=1
            ns.append((count,i))
        if streak(i)==n+1:
            countnp1+=1
            np1s.append((countnp1,i))
    print(ns)
    print()
    print(np1s)
            


def p601v1(limit):
    Psum=0
    vals= [[2,3,2,2],
 [3,7,12,1],
 [4,13,12,4],
 [6,61,60,6],
 [7, 421, 840,1],
 [8, 841, 840,2],
 [10, 2521, 2520,10],
 [12 , 27721,27720,12],
 [15, 360361,720720,1],
 [16,720721,720720,16],
 [18,12252241,12252240,18],
 [22, 232792561,232792560,22],
 [24,5354228881,5354228880,4],
 [26,26771144401,26771144400,2],
 [28,80313433201,80313433200,28],
[30,2329089562801,2329089562800,30],
[31,72201776446801,144403552893600,1]]
    for val in vals:
        newVal=P4(val[0],4**val[0],val[1],val[2],val[3])
        print(val,newVal)
        Psum+=newVal
    print(Psum+1)
        
def P4(s,limit,val1,dval,period) :
    nval=1
    valSum=val1
    if period==1:
        while valSum<limit:
            valSum+=dval
            if valSum>=limit:
                break
            nval+=1            
    else:
        while  valSum<limit:
            for i in range(period-1):
                valSum+=dval
                if valSum>=limit:
                    break
                nval+=1
            valSum+=2*dval
            if valSum>limit:
                break
            nval+=1
    return nval
        
def streak(n):
    k=1
    while 1:
#        print(n+k,k+1)
        if(n+k)%(k+1):
            break
        k+=1        
    return(k)

def P(s,limit,verbose=False):
    t=time.clock()
    P=0    
    for n in range(2,limit):
        k=0
        while 1:
            if(n+k)%(k+1):
                break
            k+=1
            if k>s:
                P-=1
                break
            if k==s:
                P+=1
        if k==s: print(P,n,streak(n))
    print(P,time.clock()-t)
    return P
    
def P2(s,limit):
    t=time.clock()
    Psum=0
    k=s
    klast=0
    count=0
    val1=0
    dval=0
    while k<limit:
        k+=s
        j=1
        while j<s:
            if (k-j)%(s-j):
                break
            j+=1
        if j==s:
            if (k+1)%(s+1)>0:
                Psum+=1
                print(k,s,(k+1)%(s+1),k-s+1,k-klast)
                dval=k-klast
                klast=k
                count+=1
                if count==1:
                    val1=k-s+1
    print(Psum,time.clock()-t)
    return s,val1,dval
            