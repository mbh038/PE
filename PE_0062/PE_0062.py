# -*- coding: utf-8 -*-
"""

PE_0062

Find the smallest cube for which exactly five permutations of its digits are cube.

#127035954683

Created on Sun Jul 17 06:31:06 2016
@author: mbh
"""

import time

def p62(n):
    
    t=time.clock()
    
    n=int(n)
    
    cubes={str(x**3):0 for x in range(1,n)} 
    
    candidates={}    
    for cube in cubes:
        key=''.join(x for x in sorted(cube))
        candidates.setdefault(key, []).append(int(cube))    

    print (min([sorted(candidates[x]) for x in candidates if len(candidates[x])==5][0]) ) 
    
    print(time.clock()-t)


    
    
    