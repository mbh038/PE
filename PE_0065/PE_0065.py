# -*- coding: utf-8 -*-
"""

PE_0065 (See also P_0057)

Convergents of e

e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.

Generally for continued fractions:
In words, the numerator of the third convergent is formed by multiplying the
numerator of the second convergent by the third quotient, and adding the
numerator of the first convergent.

n: hn = anhn − 1 + hn−2,
d: kn = ankn − 1 + kn−2.

Created on Sat Jul 16 21:02:43 2016
@author: mbh
"""
from timeit import default_timer as timer

def an_e(n):
    """returns nth term in continued fraction for e
    e=[2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...]
    """
    if n==1:
        return 2
    if n%3==0:
        return n*2/3
    else:
        return 1
        
def ecfn(n,memo={}):
    """returns nth numerator in convergents for e
    2,3,8,11,19,87....
    """
    
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
    
from math import log10
def digitsum(x):
    num=int(log10(x))
    digsum=0
    for n in range(num,-1,-1):
        digsum+=x /10**n
        x=x%10**n
    return digsum

