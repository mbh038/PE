# -*- coding: utf-8 -*-
"""
Problem Euler 83

Path sum: four ways

Same as problem 81, but movement rules are different.

The code is exactly as for problem 81, but with a different rules argument.

Find the minimal path sum, in matrix.txt (right click and
 "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix,
from the top left to the bottom right by only moving left,right,up and down.

Created on Wed Jun 22 04:25:27 2016

@author: Mike
"""
from timeit import default_timer as timer
import math as m
   
#ssame code as for P_0081, just with different neighbour rules  
def PE_0083(filename='p083_matrix.txt',sn=(0,0),fn=(79,79),rules='udlr'): 
    start=timer()
    M=readfile(filename)
    graph=gm(M,rules,sn,fn)
    print('Minimum path sum:',dijkstra(graph,sn,fn))
    print ('Elapsed time: ',timer()-start,'s')
    
def readfile(filename):
    with open(filename,'r') as file:
        data  = file.readlines()
    return [[int(x) for x in line.split(',')] for line in data]

def gm(M,rules,sn,fn): 
    """returns a graph as a dictionary,indexed by coordinate. The values of each
    element are a list of three components - the first is the total cost of visiting 
    that element, along the chosen path, the second is the cost of that element and 
    the third is a list of coordinates of the elements to which the element is 
    directly connected as determined by the rules
    
    'vl','vr','vt' and 'vb are virtual nodes used to denote/finihing starting anywhere on
    the left,right, top or bottom  edges. .
    """

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
    if fn=='vt':
        nodes['vt']=[m.inf,0,[(0,c) for c in range(cols)]] 
        for c in range(cols):
            nodes[(0,c)][2].append('vt') 
    if fn=='vb':
        nodes['vb']=[m.inf,0,[(rows-1,c) for c in range(cols)]] 
        for c in range(cols):
            nodes[(rows-1,c)][2].append('vb')             
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
#        print(nv)
        cnv,cn = min((v[0],k) for k,v in nv.items()) 

        if cn==fn: break
        del(nv[cn]) 

    return int(nv[fn][0]) 