# -*- coding: utf-8 -*-
"""
PE_0026

Reciprocal Cycles

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.

Created on Thu Jun 23 17:28:03 2016
@author: Mike
"""     
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
    """#returns the value d<1000 for which has the longest recrringing cycle 
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
    print 'The value of d < 1000 for which 1/d contains the longest recurring\ncycle in its decimal fraction part is',maxn
    print '\nLength of recurring cycle: ',maxlam
    print '\nThe cycle: 0.',maxst,'...'
    print("--- %s seconds ---" % (time.time() - start_time))


main(range(1,1000))

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
            
        print 'n: ',i,'repeat: ',repeat,result
  
  
  
def floyd(s, f, x0):
    # from https://en.wikipedia.org/wiki/Cycle_detection

    # Main phase of algorithm: finding a repetition x_i = x_2i.
    # The hare moves twice as quickly as the tortoise and
    # the distance between them increases by 1 at each step.
    # Eventually they will both be inside the cycle and then,
    # at some point, the distance between them will be
    # divisible by the period λ.
    tortoise = f(x0) # f(x0) is the element/node next to x0.
#    print tortoise
    hare = f(f(x0))
#    print hare
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
#        print tortoise,hare
  
    # At this point the tortoise position, ν, which is also equal
    # to the distance between hare and tortoise, is divisible by
    # the period λ. So hare moving in circle one step at a time, 
    # and tortoise (reset to x0) moving towards the circle, will 
    # intersect at the beginning of the circle. Because the 
    # distance between them is constant at 2ν, a multiple of λ,
    # they will agree as soon as the tortoise reaches index μ.

    # Find the position μ of first repetition.    
    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)   # Hare and tortoise move at same speed
        mu += 1
 
    # Find the length of the shortest cycle starting from x_μ
    # The hare moves one step at a time while tortoise is still.
    # lam is incremented until λ is found.
    lam = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lam += 1
 
#    print lam,mu
    return lam, mu
    

    



