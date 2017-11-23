#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0586

Binary Quadratic Form

f(10^11,40)=258 / 258  0
f(10^12,40)=12672/ 12672  0
f(10^13,40)=309811 / 309803  8
f(10^14,40)=5520971 / 5520926  70
f(10^15,40)=82490213 / 82489813 400

Created on Sun Oct 22 08:56:29 2017
@author: mbh
"""

import time
import numpy as np

def p586(limit):
    t=time.clock()
    
    limit=int(limit)
       
#    f(10**15,40)
    c139=candidates3(limit,1,3,9)
    print('c139',len(c139),time.clock()-t)
    c147=candidates3(limit,1,4,7)
    print('c147',len(c147),time.clock()-t)
    c1119=candidates1119(limit)
    print('c1119',len(c1119),time.clock()-t)
    c1134=candidates1134(limit)
    print('c1134',len(c1134),time.clock()-t)
    c11114=candidates11114(limit)
    print('c11114',len(c11114),time.clock()-t)
    c2222=candidates2222(limit)
    print('c2222',len(c2222),time.clock()-t)
    c228=candidates3(limit,2,2,8)
    print('c228',len(c228),time.clock()-t)
    ps=sorted(c139+c147+c1119+c1134+c11114+c2222+c228)
    print(len(ps))
    print(len(c139)+len(c147)+len(c1119)+len(c1134)+len(c11114)+len(c2222)+len(c228))
    
#    f(10**5,4)
#    ps=candidates2(limit,1,3)+candidates3(limit,1,1,1)+candidates2(limit,2,2)


    #f(10**8,6)
#    ps=candidates2(limit,1,5)+candidates2(limit,2,3)+list(candidates3(limit,1,1,2))
    
#    print(time.clock()-t)

#    ns=[]
#    
#    lLog=np.log(limit)
#    log3root=np.log(3**0.5)        
#    mults=(lLog-np.log(psa))//log3root       
#    print('mults:',len(mults),sum(mults))    
#    print(time.clock()-t)
#    
#    return mults
    
    ns=[]
    
    fives=[5**k for k in range(int(np.log(limit/min(ps))/np.log(5))+1)] 
    
    for p in ps:
        for p5 in fives:
            if p5*p>limit:
                break
            ns.append(p*p5)
            
#    for p in ps:
#        while p<=10000*limit:           
#           ns.append(p)
#           p*=5
    print(limit/10**13)
    print('ns:',time.clock()-t)
    
    print(len(ns),min(ns))
    
    ns=sorted(ns)
#    return ns

#    fives=[5**k for k in range(1,int(np.log(limit/min(ns))/np.log(5))+1)]    
    qg=[int(p) for p in notPrimeMod5Is1or4Factor(int((limit/min(ns))**0.5+1))]    
#    qg=sorted(fives+qgood)
    print(time.clock()-t)
    
    print('qg length:',len(qg))
    
    nfinal=[]
#    count=0
#    lLog=np.log(limit)
#    qLogs=[np.log(q) for q in qgood]
#    
#    print(time.clock()-t)
#    
#    for n in ns:
#        for ql in qLogs:
#            k=(lLog-np.log(3**0.5*n))//ql
#            total=(k+1)*sumFrac(min(m,k+1))

    for n in ns:
        for q in qg:
            nq=n*q
            if nq>limit:
                break
            nfinal.append(nq)
    
    print ('nfinal',len(nfinal))
    print(time.clock()-t)
    
    return nfinal

#case p1^1.p2^3 where p are primes=1 or 4 mod 5.
def candidates13(limit):

    p1lim=int((limit/11**3))
    p2lim=int((limit/11)**(1/3))
    pfs=primeSieve(max(p1lim,p2lim))
    pfs=pfs[np.logical_or((pfs%5==1),(pfs%5==4))]

    p1s=[int(p) for p in pfs[pfs<=p1lim]]
    p2s=[int(p) for p in pfs[pfs<=p2lim]]   
    ps=set()
    for p1 in p1s:
        for p2 in p2s:
            if p2==p1:
                continue
            pprod=p1*p2**3
            if pprod<=limit:
                ps.add(pprod)
    return list(ps)


def candidates1119(limit):

    qs=set()
    limit=limit//11**9
    plim=int(limit/(19*29)+1)
#    pfs=primeSieve(plim)
    ps=[int(p) for p in primeSieve(plim) if p>11 and int(p)%5==1 or int(p)%5==4]
    elevenp9=11**9
    for p1 in ps:
        p2lim=limit//(19*p1)
        for p2 in ps:
            if p2<=p1:
                continue
            if p2>p2lim:
                break
            p3lim=limit//(p1*p2)
            for p3 in ps:
                if p3<=p2:
                    continue
                if p3>p3lim:
                    break
                pprod=p1*p2*p3
                if pprod<=limit:
                    qs.add(pprod*elevenp9)
    return list(qs)

def candidates2222(limit):
    t=time.clock()
    qs=set()
    plim=int((limit//(11**2*19**2*29**2))**0.5+1)
    ps=[int(p) for p in primeSieve(plim) if int(p)%5==1 or int(p)%5==4]
    for p1 in ps:
        p2lim=(limit/(11**2*19**2*p1**2))**0.5
        for p2 in ps:
            if p2<=p1:
                continue
            if p2>p2lim:
                break
            p3lim=(limit/(11**2*p2**2*p1**2))**0.5
            for p3 in ps:
                if p3<=p2:
                    continue
                if p3>p3lim:
                    break
                p4lim=(limit/(p3**2*p2**2*p1**2))**0.5
                for p4 in ps:
                    if p4<=p3:
                        continue
                    if p4>p4lim:
                        break 
#                    print(p1,p2,p3,p4)
#                    pprod=(p1*p2*p3*p4)**2
                    pprod=(p1**2*p2**2*p3**2*p4**2)
                    if pprod<=limit:
                        qs.add(pprod)
    print(time.clock()-t)
    return list(qs)

#case p1.p2.p3, p are prime=1 mod 3    
def candidates111(limit):

    qs=set()
    plim=int(limit/(11*19))
    pfs=primeSieve(plim)
    pfs=pfs[np.logical_or((pfs%5==1),(pfs%5==4))]
    ps=[int(p) for p in pfs[pfs<=plim]]
    for p1 in ps:
        p2lim=limit/(11*p1)
        for p2 in ps:
            if p2==p1:
                continue
            if p2>p2lim:
                break
            p3lim=limit/(p1*p2)
            for p3 in ps:
                if p3==p2 or p3==p1:
                    continue
                if p3>p3lim:
                    break
                pprod=p1*p2*p3
                if pprod<=limit:
                    qs.add(pprod)
    return list(qs)    

#case p1^exp1 . p2^exp2, ps are prime=1 or 4 mod 5    
def candidates2(limit,exp1,exp2):

    qs=set()
    p1lim=int((limit/11**exp2)**(1/exp1))
    p2lim=int((limit/11**exp1)**(1/exp2))
    pf1s=primeSieve(p1lim)
    pf1s=pf1s[np.logical_or((pf1s%5==1),(pf1s%5==4))]
    pf2s=primeSieve(p2lim)
    pf2s=pf2s[np.logical_or((pf2s%5==1),(pf2s%5==4))]
    p1s=[int(p) for p in pf1s[pf1s<=p1lim]]
    p2s=[int(p) for p in pf2s[pf2s<=p2lim]]
    for p1 in p1s:
        for p2 in p2s:
            if p2==p1:
                continue
            pprod=p1**exp1*p2**exp2
            if pprod<=limit:
                qs.add(pprod)
    return list(qs)

def candidates3(limit,exp1,exp2,exp3):

    qs=set()

    p1lim=int((limit/(11**exp3*19**exp2))**(1/exp1)+1)
    p2lim=int((limit/(11**exp3*19**exp1))**(1/exp2)+1)
    p3lim=int((limit/(11**exp2*19**exp1))**(1/exp3)+1)

    p1s=[int(p) for p in primeSieve(p1lim) if int(p)%5==1 or int(p)%5==4]
    p2s=[int(p) for p in primeSieve(p2lim) if int(p)%5==1 or int(p)%5==4]
    p3s=[int(p) for p in primeSieve(p3lim) if int(p)%5==1 or int(p)%5==4]

    for p1 in p1s:
        p2lim=(limit/(11**exp3*p1**exp1))**(1/exp2)
        for p2 in p2s:
            if p2>p2lim:
                break
            if p2==p1:
                continue
            p3lim=(limit/(p1**exp1*p2**exp2))**(1/exp3)
            for p3 in p3s:
                if p3>p3lim:
                    break
                if p3==p2 or p3==p1:
                    continue
                pprod=p1**exp1*p2**exp2*p3**exp3
                if pprod<=limit:
                    qs.add(pprod)
    return list(qs)

def candidates228(limit):
    qs=set()
    p22lim=int((limit/(11**8*19**2))**0.5+1)
    p8lim=int((limit/(11**2*19**2))**0.125+1)
    p22s=[int(p) for p in primeSieve(p22lim) if int(p)%5==1 or int(p)%5==4]
    p8s=[int(p) for p in primeSieve(p8lim) if int(p)%5==1 or int(p)%5==4]
    
    for p1 in p22s:
        p2lim=(limit/(p1**2*11**8))**0.5
        for p2 in p22s:
            if p2>p2lim:
                break
            if p2<=p1:
                continue
            p8lim=(limit/(p1**2*p2**2))**0.125
            for p8 in p8s:
                if p8>p8lim:
                    break
                if p8==p1 or p8==p2:
                    continue
                pprod=p1**2*p2**2*p8**8
                if pprod<=limit:
                    qs.add(pprod)
    return list(qs)

def candidates139(limit):
    qs=set()
    p1lim=int(limit/(11**9*19**3)+1)
    p3lim=int((limit/(11**9*19))**(1/3)+1)
    p9lim=int((limit/(11**3*19))**(1/9)+1)
    p1s=[int(p) for p in primeSieve(p1lim) if int(p)%5==1 or int(p)%5==4]
    p3s=[int(p) for p in primeSieve(p3lim) if int(p)%5==1 or int(p)%5==4]
    p9s=[int(p) for p in primeSieve(p9lim) if int(p)%5==1 or int(p)%5==4]
    
    for p1 in p1s:
        p3lim=(limit/(p1*11**9))**(1/3)
        for p3 in p3s:
            if p3>p3lim:
                break
            if p3==p1:
                continue
            p9lim=(limit/(p1*p3**3))**(1/9)
            for p9 in p9s:
                if p9>p9lim:
                    break
                if p9==p1 or p9==p3:
                    continue
                pprod=p1*p3**3*p9**9
                if pprod<=limit:
                    qs.add(pprod)
    return list(qs)

def candidates1134(limit):
    
    qs=set()
    
    p12lim=int(limit/(11**4*19**3*29)+1)
    p3lim=int((limit/(11**4*19*29))**(1/3)+1)
    p4lim=int((limit/(11**3*19*29))**(1/4)+1)
#    print(p12lim,p3lim,p4lim)
    p12s=[int(p) for p in primeSieve(p12lim) if int(p)%5==1 or int(p)%5==4]
    p3s=[int(p) for p in primeSieve(p3lim) if int(p)%5==1 or int(p)%5==4]
    p4s=[int(p) for p in primeSieve(p4lim) if int(p)%5==1 or int(p)%5==4]

    for p1 in p12s:
        p2lim=limit/(11**4*19**3*p1)
        for p2 in p12s:
            if p2>p2lim:
                break
            if p2<=p1:
                continue
            p3lim=(limit/(11**4*p1*p2))**(1/3)
            for p3 in p3s:
                if p3>p3lim:
                    break
                if p3==p2 or p3==p1:
                    continue
                p4lim=(limit/(p1*p2*p3**3))**(1/4)
                for p4 in p4s:
                    if p4>p4lim:
                        break
                    if p4==p3 or p4==p2 or p4==p1:
                        continue
                    pprod=p1*p2*p3**3*p4**4
                    if pprod<=limit:
                        qs.add(pprod)
    return list(qs)

def candidates11114(limit):
    t=time.clock()
    qs=set()
    p1lim=int((limit/(11*19*29*31))**(1/4)+1)
    p2345lim=int(limit/(11**4*19*29*31)+1)    
    p1s=[int(p) for p in primeSieve(p1lim) if int(p)%5==1 or int(p)%5==4]
    p2345s=[int(p) for p in primeSieve(p2345lim) if int(p)%5==1 or int(p)%5==4]

    p1set=set()
    for p1 in p1s:
        p1p4=p1**4
        p2lim=limit/(p1p4*11*19*29)
        for p2 in p2345s:
            if p2>p2lim:
                break
            if p2==p1:
                continue
            p3lim=limit/(p1p4*p2*11*19)
            for p3 in p2345s:
                if p3>p3lim:
                    break
                if p3<=p2 or p3==p1:
                    continue
                p4lim=limit/(p1p4*p2*p3*11)
                for p4 in p2345s:
                    if p4>p4lim:
                        break
                    if p4<=p3 or p4==p1:
                        continue
                    p5lim=limit/(p1p4*p2*p3*p4)
                    for p5 in p2345s:
                        if p5>p5lim:
                            break
                        if p5<=p4 or p5==p1:
                            continue
                        
                        pprod=p1p4*p2*p3*p4*p5
                        if pprod<=limit:
                            qs.add(pprod)
                            p1set.add(p1)
    print(p1set)
    print(time.clock()-t)
    print(len(qs))
    return list(qs)


def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

def notPrimeMod5Is1or4Factor(n):
    """return array of numbers not divisible by 5 or primes p = 1 or 4 mod 5"""
    sieve=np.ones(n+1,dtype=bool)
    ps=primeSieve(n)
    ps=ps[np.logical_or((ps%5==1),(ps%5==4))]
    for i in ps:
        if sieve[i]:
            sieve[i::i]=False
    ps= np.nonzero(sieve)[0]
    ps=ps[ps%5!=0]
    ps=ps**2
#    ps=ps[2:]    
    return ps.astype(int)

def prime_factors(n):
    """returns the prime factors of n"""   
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

def oeis():
    ns=	[1, 4, 5, 9, 11, 16, 19, 20, 25, 29, 31, 36, 41, 44, 45, 49, 55, 59, 61, 64, 71, 76, 79, 80, 81, 89, 95, 99, 100, 101, 109, 116, 121, 124, 125, 131, 139, 144, 145, 149, 151, 155, 164, 169, 171, 176, 179, 180, 181, 191, 196, 199, 205, 209, 211, 220, 225, 229, 236]
    sols=[]
    for n in ns:
        sol=1
        pfs=pfdic(n)
        for pf,exp in pfs.items():
            if pf%5==1 or pf%5==4:
                sol*=(exp+1)
        sols.append(sol//2)
    return sols
        
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