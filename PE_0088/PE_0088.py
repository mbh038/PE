# -*- coding: utf-8 -*-
"""

PE_0088

Product-sum numbers

A natural number, N, that can be written as the sum and product of a given set 
of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum 
number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a 
minimal product-sum number. The minimal product-sum numbers for sets of size, 
k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; 
note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is 
{4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
Created on Fri Sep  2 04:06:27 2016
@author: mbh
"""
import numpy as np
import itertools as it
import matplotlib.pyplot as plt
from timeit import default_timer as timer

def pgen(r,xm,memo={}):
    if r==1:
        return [x for x in range(2,xm+1)]
    if xm==2:
        return [2]*r
    try:
        return memo[(r,xm)]    
    except KeyError:
        result=[[x]+[xm] for x in pgen(r-1,xm,memo)]+[pgen(r,xm-1,memo)]
        print(result)
        memo=result
        return result

   
import sys
sys.setrecursionlimit(1000000)
def p2(n,memo={}):
    """how many ways to partition n. From p76"""
    if n<0:
        return 0
    if n==0:
        return 1
    try:
        return memo[n]
    except:       
        result=sum([(-1)**(k-1)*(p2(n-k*(3*k-1)//2,memo)+p2(n-k*(3*k+1)//2,memo) ) for k in range(1,int(np.sqrt(n))+1)])
        memo[n]=result
        return result
        
from itertools import chain, combinations
S={1,2,3,4}
def mpS():
    """find all the subsets of S"""
    return list(chain(*(list(combinations(S, n)) for n in range(1, len(S)+1))))
    
#see alexis on Stack Exchange May 8 2015
def partition(collection):
    """find additive partitions of a list S"""
    if len(collection)==1:
        yield [collection]
        return

    first=collection[0]
    for smaller in partition(collection[1:]):
        #insert 'first' in each of the subpartition's subsets
        for n, subset in enumerate (smaller):
            yield smaller[:n]+ [[first]+subset] + smaller [n+1:]
        #put 'first' in its own subset
        yield [[first]]+smaller
    
def test2(nmin,nmax):
    start=timer()
    for n in range(nmin,nmax):
        ps4(n)
    print('Elapsed time:',timer()-start)

def mp(n):
    """return multiplcative partitions of n"""
#    mps={}
    mps=[]
    pfs=prime_factors(n)
    for n,p in enumerate(partition(pfs),1):
#        mps.append(tuple([x for x in p]))
        mps.append(tuple([listprod(x) for x in p]))
    mps=list(set(mps))
    return mps
           

def test3(nmin,nmax):
    start=timer()
#    for n in range(nmin,nmax+1):
#        for n,p in enumerate(partition(prime_factors(n)),1):
#            pass
#    print(n,timer()-start)
#    return
     
    ps=set()
    nx=0
    hmax=0
    hs=[]
    ns=[]
    sps=[]
    ds=[]
    az=[]
    pz=[]
    for n in range(nmin,nmax+1):
        if n%1000==0:print(n,timer()-start)
        sp,h,a,v,p=ps4(n)
        if a==4:
            print(n,sp,h,a,v,p)
            ns.append(n)
            hs.append(h)
            sps.append(sp)
            az.append(a)
            pz.append(p)
            ds.append(len(divisors(n)))
        if h>hmax:
            hmax=h
            nx=n
        ps.add(sp)

#    plt.plot(ns,sps)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(ns,az)
    
    plt.subplot(212)
    plt.plot(ns,pz)
    plt.show()
    
    print(sum(ps))
    print(nx,hmax)
    
    print (sum([x%10==3 for x in sps]))
    
def ps5(n):
    ns=set()
    gs=set()
    ncomplete=set(list(range(1,n+1)))
    a=1
    while a<=n:
        a+=1
        print (a,len(ns))
        rmax=int(1+(np.log(n)-np.log(a))//np.log(2))
        for r in range(1,rmax+1):
            for ks in it.combinations_with_replacement(list(range(a+1,1,-1)),r):
                p=listprod(ks)
                s=sum(ks)
                newn=(a*(p-1)-s+r+1)
                if newn<=n and newn not in ns:
                    ns.add(newn)
                    gs.add(a*p)
                    if len(ns)==n-1:
                        break

    print(len(ns))
    print(gs)
    print(ncomplete)
    print (sum(gs))
                
        


    
def ps4(n):
    okts=[]
    if n in [2, 3, 4, 6, 24, 114, 174, 444]:
        okts.append((n,1,2,2,(2,),2*n))
        return 2*n,1,n,(2),2
    
    
    h=0
#    while len(okts)<=2:
    flag=False
    gmin=np.inf
    while h<=1000:
        h+=1
#        if flag:break            
#        print('n,h',n,h,len(okts))
        d=divisors(n+h-1)
        try:
            az=[(n+h-1)//x for x in d[1:-1]]
            if min(az)>n:break
            ps=[x+1 for x in d[1:-1]]
            if max(ps)<=h:break
#            gs=[(x+1)*(n+h-1)//x for x in d[1:-1]]
            
#            if len(az)==0 and h==3:
#                return 2*n

#            az=[(n+h-1)//x for x in d]
#            ps=[x+1 for x in d]
#            gs=[(x+1)*(n+h-1)//x for x in d]
            
            ts=[(az[x],ps[x]) for x in range(len(az))]
#            print('ts',h,ts)
            for  t in ts:
                a,p=t[0],t[1]
                g=a*p
#                print ('a,p,g',a,p,g)
#                print('rmax',rmax)
                mpp=mp(p)
#                print('mpp',mpp)
                for v in mpp:
                    if max(v)>a:
                        continue
                    s=sum(v)
                    r=s-h
                    if r<1: 
                        flag=True
                        continue
                    if r!=len(v):
                        continue
                    if a+s+n-r-1==a*p and g<=gmin:
                        gmin=g
#                        print(a*p==g)
#                        print('h',h,'s',s,'r',r,'n',n,'a',a,'v',v,'g',g)
                    
                        best=(a,r,s,p,v,g,h)
#                        okts.add((g))
        except:
            pass
#            print('exception')
#        if h>10:
#            break
#    print(okts)
    return best[5],best[6],best[0],best[4],best[3]
#    return min([x[5] for x in okts]),h

def psnmin2(a,b,c,m):
    """returns n,product-sum number for given m,""" 
    return (a*b*c**(m-2)-(a+b)-c*(m-2)+m,c**(m-2)*a*b,[c]*(m-2)+[a,b])

def n2(a,b,c,nmax):
    m=2
    n=m+a*b*c**(m-2)-(a+b+c*(m-2))
    yield (n)
    while n<nmax:
        m+=1
        n+=(c-1)*(a*b*c**(m-3)-1)
        yield n
    return
    
def psnmin3(nmax):
    psns={}
    count=0
    stems=[(b,a) for a in range(2,2*nmax) for b in range (2,2*nmax) if b<=a]
    print(len(stems))
    print (stems)
    for stem in stems:
        p=stem[0]*stem[1]
        s=stem[0]+stem[1]
        n=2+p-s
        if n<=nmax:
            psns[n]=(n,2,stem)
        while n<nmax:
            m=2
            for c in range(stem[0],1,-1):
                while 1:
                    m+=1
                    p*=p
                    newn=m+c*p-(s+c)
                    if p>2*n:
                        break
                    if p<psns[newn]:
                        psns[newn]=p
                
                
                
            
    for x in range(2,1201):
        if x in psns:
            count+=1
    print(count)
    return psns
    
                    
def p88(nmax):
    """returns minmal sum-product numbers up to n digits"""
    start=timer()
#    pset=set()
    psns={}
    primes=primesfrom2to(nmax)
    for n in range(2,nmax+1):
        psn,m,solution=psnmin(n,primes)
        psns[n]=(psn,m,solution)
#        print(n,psn,m,solution)
#    return
    count=0
    psums=[]
    for k,v in psns.items():
        a,b=v[2][0],v[2][1]
        newn=0
        m=2
        for c in [2,3]:
            while newn<nmax:                
                m+=1
                newn,newpsn,newsol=psnmin2(a,b,c,m)
    #            print(k,newn,newpsn,newsol)
                if newn<=nmax and newpsn<psns[newn][0]:
                    count+=1
                    psns[newn]=(newpsn,m,newsol)
    #                print(k,newn,psns[newn])
        psums.append(sum(set([v[0] for k,v in psns.items()])))
#    print (pset)
#    print(sum(pset))
    plt.plot(psums)
    print(psums[-1])
    print('replacements:',count)
    print('Elapsed time:',timer()-start)
    return psns    

def psnmin(n,primes=[]):
    """returns minimal m=2 sum-product solution for n digits"""
    if len(primes)==0:
        primes=primesfrom2to(n)

#    start=timer() 
    if n==2:
        return 4,2,[2,2]

    m=ndig(n)
    psn=np.inf
#    print (2,psns[2]       
    if n-1 in primes:
        psn=2*n
        solution=[2,n]
        
    if n-1 not in primes:
        abcands=[x+1 for x in divisors(n-1)[1:-1]]
        nf=len(abcands)
        if nf%2==1: 
            abcands=sorted(abcands+[abcands[(nf-1)//2]])                
            nf+=1
        psn=abcands[(nf-1)//2]*abcands[(nf+1)//2]
        solution=[abcands[(nf-1)//2],abcands[(nf+1)//2]]
#        print(psns)
    return psn,2,solution
 
    
from operator import itemgetter
def pfpowers(m,maxpow):
    ps=[]
    for a in it.combinations_with_replacement([x for x in range(2,maxpow+1)],m):
        ps.append(list(a))
#    return(ps)
    ranks=[]
    ps=ps[::-1]
    ranks=sorted([(i,listprod(ps[i])) for i in range(len(ps))],key=itemgetter(1))
    rps=[]
    i=0
    while True:
        yield listprod(ps[ranks[i][0]])
        i+=1
        if i>=len(ranks):
            return
#    return [listprod(rp) for rp in rps]
                          
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
                return sorted(divs) 
                
                    
def ndig(n):
    return int(1+np.log(n)/np.log(2))
                    
def listprod(numbers):
    p=1
    for i in range(len(numbers)):
        p*=numbers[i]
    return p
    
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    #Code by Robert William Hanks
    #http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[ k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]
    
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
    
def gcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b

def is_prime1(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
