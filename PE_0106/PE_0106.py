# -*- coding: utf-8 -*-
"""

PE_0106

Special subset sums: meta-testing

For n = 12, how many of the 261625 subset pairs that can be obtained need to be 
tested for equality?

Created on Thu Nov 24 07:26:27 2016
@author: mbh
"""

import itertools as it
import time
 
def p106(L):
    t=time.clock()
    pset=[[x for x in it.compress(L,binLst)] for binLst in it.product([0,1],repeat=len(L))]
    p=[x for x in pset if len(x)<=len(L)//2]
    q={size:[x for x in p if len(x)==size] for size in range(2,len(L)//2+1)}
    print (time.clock()-t)
    count=0
    for size,sets in q.items():
        for i in range(len(sets)):
            for j in range(i+1,len(sets)):
                if set(sets[i]).intersection(set(sets[j]))==set():
                    if not all(sets[i][x]>sets[j][x] for x in range(len(sets[i]))):
                        count+=1
    print (count,time.clock()-t)
        
def powerset(L):
    return [[x for x in it.compress(L,binLst)] for binLst in it.product([0,1],repeat=len(L))]        
    
def p106test(L,filename='p105_sets.txt'):
    t=time.clock()    
    sets=[[int(c) for j,c in enumerate(l.strip().split(','))] for i,l in enumerate(open(filename))]
    sets=[x for x in sets if len(x)==L]
    print(sets)
    sums=0
    r2=[]
    r2r1=[]
    for L in sets:
        if rule2(L):
            sums+=sum(L)
            r2.append(sorted(L))
            if rule1(L):
                r2r1.append(sorted(L))
#            print(subset)       
    print(sums,time.clock()-t) 
    return r2,r2r1       

def isSSS(L):
    """returns True if candidate is a special sum set, False if not"""
    powerset=[[x for x in it.compress(L,binLst)] for binLst in it.product([0,1],repeat=len(L))]    
    #Rule 1
#    powersum=[sum(x) for x in powerset]
#    if len(set(powersum))<len(powerset):
#        return False
    #Rule 2
    powers=[(len(x),sum(x)) for x in powerset]
    for i in range(1,len(L)):
        if max([x[1] for x in powers if x[0]==i])>min([x[1] for x in powers if x[0]==i+1]):
            return False
    return True

#much faster, from riffraff11235
def isSpecialSumSet(s):
    uSet = set(s)
    for i in range(2,len(s)):
        maxSet = max(uSet)
        for a in it.combinations(s, i):
            ss = sum(a)
            if ss <= maxSet or ss in uSet: return False
            else: uSet.add(ss)
    return True
    
def rule1(L):
    powerset=[[x for x in it.compress(L,binLst)] for binLst in it.product([0,1],repeat=len(L))]
    powersum=[sum(x) for x in powerset]
    if len(set(powersum))<len(powerset):
        return False
    return True

def rule2(L):
    powerset=[[x for x in it.compress(L,binLst)] for binLst in it.product([0,1],repeat=len(L))]
    powers=[(len(x),sum(x)) for x in powerset]
    for i in range(1,len(L)):
        if max([x[1] for x in powers if x[0]==i])>min([x[1] for x in powers if x[0]==i+1]):
            return False
    return True
    
    

def nCk(n,k,memo={}):
    if n<k:
        return 0
    if n==0:
        return 1
    if k==0 or k==n:
        return 1
    try:
        return memo[(n,k)]
    except KeyError:
        result=nCk(n-1,k-1,memo)+nCk(n-1,k,memo)
        memo[(n,k)]=result
    return result