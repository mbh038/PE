# -*- coding: utf-8 -*-
"""
PE_0100

Arranged Probability

If a box contains twenty-one coloured discs, composed of fifteen blue discs and 
six red discs, and two discs were taken at random, it can be seen that the 
probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two 
blue discs at random, is a box containing eighty-five blue discs and thirty-five 
red discs.
By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs 
in total, determine the number of blue discs that the box would contain.

Created on Mon Aug 22 08:50:41 2016
@author: mbh
"""
from timeit import default_timer as timer
#how I eventually solved it: 
def rb(n):
    
    fs=(3,1)
    x=1
    while True:
        s,r=Pellnk(8,x,fs)
        if s%2==1:
            b = r + (s + 1) // 2
            if b+r>n:
                break
        x+=1
    print (b)  
  
def Pellnk(n,k,fs,memo={}):
    """
    returns kth solution to Pell equation x^2-ny^2 =1 for given n
    fs is the fundamental solution, given n.
    """   
    x1,y1=fs#Pellfs(n)
    if k==1:
       return x1,y1
    try:
        return memo[k]
    except KeyError:
        xk,yk=Pellnk(n,k-1,fs,memo)
        x=x1*xk+n*y1*yk
        y=x1*yk+y1*xk
        result=x,y
        memo[k]=result
        return result 


#first explorations
import math as m 
def ap():
    
    """exploratory - to see how the number sequences look"""
    b=2
    r=0.5*(m.sqrt(8*b**2-8*b+1)-2*b+1)

    rb,nb,nr=[],[],[]
    delta=1.e-13
    while True:
        b+=1
        r=0.5*(m.sqrt(8*b**2-8*b+1)-2*b+1) # from Wolfram Alpha
        if abs(int(r)-r)<delta:
            nb.append(b)
            nr.append(r)
            rb.append(r+b)
            try:
                print(b,r,r+b,rb[-1]/rb[-2],nb[-1]/nb[-2],nr[-1]/nr[-2])
            except:
                pass
    return r,b,rb

#first solution that works
def ap2(n):
    
    """wrapper to get the answer""" 
    
    start=timer()
    
    r=1
    b=[3]
    
    i=0
    while b[-1]<n/2:        
        b.append(b[-1]*(5+2*A084068(i)/A079496(i+2)))
        i+=1    
    print (int(b[-1]))

    print ('Elapsed time: ',timer()-start,'s')
    
    
def A079496(n,memo={}):
    """returns first n terms of A079496"""
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        if n%2==0:
            result=2*A079496(n-1,memo)-A079496(n-2,memo)
        else:
            result=4*A079496(n-1,memo)-A079496(n-2,memo)
        memo[n]=result
        return result
    
def A084068(n,memo={}):
    """returns first n terms of A079496"""
    if n<=2:
        return n
    try:
        return memo[n]
    except KeyError:
        if n%2==0:
            result=2*A084068(n-1,memo)-A084068(n-2,memo)            
        else:
            result=4*A084068(n-1,memo)-A084068(n-2,memo)
        memo[n]=result
        return result
    
    