# -*- coding: utf-8 -*-
"""

PE_0109

Darts

How many distinct ways can a player checkout with a score less than 100?

Created on Wed Nov 23 09:35:57 2016
@author: mbh
"""
import time
        
def p109(limit=100):
    
    t=time.clock()

    #doubles
    dd=[2*x for x in range(1,21)]+[50]
    #1-dart scores
    d1=[x*y for x in range(1,21) for y in [1,2,3]]+[25,50]
    #1-dart and distinct two dart scores
    d1d2=[x for x in d1+[d1[i]+d1[j] for i in range(62) for j in range(i,62)]] 
   
    total=len([x for x in dd if x<limit])+len([x+y for x in dd for y in d1d2 if x+y < limit])

    print(total,time.clock()-t)

# first version - much slower
def p109_v1(limit=100):
    
    t=time.clock()

    S={'S'+str(x):x for x in range(1,21)}
    S['S25']=25
    D={'D'+str(x):2*x for x in range(1,21)}
    D['D25']=50
    T={'T'+str(x):3*x for x in range(1,21)}    
    Z={**S,**D,**T}

    #possible scores with one dart
    firstOneScore=sorted([v for k,v in Z.items()])
    #possible scores with two darts
    firstTwoK=set([])
    for k1,v1 in Z.items():
        for k2,v2 in Z.items():
            firstTwoK.add(tuple(sorted((k1,k2))))
    firstTwoScore=[]
    for pair in firstTwoK:
        firstTwoScore.append(Z[pair[0]]+Z[pair[1]])
        
    #for each checkout below the limit...
    total=0
    total1=0
    total2=0
    total3=0
    for checkout in range(2,limit): 
        #the checkout is itself a double
        ways1=len([v for k,v in D.items() if v==checkout])
        total1+=ways1
        #in how many ways can the first one or two dats take us to a score that is a double
        ways2,ways3=0,0
        for k,v in D.items():
            required=checkout-v
            if required<1:
                continue       
            ways2+=len([x for x in firstOneScore if x==required])
            ways3+=len([x for x in firstTwoScore if x==required])
        total2+=ways2
        total3+=ways3
        total+=ways1+ways2+ways3
    print ('1',total1)
    print ('2',total2)
    print ('3',total3)
#    print(limit,total,time.clock()-t)
    return total
        
    
    
    

