# -*- coding: utf-8 -*-
"""

PE_0090

Cube digit pairs

Created on Wed Nov 30 15:11:13 2016
@author: mbh
"""

import  time
import itertools as it

def p90():
    
    t=time.clock()
    
    digits=set([0,1,2,3,4,5,6,7,8,9])
    
    pairs=set()
    for set1 in it.combinations(digits,6):
        set1x=set(set1)
        if 6 in set1x: set1x.add(9)
        if 9 in set1x: set1x.add(6)
        for set2 in it.combinations(digits,6):
            set2x=set(set2)
            if 6 in set2x: set2x.add(9)
            if 9 in set2x: set2x.add(6)
            squares={'01':0,'04':0,'09':0,'16':0,'25':0,'36':0,'49':0,'64':0,'81':0}
            for d1 in set1x:
                for d2 in set2x:
                    n1=str(d1)+str(d2)
                    n2=str(d2)+str(d1)
                    if n1 in squares:
                        squares[n1]+=1
                    if n2 in squares:
                        squares[n2]+=1
            if all([v>0 for k,v in squares.items()]):
                pairs.add(tuple(sorted((set1,set2))))
                
    print(len(pairs),time.clock()-t)
    
#    return pairs
    
                        
def HuggyHermit():
    t=time.clock()
    print (sum(all(((d1 in c1 and d2 in c2) or (d2 in c1 and d1 in c2))
              for d1, d2 in ((0,1),(0,4),(0,6),(1,6),(2,5),(3,6),(4,6),(8,1)))
              for c1, c2 in it.combinations(it.combinations([x for x in range(9)]+[6], 6), 2)))
    print(time.clock()-t)