# -*- coding: utf-8 -*-
"""
Good recursive solutions to p88, found on the thread after I posted my much slower
solution.
Created on Sat Oct  8 06:48:47 2016
@author: mbh
"""
import time
#from nanogyth - creating factors instead of factorising : 160 ms

def find_total_sum_prod(MAX):
    t=time.clock()
    def update_list(s=0,p=1,factors=0,start=2,sp_list=[2*MAX]*MAX):
        terms = p - s + factors
        if terms < MAX and sp_list[terms] > p:
            sp_list[terms] = p
        stop = 2*MAX if p == 1 else (MAX+s)//(p-1)
        for n in range(start,stop+1):
            update_list(s+n, p*n, factors+1, n)
        return sp_list

    print( sum(set(update_list()[2:])),time.clock()-t)

#from under-score - similar to Marcus Stuhr, but 25% faster. - 240 ms
def recurse(p, s, n, start):
    k = n + p - s
    if k > kmax: return
    if p < N[k]: N[k] = p
    for x in range(start, 2*kmax//p+1):
        recurse(p*x, s+x, n+1, x)

t=time.clock()
kmax = 12000
N = [3*kmax] * (kmax+1)
recurse(1, 0, 0, 2)
print (sum(set(N[2:])),time.clock()-t)               
                
#from Marcus Stuhr - abour 310 ms

N = 12000
arr = [2*N+1]*(N+1)

def fillArr(depth,prodL,sumL,minElement):
    numOnes = abs(sumL-prodL)
    k = depth + numOnes
    if k > N: return
    arr[k] = min(arr[k], prodL)

    for i in range(minElement, 2*N//prodL+1):
        fillArr(depth+1,i*prodL,sumL+i,i)

t = time.clock()
fillArr(0,1,0,2)
print (sum(set(arr[2:N+1])), time.clock()-t)