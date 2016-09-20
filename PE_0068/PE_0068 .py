# -*- coding: utf-8 -*-
"""

PE_0068

Magic 5-gon ring

Created on Sat Aug 27 10:25:17 2016
@author: mbh
"""
from timeit import default_timer as timer
import itertools as it
def magicNgon(n):
    """
    Solves Project Euler 68 for magic n-gon ring, where n is the number
    of vertices in the central ring, each vertex having a spur, giving 2n
    positions in all, each filled by a unique integer in the range 1...2n
    """
    start=timer()
    numlist=[x for x in range(1,2*n+1)]
    ringlist=[x for x in range(1,n+1)]
    #The n-gon has a central ring and spurs. First get all possible central rings.
    #These must only contain the lowest n-digits.
    rings=set()
    for perm in it.permutations(ringlist,len(ringlist)):
        #remove those rings where more than two neighbour pairs sum to the same value
        ns=set([(perm[i]+perm[i+1]) for i in range(len(perm)-1)])
        ns.add(perm[-1]+perm[0])
        if len(ns)==len(perm):
            #remove duplicates eg (1,2,3,4,5) is the same ring as (2,3,4,5,1)
            plist=recycle(perm)
            rings.add(tuple(plist)) 
    rowcatmax=-1
    for ring in rings:
        #find the list of spur values for the given ring        
        spurs=[x for x in it.permutations(tuple(set(numlist).difference(set(ring))),len(ring))]
        #make list from the ring of possible pairs within n-gon 3-rows
        pairs=[(ring[i],ring[i+1]) for i in range(len(ring)-1)]
        pairs.append((ring[-1],ring[0]))
        for spur in spurs:
            #for each list of pairs, append all possible permutations of spur values
            rows=[(spur[i],pairs[i][0],pairs[i][1]) for i in range(len(spur))]
            rowtotals=set([sum(row) for row in rows])
            #as soon as we get different row sums, the n-gon cannot be magic, so ditch this ring
            if len(rowtotals)>1:
                continue
            #otherwise find the integer value of the clockwise concatenated row values,
            #with the rows cycled until that with the minimum spur value is first
            rows=recycle([int(''.join(str(x) for x in row)) for row in rows])
            rowcat=''.join(str(row) for row in rows)
            #we only want 16 digit values - ie solutions with '10' in a spur.
            if len(rowcat)==17:
                continue
            rowcat=int(rowcat)
            #find the  maximum concatenation of row values.
            if rowcat>rowcatmax:
                rowcatmax=rowcat 
    print (rowcatmax)
    print ('Elapsed time:',timer()-start,'s')
                   
def recycle(mylist):
    """cycles a list of numerical values until list[0]=min(list)"""    
    minval=mylist.index(min(mylist))   
    return [mylist[(x+minval)%len(mylist)] for x in range(len(mylist))]

        



    
    

