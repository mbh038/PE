# -*- coding: utf-8 -*-
"""

PE_0157

Created on Tue Sep 13 15:10:14 2016
@author: mbh
"""

from timeit import default_timer as timer
def p157(nmax):
    """
    returns number of solutions to 1/x + 1/y = p/10^n for 1<=n<=nmax
    x,y,p,n are positive integers, x<=y
    """
    start=timer()
    solutions=set()
    sols=0    
    for n in range(1,nmax+1):
        d=sorted([2**i*5**j for i in range(2*n+1) for j in range(2*n+1)])
        ks=[k for k in d if k<=10**n]
        for k in ks:
            yp=10**n+(10**(2*n))/k
            xp=k+10**n
            ps=[p for p in divisorGen(xp) if yp%p==0]
            sols+=len(ps)
#            xs=[xp/p for p in ps]
#            ys=[yp/p for p in ps]
#            for i in range(len(xs)):
#                solutions.add((xs[i],ys[i],ps[i]))
#        print(n,len(solutions))
    print(sols)
    print('Elapsed time:',timer()-start,'s')


def divisorGen(n):
    """yields the divisors of n"""    
    #first get the prime factors
    i = 2
    fs = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            fs[i]=fs.get(i,0)+1
    if n > 1:
        fs[n]=fs.get(n,0)+1
        
    ps=[k for k,v in fs.items()] #prime factors
    es=[v for k,v in fs.items()] #exponents 
    
    nfactors = len(ps)
    f = [0] * nfactors
    while True:
        p=1
        pfs=[x**y for (x,y) in zip(ps,f)]
        for i in range(len(ps)):
            p*=pfs[i]
        yield p
#        yield np.cumprod(np.array([x**y for (x,y) in zip(ps,f)]))[-1]
        i = 0
        while True:
            f[i] += 1
            if f[i] <= es[i]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return                                 
                   
