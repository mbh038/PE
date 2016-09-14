# -*- coding: utf-8 -*-
"""

PE_0157

Created on Tue Sep 13 15:10:14 2016
@author: mbh
"""
import math
from timeit import default_timer as timer
def p157(nmax):
    start=timer()
    solutions=set()
    sols=0

    for n in range(1,nmax+1):
        tp=10**n
        k=0
        sols=0
        ps=set()
        ks=set()
        xs=set()
        ys=set()
        while k<10**n:
#            solutions=set()            
            k+=1
#            if int(10**n/k)!=10**n/k:
#                continue

            if int((tp/k)*(k+tp))!=(tp/k)*(k+tp):
                continue
#            print('k',k)
#            print(ynum)

#            p2=findDivisors(10)
#            p=pfdic(ynum)
            
#            sols+=listprod([(v+1) for k,v in p.items()])
    
#            if len(p)==0:
#                break
#            print('p',p)
#            print('k',k)
            p=k+10**n
#            print ('k,p',k,p)
#            if 10**n%k==0:
#                sols+=len(p)
#            continue
#            d=findDivisors(10**n/k)
#            print('d',d)
            
#            pdr=[pval for pval in findDivisors((tp/k)*(k+tp)) if (k+tp)%pval==0]
            pdr=[pval for pval in prime_factors((tp/k)*(k+tp))]
#            print('pd',pd)
#            pdr=[pval for pval in pd if (k+tp)%pval==0]
#            print('pdr',pdr)
#            print()
            sols+=len(pdr)
#            continue
#            y=[((10**n/k)*(k+10**n))/pval for pval in p]
#            print('y',y)
#            x=[(k+10**n)/pval for pval in p]
#            print('x',x)              
#            for i in range(len(y)):
#                solutions.add((tuple(sorted([x[i],y[i]])),p[i],k))
#                ps.add(p[i])
#                ks.add(k)
#                xs.add(x[i])
#                ys.add(y[i])
                
#            print (solutions)
#            valids=[10**n*(x[i]+y[i])==x[i]*y[i]*p[i] for i in range(len(x))]
#            print('valids',valids)
#            print('integer values of x',sum([int(xval)==xval for xval in x]))
#            print('Non-integer values of x',sum([int(xval)!=xval for xval in x]))
        print(n,sols)
#        print (solutions)
#        (pmin,pmax)=(min([v[1] for v in solutions]),max([v[1] for v in solutions]))
#        print ('pmin,pmax',pmin,pmax)
#        (kmin,kmax)=(min([v[2] for v in solutions]),max([v[2] for v in solutions]))
#        print ('kmin,kmax',kmin,kmax)
#        (xmin,xmax)=(min([v[0][0] for v in solutions]),max([v[0][0] for v in solutions]))
#        print ('xmin,xmax',xmin,xmax)
#        (ymin,ymax)=(min([v[0][1] for v in solutions]),max([v[0][1] for v in solutions]))
#        print ('ymin,ymax',ymin,ymax)
#        print ('ps,ks,xs,ys',len(ps),len(ks),len(xs),len(ys))        
        print('Elapsed time:',timer()-start)

            
#    return solutions
       
#        for k in range(1,2*100**n):
#            for p in range(1,200*(k+10**n)//k):
#                ab=[]
#                bnum=10**n*(k+10**n)
#                bden=k*p
#                if bden in findDivisors(bnum):
#                    ab.append(bnum/bden)
#                    ab.append((k+10**n)/p)
#                    ab=sorted(ab)
#                    a=ab[0]
#                    b=ab[1]
#                    if a==6:
#                        print (a,b,p)
#                    if a>0 and b>0:
#                        if int(a)==a and int(b)==b and ((a+b)/(a*b))==p/(10**n):
#                            i+=1
#                            solutions.add((a,b,p))
#    #                    print (i,'a,b,p,k',a,b,p,k)               
#        print(solutions)
#        print(len(solutions))

def pfdic(n):
    '''
    returns the distinct prime factors of n as a dictionary
    k:v = prime factor:exponent
    '''   
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i]=factors.get(i,0)+1
    if n > 1:
        factors[n]=factors.get(n,0)+1
    return factors
                
def prime_factors(n):
    '''
    returns the prime factors of n
    '''   
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def findDivisors(n,proper=False):
    """
    returns a list of the divisors of n (numbers less than or equal to n which 
    divide evenly into n)
    n is a positive integer
    If proper is set True, only the proper divisors are returned - all divisors 
    of n that are less than n
    """
    factors=[]
    for i in range(1,int(math.floor(math.sqrt(n)))+1):
        if n % i == 0:
            factors.append(i)
            if n//i != i:
                factors.append(n//i)
    if proper: factors.remove(n)
    return factors
#    return sorted(factors)[:-1] - use this if sorted list required
    
def listprod(numbers):
    p=1
    for i in range(len(numbers)):
        p*=numbers[i]
    return p 