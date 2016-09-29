# -*- coding: utf-8 -*-
"""

PE_0073

Counting fractions in a range

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
fractions for d ≤ 12,000?

Created on Wed Jul 20 12:55:25 2016
@author: mbh
"""
from timeit import default_timer as timer
from fractions import Fraction #very slow
        
# very slow -O(N2) and uses fractions
def FareyNext(n,lim,memo={}):
    """returns nth numerator in convergents for e
    2,3,8,11,19,87....
    """
    
    if n==1:
        return Fraction(1,2)
    if n==2:
        a=int(lim/2)-1
        b=lim
        return max([Fraction(x,y) for x in range(a-3,a+3) for y in range (b-3,b+1) if x/y<1/2])
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


def main(lim):
    start=timer()
    count=1
    result=Fraction(1,2)
    while result>Fraction(1,3): 
        result=FareyNext(count,lim)
        count+=1

    print (count-3)
    print ('Elapsedtime: ',timer()-start,'s')
    
# wikipedia        
def farey( n, asc=True ):
    """Python function to print the nth Farey sequence, either ascending or descending."""
    if asc: 
        a, b, c, d = 0, 1,  1 , n     # (*)
    else:
        a, b, c, d = 1, 1, n-1, n     # (*)
    print ("%d/%d" % (a,b))
    count=0
    
    while (asc and c <= n) or (not asc and a > 0):
        count+=1
        k = int((n + b)/d)
        result= c, d, k*c - a, k*d - b
#        print "%d/%d" % (a,b)  
        count+=1
    print (count)
    

#about 4s, O(N2) - counts along the Farey sequence
def myfarey(n):
    a,b=1,3 
    c0,d0=1,2
    c=c0+a*(n-d0)/b
    d=d0+b*(n-d0)/b
    count=0
    while d>=2*c:
        k=int((n+b)/d)
        a,b,c,d=c,d,k*c-a,k*d-b
        count+=1   
    print (count)

    

    
#just as fast in Python 3.5...
from math import gcd
def farey3():
    start=timer()
    #with Python 3.5 or higher, this is much faster: from math import gcd
    print(sum(1 for d in range(12001) for n in range(d//3+1,(d+1)//2) if gcd(n,d)==1))
    print ('Elapsedtime: ',timer()-start,'s')
    

#dfs tree method, also O(N2)
from sys import setrecursionlimit
setrecursionlimit(10**4)
def SternBrocot(limit,leftN,leftD,rightN,rightD):
    medN = leftN + rightN
    medD = leftD + rightD
    if medD > limit:
        return 0
    else:
        count = 1
        count = count + SternBrocot(limit,leftN,leftD,medN,medD)
        count = count + SternBrocot(limit,medN,medD,rightN,rightD)
        return count
        
def mainSB(limit,leftN,leftD,rightN,rightD):
    start=timer()
    count=SternBrocot(limit,leftN,leftD,rightN,rightD)
    print(count)
    print ('Elapsedtime: ',timer()-start,'s')
    

#about 2.5s - as fast as it gets for counting algorithms. But is still O(N2)
def fastcount(limit):
    start=timer()
    count = 0
    top = 0
    stack = [x for x in range(0,int(limit/2)+1)]
    left = 3
    right = 2
    while True:
        med = left + right
        if med > limit:
            if top > 0:
                left = right
                top = top - 1
                right = stack[top]
            else:
                break
        else:
            count += 1
            stack[top] = right
            top = top + 1
            right = med
    print ('Elapsedtime: ',timer()-start,'s')


    print(count)

#c=vry fast sub linear method, explained in P73 overview
from timeit import default_timer as timer
from math import sqrt

def F(n):
    q = n // 6
    r = n % 6
    f = q*(3*q - 2 + r)
    if r == 5:
        f +=1
    return f
    

def R(n,N,K,M,rsmall,rlarge): 
    switch =   sqrt(n/2)
    count = F(n)
    count = count - F(n // 2)
    m = 5
    k = (n - 5) // 10
    while k>=switch:
        nextk = (n // (m + 1) - 1) // 2
        count -= (k - nextk)*rsmall[m]
        k = nextk
        m +=1

    while k > 0:
        m = n // (2*k+1)
        if m<=M:
            count -= rsmall[m]
        else:
            count -= rlarge[((N // m) - 1) // 2]   
        k = k - 1
    if n<=M:
        rsmall[n] = count
    else:
        rlarge[((N // n) - 1) // 2] = count
        
def mainfast(N):
    start=timer()
    K =int(sqrt(N/2))
    M =int(N/(2*K+1))

    rsmall = list(range (0,M+1))
    rlarge = list(range (0,K))
    
    for n in range(5,M+1):
        R(n,N,K,M,rsmall,rlarge)

    for j in range(K-1,-1,-1):
        R(N // (2*j + 1),N,K,M,rsmall,rlarge)

    count = rlarge[0]
    print (count)
    print('Elapsed time: ',timer()-start)