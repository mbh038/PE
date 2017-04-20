# -*- coding: utf-8 -*-
"""

PE_0297

Created on Mon Feb 20 06:19:42 2017
@author: mbh
"""

def p297(n):
    
    fibs=[0]
    m=2
    while 1:
        nextfib=dijkFib(m)
        if nextfib>n:
            break
        fibs.append(nextfib)
#        print(m,fibs[-1],fibs[-1]<n)
        m+=1
        
    fibs=fibs[::-1]
        
    print (fibs)

def Z(n):
    m=1
    while 1:
        if dijkFib(m)>n:
            break
        m+=1
    print( m-1,dijkFib(m-1))
    
        
        
        

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

