# -*- coding: utf-8 -*-
"""
PE_0031

Coin Sums

How many different ways can £2 be made using any number of coins
Simple example of dynamic programming

Created on Mon Jun 27 08:53:29 2016

@author: Mike
"""
import time
def p31(value,coins):
       
    ways=[0] * (value+1)
    ways[0]=1
   
    while coins[-1]>value:
        del(coins[-1])

    for i in range(len(coins)):
        for j in range (coins[i],value+1):
            ways[j]+=ways[j-coins[i]]
    
    return ways[-1]

#recursive solution using dicts and a memo
#6-10 times slower than dptable or p31, and reaches recursion limit at n=1000
def dpdic(n,denom,memo={}):    
    
#    denom=[1,2,5,10,20,50,100,200]
    m=len(denom)
    
#    base cases    
#    we have no money, coin change must = 0
    if n==0:
        return 1
#    negative money, no change possible
    if n<0:
        return 0
#    we have money, but no change is available
    if n>=1 and m<=0:
        return 0
        
    #recursive solutions
    try:
        key1=tuple([n]+denom[:-1])
        result1 = memo[key1]
    except KeyError:
        result1 = dpdic(n,denom[:-1],memo)
        memo[key1]=memo.get(key1,0)+result1
    try:
        key2=tuple([n-denom[-1]]+denom)
        result2=memo[key2]
    except KeyError:
        result2=dpdic(n-denom[-1],denom,memo)
        memo[key2]=memo.get(key2,0)+result2
    return result1+result2
    
#dynamic programming solution without recursiom
#is 100 times faster in C++
#code from gotclout in p31 forum
def dptable(n,denom):
    m=len(denom)
    table = [[1 for i in range(m)] for j in range(n+1)]
            
    for i in range(1,n+1):
        for j in range(1,m):
            if i-denom[j]>=0:
                table[i][j] = table[i][j-1]+table[i-denom[j]][j]
            else:
                table[i][j] = table[i][j-1]
                
    return table[n][m-1]   
        
    
def dpcall(n=200,denom=[1,2,5,10,20,50,100,200]):
#    t=time.clock()
#    print(dpdic(n,denom,memo={}))
#    print (time.clock()-t)
    
    t=time.clock()
    print(dptable(n,denom))
    print (time.clock()-t)
    
    t=time.clock()
    print(p31(n,denom))
    print (time.clock()-t)
    
