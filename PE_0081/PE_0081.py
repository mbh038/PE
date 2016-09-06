# -*- coding: utf-8 -*-
"""
Problem Euler 81

Path sum: two ways

Find the minimal path sum, in matrix.txt (right click and
 "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix,
from the top left to the bottom right by only moving right and down.

Created on Wed Jun 22 04:25:27 2016

@author: Mike
"""
from timeit import default_timer as timer
from numpy import matrix
from numpy import genfromtxt
import math as m


def PE_0081v1(filename='PE_0081.txt'):
    
    start=timer()
      
    M = genfromtxt(filename, delimiter=',')

    rows=M.shape[0]
    cols=M.shape[1]

    LSMrows = [[] for x in range(cols)]
  
    LSMrows[0].append(M[0,0])
    for col in range(1,cols):
        LSMrows[0].append(LSMrows[0][col-1]+M[0,col])
    for row in range(1,rows):
        LSMrows[row].append(LSMrows[0][row-1]+M[0,row]) 

    for row in range(1,rows):
        for col in range(1,cols):
            LSMrows[row].append(M[row,col]+min(LSMrows[row-1][col],LSMrows[row][col-1]))
    
    print('Elapsed time: ',timer()-start,'s') 
    return int(LSMrows[-1][-1])
    
    
#using Dijkstra - slower but can generalise, eg to p82 and p83.
    
def PE_0081(filename='PE_0081.txt',sn=(0,0),fn=(79,79),rules='dr'): 
    start=timer()
    M=readfile(filename)
    graph=gm(M,rules,sn,fn)
    print('Minimum path sum:',dijkstra(graph,sn,fn))
    print ('Elapsed time: ',timer()-start,'s')
    
def readfile(filename):
    """returns matrix as a list of rows"""
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
    """uses Dijkstra's algorithm to find the lowest cost path between the start
      and finish nodes in the graph. Returns the cost of that path.
    """    
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

