# -*- coding: utf-8 -*-
"""

PE_0082

Path sum: three ways

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the 
left column and finishing in any cell in the right column, and only moving up, 
down, and right, is indicated in red and bold; the sum is equal to 994.

Created on Thu Aug 25 02:51:48 2016
@author: mbh
"""

from timeit import default_timer as timer
import math as m

#def PE_0082(filename='test.txt',rules='udr'):

def PE_0082(filename='p082_matrix.txt',sn='vl',fn='vr',rules='udr'): 
    start=timer()
    M=readfile(filename)
    graph=gm(M,rules,sn,fn)
    print('Minimum path sum:',dijkstra(graph,sn,fn))
    print ('Elapsed time: ',timer()-start,'s')
    
def readfile(filename):
    with open(filename,'r') as file:
        data  = file.readlines()
    return [[int(x) for x in line.split(',')] for line in data]


def gm(M,rules,sn='vl',fn='vr'): 
    rows,cols=len(M),len(M[0])
    nodes={(r,c):[m.inf,M[r][c],[]] for r in range(rows) for c in range(cols)}    
    movedict={'u':(-1,0),'d':(1,0),'l':(0,-1),'r':(0,1)}
    moves=[movedict[rule] for rule in [letter for letter in rules]]
    
    for node in nodes:
        for n in moves:
            nodes[node][2].append(tuple(p+q for p, q in zip(node, n)))            

    if sn=='vl':
        nodes['vl']=[m.inf,0,[(r,0) for r in range(rows)]] 
        for r in range(rows):
            nodes[(r,0)][2].append('vl') 
    
    if fn=='vr':
        nodes['vr']=[m.inf,0,[(r,cols-1) for r in range(rows)]] 
        for r in range(rows):
            nodes[(r,cols-1)][2].append('vr') 

    return nodes
    
def dijkstra(graph,sn,fn):
     
    nv={}
    cn=sn
    graph[cn][0]=graph[cn][1]
    while 1:
        for nn in graph[cn][2]:
            try:
                value=graph[cn][0]+graph[nn][1]
                if value<graph[nn][0]:
                    graph[nn][0]=value
                    nv[nn]=graph[nn]
            except KeyError:
                pass  
        cnv,cn = min((v[0],k) for k,v in nv.items()) 

        if cn==fn: break
        del(nv[cn]) 

    return int(nv[fn][0])        
    
