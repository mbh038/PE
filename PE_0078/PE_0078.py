# -*- coding: utf-8 -*-
"""
PE_0078

Coin partitions

Find the least value of n for which p(n) is divisible by one million.

Created on Sat Jul 23 07:01:17 2016
@author: mbh
"""

#begin with 4 and ivisible by 1000: (7964 divisible by 10000)
#using Ramanujan ob.s that most div by 5 end in 4 or 9
d4b1000=[2124,2334,2474,3324,3584,4224,4424,4624,4724,5534,5574,5624,6374,6814,7324,7964,9724]

from timeit import default_timer as timer
from math import sqrt

#originally for p31, adapted for p76
def p1(value):
#    start=timer()
    ps=list(range(1,value+1))   
    ways=[0] * (value+1)
    ways[0]=1   
#    while ps[-1]>value:
#        del(ps[-1])
    for i in range(len(ps)):
        for j in range (ps[i],value+1):
            ways[j]+=ways[j-ps[i]] 
#    print('Elapsed time: ',timer()-start,'s')
    return ways[-1]
    
    

#from P76: partition formula, using memoization    
#import sys,threading
#sys.setrecursionlimit(200000)
#threading.stack_size(10240000)
def p2(n,memo={}):
    if n<0:
        return 0
    if n==0:
        return 1
    try:
        return memo[n]
    except:       
        result=sum([(-1)**(k-1)*(p2(n-k*(3*k-1)//2,memo)+p2(n-k*(3*k+1)//2,memo)) for k in range(1,int(sqrt(n)+1))])
        memo[n]=result
        return result
            
def PE_0078(ll,ul,divisor):
    for n in range(ll+4,ul+4,5):
        a=p2(n)
        if a%divisor==0:
            print (n,a)
            break
            
#Hardy-Ramanujan asymptotic formula
from math import sqrt,exp,pi
def p3as(n):
    return (1/(4*n*sqrt(3)))*exp(pi*sqrt(2*n/3))
    
    def pl():
    for n in range (1,50):
        print (n,p1(n))            


#pe_dilantha Thu, 29 Oct 2015, 09:22 
def ped(n):
    cnt = [0] * (n+1)
    cnt[0] = 1
    for i in range(1, n):
        for j in range(i, n+1):
            cnt[j] += cnt[j - i]
    print (cnt[n])