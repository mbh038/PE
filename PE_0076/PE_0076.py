# -*- coding: utf-8 -*-
"""

PE_0076

Counting summations

How many different ways can one hundred be written as a sum of at least two
positive integers?

This is the partition function p(n)

https://en.wikipedia.org/wiki/Partition_(number_theory)

We need pentagonal numbers and generalised pentagonal numbers.

For 

n= 0,1,2,3,4,5,6

pent(n)=(3n^2-n)/2

.. = 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287, 330, 376, 425,
 477, 532, 590, 651, 715, 782, 852, 925, 1001
 
but for 

n= 0,1,-1,2,-2,3,-3...

we have the generalised pentagonal numbers:

gpent(n)= 0, 1, 2, 5, 7, 12, 15, 22, 26, 35, 40, 51, 57, 70, 77, 92, 100, 117, 126,
 145, 155, 176, 187, 210, 222, 247, 260, 287, 301, 330, 345,
 
The partition function p(k):

p(k)= p(k − 1) + p(k − 2) − p(k − 5) − p(k − 7) + p(k − 12) + p(k − 15)
 − p(k − 22) − ...

where the decrements in each temr are the generalised pentagonal numbers,
gpent(m), and the sign is (-1)^(|m|-1)

Created on Fri Jul 22 17:03:44 2016


@author: mbh
"""

from timeit import default_timer as timer
from math import sqrt

#code adapted from P31, coin sum problem. 1 ms!
def p1(value):
    start=timer()
    ps=list(range(1,value+1))   
    ways=[0] * (value+1)
    ways[0]=1   
    while ps[-1]>value:
        del(ps[-1])
    for i in range(len(ps)):
        for j in range (ps[i],value+1):
            ways[j]+=ways[j-ps[i]]    
    return (ways[-1]-1)+1
    print('Elapsed time: ',timer()-start,'s')


#try recursion solution from 
#https://en.wikipedia.org/wiki/Partition_(number_theory)#Partition_function_formulas
import sys
sys.setrecursionlimit(1000000)
def p2(n,memo={}):
    if n<0:
        return 0
    if n==0:
        return 1
    try:
        return memo[n]
    except:       
        result=sum([(-1)**(k-1)*(p2(n-k*(3*k-1)//2,memo)+p2(n-k*(3*k+1)//2,memo) ) for k in range(1,int(sqrt(n))+1)])
        memo[n]=result
        return result
        
#n=100
#print(p2(n)-1)

#try without memoization: massively slower
def p3(n):
    if n<0:
        return 0
    if n==0:
        return 1      
    result=sum([(-1)**(k-1)*(p3(n-k*(3*k-1)//2)+p3(n-k*(3*k+1)//2) ) for k in range(1,n+1)])
    return result

       
def partition(n):
#    start=timer()
#    print (p1(n)-1)
#    print ('Elapsed time: ',timer()-start,'s')
    start=timer()
    print (p2(n)-1)
    print ('Elapsed time: ',timer()-start,'s')