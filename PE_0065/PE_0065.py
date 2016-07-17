# -*- coding: utf-8 -*-
"""

PE_0065

Convergents of e

In words, the numerator of the third convergent is formed by multiplying the
numerator of the second convergent by the third quotient, and adding the
numerator of the first convergent.

hn = anhn − 1 + hn − 2,
kn = ankn − 1 + kn − 2.

e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

Created on Sat Jul 16 21:02:43 2016
@author: mbh
"""
from timeit import default_timer as timer

def an_e(n):
    """returns nth term in continued fraction for e"""
    if n==1:
        return 2
    if n==2:
        return 1
    if n%3==0:
        return n*2/3
    else:
        return 1
        
def ecfn(n,memo={}):
    """returns nth numerator in convergents for e"""
    
    if n==1:
        return 2
    if n==2:
        return 3
    try:
        return memo[n]
    except:
        result=an_e(n)*ecfn(n-1,memo)+ecfn(n-2)
        memo[n]=result
        return result
    
def main(n):
    """return sum of digits in numerator of nth convergent to e"""
    start=timer()
    print sum(int(x) for x in str(ecfn(n)))
    print 'Elapsed time: ',timer()-start
    



# not required
def cpell(n,memo={}):
    """ Returns nth companion Pell number, n is an integer"""
    if n==0:
        return 2
    if n==1:
        return 2
    try:
        return memo[n]
    except KeyError:
        result=2*cpell(n-1,memo)+cpell(n-2,memo)
        memo[n]=result
        return result
        
def pell(n,memo={}):
    """ Returns nth Pell number, n is an integer"""
    if n==0:
        return 0
    if n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result=2*pell(n-1,memo)+pell(n-2,memo)
        memo[n]=result
        return result
        
def root2(n):
    start=timer()
    count=0
    for i in xrange(1,n+2):
        num=pell(i-1)+pell(i)
        den=pell(i)
        if(len(str(num)))>(len(str(den))): count+=1
    print count
    print 'Elapsed time: ',timer()-start,'s'
    