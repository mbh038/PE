# -*- coding: utf-8 -*-
"""

PE_0122

Efficient exponentiation

Created on Sat Nov 26 13:18:39 2016
@author: mbh
""" 
import time       
def p122(n):

    t=time.clock()
    
    memo={1:[0,{(1)},{1}],2:[1,{(1,2)},{1,2}]}
    msum=1
    for k in range(3,n+1):
        options={}
        for m in range(1,k//2+1): 
            if m in memo[k-m][2]:              
                options[m]=1+memo[k-m][0]
                
        minpath=min([v for key,v in options.items()])
        shortest=[key for key,v in options.items() if v==minpath]
        
        memo[k]=[minpath,set(),set()]
        for index in shortest:
            for x in memo[k-index][1]:
                if index in x:                    
                    memo[k][1].add((k,)+x)
                    memo[k][2].add(k)
                    for i in x:
                        memo[k][2].add(i)
        msum+=minpath
        
    print(msum,time.clock()-t)
    
    
    
#    print (len(set([x[i] for x in memo[n][1] for i in range(len(x)) ])))
    
    
#    return memo[70]
#    for k,v in memo.items():
#        try:
#            if v[0]!= min([len(x) for x in v[2]])-1:
#                print (k,v[0],v[2])
#        except:
#            print('Error!')
#            print (k,v[0],v[1],v[2])
    


def tzaman(n):
    path = [[range(1, i+1)] for i in range(n+1)]
    print (path)
    for i in range(1, len(path)):
        for j in path[i]:
            for k in [a for a in j if i+a<len(path)]: 
                if len(path[i][0])+1 < len(path[i+k][0]): path[i+k] = [j + [i+k]]
                elif len(path[i][0])+1 == len(path[i+k][0]): path[i+k].append(j + [i+k])
    print (sum(len(p[0])-1 for p in path[1:]))
        

