# -*- coding: utf-8 -*-
"""
PE_0061

Cyclical figurate numbers


Triangle	 	P3,n=n(n+1)/2	      1, 3, 6, 10, 15, ...
Square	 	P4,n=n2   	 	      1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2         1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...

Find the sum of the only ordered set of six cyclic 4-digit numbers for which
each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and
octagonal, is represented by a different number in the set.

Created on Tue Jul 26 13:38:44 2016
@author: mbh
"""


# find sets of each type

from timeit import default_timer as timer
from itertools import permutations
def p3():
    start=timer()
    p3,p4,p5,p6,p7,p8=[],[],[],[],[],[]
    for n in range (1,140):
        p3.append(n*(n+1)//2)
        p4.append(n**2)
        p5.append(n*(3*n-1)//2)
        p6.append(n*(2*n-1))
        p7.append(n*(5*n-3)//2)
        p8.append(n*(3*n-2))
            
    p3=[x for x in p3 if len(str(x))==4]
    p4=[x for x in p4 if len(str(x))==4]
    p5=[x for x in p5 if len(str(x))==4]
    p6=[x for x in p6 if len(str(x))==4]
    p7=[x for x in p7 if len(str(x))==4]
    p8=[x for x in p8 if len(str(x))==4]
    
    notfound=True
    for perm in permutations([(3,p3),(4,p4),(5,p5),(6,p6),(7,p7),(8,p8)]):
        if notfound==False:
            break
        path=[]
        i=0
        for a in perm[i][1]:
            path=[(a,perm[i][0])]           
            for b in perm[i+1][1]:
                if str(b)[:2]==str(a)[-2:]:
                    path.append((b,perm[i+1][0]))
                    for c in perm[i+2][1]:
                        if str(c)[:2]==str(b)[-2:]:
                            path.append((c,perm[i+2][0]))
                            for d in perm[i+3][1]:
                                if str(d)[:2]==str(c)[-2:]:
                                    path.append((d,perm[i+3][0]))
                                    for e in perm[i+4][1]:
                                        if str(e)[:2]==str(d)[-2:]:
                                            path.append((e,perm[i+4][0]))
                                            for f in perm[i+5][1]:
                                                if str(f)[:2]==str(e)[-2:]:
                                                    path.append((f,perm[i+5][0]))
                                                    for a in perm[i][1]:
                                                        if str(a)[:2]==str(f)[-2:]:
                                                            path.append((a,perm[i][0]))
                                                            if path[0][0]==path[-1][0]:
                                                                if len(set([path[j][0] for j in range(len(path))]))==len([path[j][0] for j in range(len(path))])-1:
                                                                    print(path,sum([path[i][0] for i in range(len(path)-1)]))
                                                                    notfound=False
                                                                    break
         
            
                                                
    print('Elapsed time: ',timer()-start)
                                                            
            
    




