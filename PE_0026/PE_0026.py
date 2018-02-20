# -*- coding: utf-8 -*-
"""
PE_0026

Reciprocal Cycles

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.

Created on Thu Jun 23 17:28:03 2016
@author: Mike
"""

import time
import itertools as it
import numba as nb
     
def ld(n,d,digits):
    """
    returns the recurring cycle and its length for n/d where n < d.
    if there is no recurring cycle, returns 0.
    """
    
        
    ans=[]
    ns=[]
    count=0
    while count<digits:
        if d%2 == 0 or d%5 ==0:
            ns.append(0)
            break
        count +=1
        nmult=0
        while n<d:
            nmult+=1
            if nmult>1:
                ans.append(0)
                ns.append(n)
            n *= 10
        if n in ns:
            ns.append(n)
            break
        ns.append(n)
        ans.append(n/d)
        n=n%d
        if n == 0:
            ns.append(0)
            break

    lastn=ns[-1]
    strseq=[]
    for x in ans: strseq.append(str(x))
    st = ''.join(strseq)
    return st,len(ns)-ns.index(lastn)-1
    
def main(denominators):
    """#returns the value d<1000 for which has the longest recurring cycle 
    for 1/d, its length and  the cycle itself
    """
    import time
    start_time = time.time()
    maxlam=-1
    for d in denominators:
        st,s=ld(1,d,1000)
        if s>maxlam:
            maxlam=s
            maxn=d
            maxst=st
#    print ('The value of d < 1000 for which 1/d contains the longest recurring\ncycle in its decimal fraction part is',maxn)
    print ('\nLength of recurring cycle: ',maxlam)
#    print ('\nThe cycle: 0.',maxst,'...')
    print("--- %s seconds ---" % (time.time() - start_time))


#main(range(1,1000))

def testcases():
    """
    returns a dictionary 
    key : i for i in 1 to 46
    value:  length of recurrence sequence for 1/i
    from  https://en.wikipedia.org/wiki/Repeating_decimal
    Use to test function intended to find these lengths for other i.
    """
    repeats={}
    seqlen=[0,0,0,1,0,0,1,6,0,1,0,2,1,6,6,1,0,16,1,18,0,6,2,22,1,0,6,3,6,28,1,15,0,2,16,6,1,3,18,6,0,5,6,21,2,1,22,0,0,0,0,0]
    for i in range(47):
        repeats[str(i)]=seqlen[i]
    return repeats
         
def testmyld():
    for i in range(2,47):   
        st,repeat=ld(1,i,100) 
        cases=testcases()
        
        if repeat==cases.get(str(i)):
            result='Correct'
        else:
            result='Wrong'
            
        print ('n: ',i,'repeat: ',repeat,result)
  
    
#@nb.jit(nopython=True)
def recur_len(n):
    # digits for unit fraction 1/n
    r = 10 # initial remainder (10/n)/10
    seen = {} # remainder -> first pos
    for i in it.count(0):
        if r == 0:
            return 0  # divides evenly.
        elif r in seen:
            return i-seen[r] # curpos - firstpos
        seen[r] = i
        r= 10*(r % n)

def brian():
    t=time.clock()
    l,i = max((recur_len(i),i) for i in range(2,1000))
    print (i)
    print(time.clock()-t)