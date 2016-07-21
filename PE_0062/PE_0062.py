# -*- coding: utf-8 -*-
"""

PE_0062

Find the smallest cube for which exactly five permutations of its digits are cube.

Created on Sun Jul 17 06:31:06 2016
@author: mbh
"""



def main(n):
    
    cubes={str(x**3):0 for x in range(1,n)} 
    
    candidates={}    
    for cube in cubes:
        key=''.join(x for x in sorted(cube))
        candidates.setdefault(key, []).append(cube)    

    print min([candidates[x] for x in candidates if len(candidates[x])==5])[0]   


    
    
    