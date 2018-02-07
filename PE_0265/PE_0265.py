#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0265

Binary Circles

2: 3 (1)
3: 52 (2)
4: 51504 (16)
5: 209110240768 (2048)

See
https://graphics.stanford.edu/~seander/bithacks.html#NextBitPermutation

Created on Thu Feb  1 22:19:27 2018
@author: mbh
"""

import time
import math

def p265(N):

    t=time.clock()        
        
    lMid=2**N-N-2
    nHigh=2**(N-1)-2    
    trial=int('0'*(lMid-nHigh)+'1'*nHigh,2)
    trialHigh=int('1'*nHigh+'0'*(lMid-nHigh),2)    
    high=2**N
    highBits='0'*N+'1'
    lowBits='1'+'0'*(N-1)
    total=0
    while trial <= trialHigh:
        flag=True
        bits=highBits+'0'*(lMid-trial.bit_length())+bin(trial)[2:]+lowBits
        seqs=set([bits[:N]])
        start=1
        while start<high:
            seq=bits[start:start+N]
            if seq in seqs:
                flag=False
                break
            seqs.add(seq)
            start+=1            
        if flag:
            total+=int(bits[:-(N-1)],2)
        trial=bitTwiddle(trial) 

    print(total)
    print(time.clock()-t)

#https://www.cl.cam.ac.uk/~am21/hakmemc.html
#https://www.cl.cam.ac.uk/~am21/hakmemc.html
#return next number higher than trial with same number of high bits as trial
def hm175(a):
    c = a & -a
    r=a+c
    return (a^r)//c>>2 | r 

def bitTwiddle(v):
    t = (v | (v - 1)) + 1;  
    return  t | ((((t & -t) // (v & -v)) >> 1) - 1)
    
def howMany(n,k):
    low=int('0'*(n-k)+'1'*k,2)
    high=int('1'*k+'0'*(n-k),2)
    
    trial=low
    count=1
    while trial != high:
        trial=hm175(trial)
        count+=1
    print(count)

#other users
                
def mrDrake():
    print (f(3, "0"*3))
#    print (f(5, "0"*5))
    
def f(n, s):
    if len(s) == 2**n + n-1:
        print(s)
        return int(s[:2**n], 2)
    dsum=0
    for d in "01":
        if (s+d)[-n:] not in s:
            dsum+= f(n,s+d)
            print (d,s+d)
    return dsum

#https://github.com/smacke/project-euler/blob/master/python/265.py    
def smacke():
    print (s(0,set([]),0,0))
    
def s(cur,used,i,n):
    if i==32: return n>>5
    if cur in used: return 0
    used.add(cur)
    total = s((cur<<1)&31,used,i+1,n<<1)
    total += s(((cur<<1)+1)&31,used,i+1,(n<<1)+1)
    used.remove(cur)
    if i==31: return total>>1
    return total


#fakesson
#import numba as nb
import numpy as np

#0.3s if use numba(), 113s without.
def fakesson(N):
    t=time.clock()
    print(euler265(N))
    print(time.clock()-t)
    
#@nb.jit(nopython=True)
def euler265(N):
  Nm1 = N-1
  m = 2**N
  z = 2**(N-1)
  v = np.empty(m, dtype=np.int32)
  e = 2**(2**N-N)
  x_ = 2**(z-1)-1 + (e >> 1)
  res = 0
  while x_ < e:
    x = x_
    for i in range(m):
      v[i] = 0
    y = 0
    for _ in range(m):
      y0=y
      y =  (y >> 1) + ((x & 1) << Nm1)
      print (x,x&1,y0,y)
      if v[y]:
        break
      v[y] = 1
      x = x >> 1 
    else:
      res += x_
    t = (x_ | (x_ - 1)) + 1
    x_ = t | ((((t & -t) // (x_ & -x_)) >> 1) - 1)
    print(x_)
  return res

#user hsmart
def int_to_binary_string(n, l):
    result = ''
    while n:
        if n % 2:
            result = '1' + result
        else:
            result = '0' + result
        n = n/2
    while len(result) < l:
        result = '0' + result
    return result

def unique(l, n, short=None):
    l2 = l+l
    subs = []
    if not short:
        r = len(l)
    else:
        r = short
    for i in range(r):
        subs.append(l2[i:i+n])
    return len(subs) == len(set(subs))

def bin_str_to_int(s):
    ns = s[::-1]
    result = 0
    for i in range(len(ns)):
        if ns[i] == '1':
            result += 2**i
    return result

def hsmart(n=5):
    t=time.clock()
    digits = 2**n
    starts = [int_to_binary_string(0,n) +'1']
    while len(starts[0]) < digits:
        new_starts = []
        for start in starts:
            for dig in ['0', '1']:
                if unique(start+dig, n, len(start+dig)-n+1):
                    new_starts.append(start+dig)
        if len(new_starts) == 0: print (starts)
        starts = new_starts
    answer = 0
    for result in starts:
        if not unique(result, n): continue
        answer += bin_str_to_int(result)
    print(answer)
    print(time.clock()-t)
#    return answer
    
#number of solutions to (k,n) where k is alphabet length (=2, normally, and in this case: 0,1)
# and n is the length of the subsequence, 2^n the length of the clock.
def deBruijn(k,n):    
    return (math.factorial(k)**k**(n-1))//k**n    

#Wikipedia
def de_bruijn(k, n):
    """
    de Bruijn sequence for alphabet k
    and subsequences of length n.
    """
    try:
        # let's see if k can be cast to an integer;
        # if so, make our alphabet a list
        _ = int(k)
        alphabet = list(map(str, range(k)))

    except (ValueError, TypeError):
        alphabet = k
        k = len(k)

    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    return "".join(alphabet[i] for i in sequence)

#print(de_bruijn(2, 3))
#print(de_bruijn("abcd", 2))