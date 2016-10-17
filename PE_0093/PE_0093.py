# -*- coding: utf-8 -*-
"""
PE_0093

Arithmetic expressions

Find the set of four distinct digits, a < b < c < d, for which the longest set 
of consecutive positive integers, 1 to n, can be obtained, giving your answer 
as a string: abcd.

Created on Sat Oct  8 07:08:50 2016
@author: mbh
"""
import scipy as sc
def Bell(n,memo={}):
    """how many ways can a set of n things be partitioned"""
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result =sum([sc.misc.comb(n-1,k)*Bell(k,memo) for k in range(n)])
        memo[n]=result
        return result
    
def p93(x='1234+-*/()'):
    vals=set()
    for a in it.permutations(x,len(x)):
        try:
            c=eval(''.join([b for b in a]))
            if int(c)==c:
               vals.add(c)
               print(a,c)
        except:
            pass
    print (sorted(list(vals)))
    print('#',len(vals),'max',max(vals))
    
 
