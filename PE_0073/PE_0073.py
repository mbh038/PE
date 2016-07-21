# -*- coding: utf-8 -*-
"""

PE_0073

Counting fractions in a range

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
fractions for d ≤ 12,000?

Created on Wed Jul 20 12:55:25 2016
@author: mbh
"""

from fractions import Fraction
        
def FareyNext(n,lim,memo={}):
    """returns nth numerator in convergents for e
    2,3,8,11,19,87....
    """
    
    if n==1:
        return Fraction(1,2)
    if n==2:
        a=int(lim/2)-1
        b=lim
        return max([Fraction(x,y) for x in range(a-3,a+3) for y in range (b-3,b+1) if float(x)/y<float(1)/2])
    try:
        return memo[n]
    except:
        a,b=FareyNext(n-2,lim).numerator,FareyNext(n-2,lim).denominator
        c,d=FareyNext(n-1,lim).numerator,FareyNext(n-1,lim).denominator
        k=int((lim+b)/d)
        p=c*k-a
        q=d*k-b
        result=Fraction(p,q).limit_denominator(lim)
        memo[n]=result
        return result

from timeit import default_timer as timer
def main(lim):
    start=timer()
    count=1
    result=Fraction(1,2)
    while result>Fraction(1,3): 
        result=FareyNext(count,lim)
        count+=1

    print count-3
    print 'Elapsedtime: ',timer()-start,'s'
    
# wikipedia        
def farey( n, asc=True ):
    """Python function to print the nth Farey sequence, either ascending or descending."""
    if asc: 
        a, b, c, d = 0, 1,  1 , n     # (*)
    else:
        a, b, c, d = 1, 1, n-1, n     # (*)
    print "%d/%d" % (a,b)
    count=0
    
    while (asc and c <= n) or (not asc and a > 0):
        count+=1
        k = int((n + b)/d)
        result= c, d, k*c - a, k*d - b
#        print "%d/%d" % (a,b)  
        count+=1
    print count
    
from timeit import default_timer as timer
def myfarey(n):
    start=timer()
    a,b=1,2    
    c=int(n/2)-1
    d=n
    cd=max([Fraction(x,y) for x in range(c-3,c+3) for y in range (d-3,d+1) if float(x)/y<float(1)/2])    
    c,d=cd.numerator,cd.denominator
    
    count=0
    while d<3*c:
        k=int((n+b)/d)
        a,b,c,d=c,d,k*c-a,k*d-b
        count+=1
    
    print count
    print 'Elapsedtime: ',timer()-start,'s'
    
from fractions import gcd 
start=timer()
#with Python 3.5 or higher, this is much faster: from math import gcd
print(sum(1 for d in range(12001) for n in range(d//3+1,(d+1)//2) if gcd(n,d)==1))
print 'Elapsedtime: ',timer()-start,'s'