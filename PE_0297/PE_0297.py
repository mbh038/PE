# -*- coding: utf-8 -*-
"""

PE_0297

Created on Mon Feb 20 06:19:42 2017
@author: mbh
"""

import time

def p297(n):
    
    t=time.clock()
    
    fs=[0]+[dijkFib(k) for k in range(1,1000)]
    fSums=[0]+[fSum(k) for k in range(1,1000)]
    
    print(zSum(n,fs,fSums))
    print(time.clock()-t)
    
def zSum(n,fs,fSums):
       
    base=[0,0,1,2,3,5,6,8,10,11]
    
    if n<10:
        return base[n]
    k=bisect(n,fs)
    return fSums[k]+(n-fs[k])+zSum(n-fs[k],fs,fSums)

#returns sum of 1s for all 0<n<F(k) where F(k) is the kth Fibonacci number
def fSum(k,memo={}):
    if k<3:
        return 0
    if k==3:
        return 1
    if k==4:
        return 2
    try:
        return memo[k]        
    except KeyError:
        result=2*fSum(k-1,memo)-fSum(k-3,memo)+dijkFib(k-4)
        memo[k]=result
        return result
    
# returns index of largest element of sortedList that is less than or equal to target.
def bisect(target,sortedList):
    
    if target in sortedList:
        return sortedList.index(target)
    
    low,high=0,len(sortedList)-1
    ans=(high+low)//2
    
    while high-low>1:
        if target>sortedList[ans]:
            low=ans
        else:
            high=ans
        ans=(high+low)//2
    
    return ans

def dijkFib(n,memo={}):
    """returns nth Fibonacci term"""
    if n==0 or n==1:
        return n
    try:
        return memo[n]
    except KeyError:
        if n%2:
            result=dijkFib((n-1)//2,memo)**2+dijkFib((n+1)//2,memo)**2
        if not n%2:
            result=(2*dijkFib((n-1)//2,memo)+dijkFib((n+1)//2,memo))*dijkFib((n+1)//2)
        memo[n]=result
        return result

# Not used below here
#################################################            

#returns list of Fibonaacci terms in Zeckendorf representation of n
def Z(n):
    Fs=[]
    ks=[]
    m=0
    while dijkFib(m)<=n:
        m+=1
    m-=1
    Fs.append(dijkFib(m))
    ks.append(m)
    mlast=m
    while m>0:
        m-=1
        Fm=dijkFib(m)
        if sum(Fs)+Fm<=n and mlast-m>1:
            Fs.append(Fm)
            ks.append(m)
            mlast=m
        else:
            Fs.append(0)
#        if sum(Fs)==n:
#            break
#    return(Fs[::-1])
    if len(ks)>1:
        ks=ks[:-1]
    return(ks)

#returns number of 1s in Zeckendorf representation of n
def z(n):
    Fs=Z(n)
    return len(Fs)
    
#returns sum of 1s for F(k-1)<=n<F(k) where F(k) is the kth Fibonacci number
def fSum2(k,memo={}):
    if k==0:
        return 1;
    if k==1 or k==2:
        return 1
    if k==3:
        return 1
    try:
        return memo[k]
    except KeyError:
        result=fSum(k-1,memo)+fSum(k-2,memo)+dijkFib(k-3)
        memo[k]=result
        return result



        
#returns sum of 1s in z(n) for 0<n<=F(k) where F(k) is the kth Fibonacci term
def zSum2(k):
    return sum([fSum(n) for n in range(2,k+1)])       
        
        

def dijkFib(n,memo={}):
    """returns nth Fibonacci term"""
    if n==0 or n==1:
        return n
    try:
        return memo[n]
    except KeyError:
        if n%2:
            result=dijkFib((n-1)//2,memo)**2+dijkFib((n+1)//2,memo)**2
        if not n%2:
            result=(2*dijkFib((n-1)//2,memo)+dijkFib((n+1)//2,memo))*dijkFib((n+1)//2)
        memo[n]=result
        return result

