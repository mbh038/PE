"""
PE_0027

Quadratic Primes

Find the product of the coefficients, a and b, for the quadratic expression
 that produces the maximum number of primes for consecutive values of n, 
 starting with n = 0.


Created on Sat Jun 25 14:22:15 2016

@author: Mike
"""
import math as m
import time

def primes (n):
    """
    Use sieve of Eratosthenes to find all the primes less than or equal to n
    """
    dprimes={}
    bools=np.ones(n+1,dtype=bool)
    for i in range(2, int(m.sqrt(len(bools)))+1):
        if bools[i] == True:
            jcount=1
            while True:
                newj=i+jcount*i 
                if newj > n:
                    break
                bools[newj]=False
                jcount += 1
    primes=[]
    count=0
    for i in range(2,len(bools)): 
        if bools[i]==True: 
            count+=1
            primes.append(i)
            dprimes.update({str(i): i})
    return primes,dprimes


def main(alim,blim):
    
    # The maximum value such that n^2 +an + b is prime for all n>=0 seems always to
    # be the square of a prime : 3,5,11,17,41. I don't know why, or why just 
    # these primes, or what determines when the limit changes from the square
    # of one to the square of the next in this series. 
    start_time = time.time()
    nprimes,dprimes=primes(41**2)    
    bs  = [x for x in nprimes if x < blim] # b must be prime
    start_time = time.time()
    nnmax=None
    if alim % 2 > 0: # a mu
        alim -=1
    for b in bs:
        for a in range(-(b),alim+2,2): # a must be odd
            n=0
            trial=n**2 + a*n + b
            while True:
                n +=1
                trial += 2*n + a -1
                if trial not in nprimes:
                    nmax=n
                    break             
            if nnmax==None or nmax>nnmax:
                amax=a
                bmax=b
                nnmax=nmax
                trialmax=trial

    print("--- %s seconds ---" % (time.time() - start_time))
    print amax,bmax,nnmax,trialmax
    print amax*bmax
    return trialmax
    
def maintest(limit):
    
    nprimes=primes(41**2) #
    trialmaxs=[]
    for i in range(4,limit,2):
        bs  = [x for x in nprimes if x < i] # b must be prime
#        start_time = time.time()
        nnmax=None
        for a in range(-i+1,i,2): # a must odd
            for b in bs:
                n=0
                while True:
                    trial=n**2 + a*n + b
    #                print n,trial
                    highprimes=[i for i in nprimes if i >= trial]
                    if trial not in highprimes:#nprimes:
                        nmax=n-1
                        break
                    n +=1
                if nnmax==None or nmax>nnmax:
                    amax=a
                    bmax=b
                    nnmax=nmax
                    trialmax=trial
    #            print a,b,nmax
#        print("--- %s seconds ---" % (time.time() - start_time))
#        print amax,bmax,nnmax,trialmax
#        print amax*bmax
        trialmaxs.append(trialmax)
    return trialmaxs    

def test(a,b):
    
    nprimes,dprimes=primes(41**2)
    
    n=0
    while True:
        trial=n**2 + a*n + b
        print n,trial
        if trial not in nprimes:
            nmax=n-1
            break
        n +=1
    return nmax
    
    
