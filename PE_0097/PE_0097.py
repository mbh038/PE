# -*- coding: utf-8 -*-
"""
PE_0097()

Large non-Mersenne prime

The first known prime found to exceed one million digits was discovered in 1999, 
and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. 
Subsequently other Mersenne primes, of the form 2p−1, have been found which contain 
more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 
2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime number.

Created on Fri Sep  2 04:04:39 2016
@author: mbh
"""

from timeit import default_timer as timer
 
# takes 40 ms
def PE_0097(a=28433,b=7830457,M=10):
    """returns a*2^b + 1 mod M"""
    start=timer()
    M=10**M
    x=1
    binb=[int(x) for x in bin(b)[2:][::-1]]
    binb=[2**i for i in range(len(binb)) if binb[i]==1]
    for i in binb:
        x=(x*2**i)%M
    print((a*x+1)%M)
    print('Elapsed time:',timer()-start)

#faster....    
def faster(a=28433,b=7830457,M=10):
    start=timer()
    print ((a*int('1'+'0'*b,2)+1) % 10**M)
    print('Elapsed time',timer()-start)
    
#or just try....
#print((28433*2**7830457+1)%10**10)
    
def test(b):
    x=2
    p=0
    while x<b:
        p+=1
        x=x**2
        print(p,x)
#    print(x**0.5,p)