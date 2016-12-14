# -*- coding: utf-8 -*-
"""

PE_0135()

Given the positive integers, x, y, and z, are consecutive terms of an arithmetic 
progression, the least value of the positive integer, n, for which the equation, 
x^2 − y^2 − z^2 = n, has exactly two solutions is n = 27:

34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?

Created on Tue Dec 13 14:16:57 2016
@author: mbh
"""
import time
import math
import numpy as np
import matplotlib.pyplot as plt

def p135(n,limit):
    t=time.clock()
    found=[]
    for i in range(1,limit):
        if ndivisors(i)>=2:
            found.append(i)
#    print (len(found))
    nn=0
    for d in found:
        aset=set()  
        ds=sorted(divisors(d))
        for i in range((len(ds)+1)//2):
            delta=(ds[i]+ds[-i-1])/4
            if delta>int(delta):
                continue
            a1=delta+ds[i]
            a2=delta+ds[-i-1]
            if a1>2*delta and a1<5*delta:
                aset.add((a1,delta))
            aset.add((a2,delta))
            
        if len(aset)==n:
            nn+=1            

    print (nn,time.clock()-t)

def p135v2(n,limit):
    t=time.clock()
    solutions={}
    maxaz=[]
    minaz=[]
    tfunc=[]
    xmodz=[]
    xz=[]
    cap=.85*int(1.1*(limit**.5)/3)
    x0=1.15*math.log10(.5*limit**.5)
    width=limit/20
    gamma=0.35#math.log10(limit)-4.7
    #limit/20
    acount,solcount=0,0
    
       
    for x in range(1,int(1.25*limit)):
        az=[]
        if x>.32 * limit and x%5<2:
            continue
        if x>.43 * limit and x%5<3:
            continue
        i=0
        
        if x<=limit/4:
            curve=((cap*gamma/(3.14))*(1/(gamma**2+(math.log10(x)-x0)**2)))
#            curve=int(cap*math.exp(-((x-x0)**2)/(width*x**.95)))+1
            amax=min(x//5+2+int(curve),x//2)
        else:
            amax=x//5+2
#            print(amax-x//5-1)
        for a in range(x//5+1,amax):
            if x<limit//4: acount+=1
#            print(x,a)
            

            sol=-(x-5*a)*(x-a)
#            print(x,a,sol,sol<limit)
            if sol>limit:
                continue
            if sol>0:
                i+=1
                az.append(a)
#                xmodz.append(x%5)
                solcount+=1
                solutions[sol]=solutions.get(sol,0)+1
#                print(x,a,x%5,a%5)

                
               
#                print (sol,(x,a),solutions[sol])
#                plt.plot(iz,az)              
#        try:
#            
            maxaz.append((max(az)-x//5-1))
#            minaz.append((min(az)-x//5-1))
            tfunc.append(curve)
            xz.append(math.log10(x))
#        except:
#            pass
#                rataz.append(max(az)/min(az))
#    print(len(solutions))
#    print(solutions)
    plt.plot(xz,maxaz)
#    plt.plot(xz[:2000],xmodz[:2000])
    plt.plot(xz,tfunc)
#    print(maxaz.index(max(maxaz)),max(maxaz))
#    plt.hist(maxaz)
#    plt.plot(xz,minaz)
#    plt.plot(xz,rataz)
#    print([(k,v) for k,v in solutions.items()])
#    print([x for x in solutions if solutions[x]==n])
    print(time.clock()-t)
    print(sum([solutions[x]==n for x in solutions]))
#    print(len([(x,a) for x,a in solutions.items() if a==1]))
#    print(solcount)
#    print(list(solutions.keys())[list(solutions.values()).index(n)])
    print(acount,solcount)
    print(time.clock()-t)


           
            

def ndivisors(n):
    """find number of divisors of n from prime factor exponents"""
    
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
        
    divisors=1
    for k,v in factors.items():
        divisors*=(v+1)
        
    return divisors
    
def divisors(n):
    """returns the divisors of n"""
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
    
    divs=[]
    nfactors = len(ps)
    f = [0] * nfactors
    while True:
        p=1
        pfs=[x**y for (x,y) in zip(ps,f)]
        for i in range(len(ps)):
            p*=pfs[i]
        divs.append(p)
#could use this from np, but is several times slower for large numbers
#        yield ft.reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= es[i]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return divs 
                
def pfdic(n):
    """returns the distinct prime factors of n as {prime1:exponent1,...}"""   
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