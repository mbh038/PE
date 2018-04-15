#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

PE_0425

Prime connection

46479497324

Created on Thu Mar  1 15:38:07 2018
@author: mbh
"""

import time
import os
import sys
sys.path.insert(0, os.getcwd()+'mylib')
#import graph
import numpy as np

from graph import Graph, Vertex,Queue


def p425(limit):
    g=buildGraph(limit)
    bfs(g,g.getVertex('2'))
    
    count=0
    for v in g:
        if not traverse(v):
            count+=1
            print(v.getId())
    print(count)
    traverse(g.getVertex('107'),True)
    [v.getId() for v in g.getVertex('107').getConnections()]
    
#@nb.jit(nopython=True)
def buildGraph(limit):
    
    t=time.clock()
    
    ps=primeSieve(limit)
    pset=set(ps)
    
    g=Graph()
#    for p in ps:
#        g.addVertex(p)
#        
#    return g
        
#    for v in g:
#        print(v.getId())
    
    psl=np.ones(limit,dtype=np.int64)
    i=1
    
    while len(psl)>0:
        psl=ps[ps>limit/(10**i)]
        psl=psl[psl<limit/10**(i-1)]
#        if len(psl)>0:
#            print(min(psl),max(psl))
        
        for p in psl:
            ppair=p%10**(3-i)
            if ppair in pset and ppair>10**(3-i-1):
#                g.addEdge(str(p),str(p%10**(3-i)))
                g.addEdge(str(p%10**(3-i)),str(p))
        i+=1
        
    d={}    
    for p in ps:
        
        pstr=str(p)
        for j in range(len(pstr)):
            bucket = pstr[:j] + '_' + pstr[j+1:]
            if bucket in d:
                d[bucket].append(pstr)
            else:
                d[bucket] = [pstr]
                
        # add vertices and edges for words in the same bucket
        for bucket in d.keys():
#            dbs=sorted(d[bucket])
#            dbs=dbs[::-1]
#            print(d,dbs)
            for i,p1 in enumerate(d[bucket]):
                for j,p2 in enumerate(d[bucket]):
                    if p1 != p2:
                        g.addEdge(p1,p2)
                        g.addEdge(p2,p1)
        
#    for v in g:
#        print(v.getId(),':',[vv.getId() for vv in v.getConnections()])                

    print(time.clock()-t) 
    return g       
                

def bfs(g,start):
#  pairs=[]
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getId()=='107':
                print('107: ',currentVert.getId())
            if nbr.getColor() == 'white':          
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)         
        currentVert.setColor('black') 
#  return pairs       
        

def isReachable(g,start,finish):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if nbr==finish:
          return True
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        if int(currentVert.id)<int(nbr.getPred().id):
            nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black') 
  return False

def trav(abList,s,f):
    abList=sorted(abList)
    for a in abList:
        if a[0]>a[1]:
            tmp=a[0]
            a[0]=a[1]
            a[1]=tmp
    d=-1
    a=s
    while 1:
        d=[a for a in abList if a[1]==a][0]
        a=d
        print(a)
    

    
    
    
def traverse(y,verbose=False):
    x = y
    while (x==None or x.getPred() or x.getId() !='2'):
        if verbose and x !=None: print(x.getId())
#        if int(x.getId())>int(y.getId()):
#            return False
        if x !=None:
            x = x.getPred()
    if verbose: print(x.getId()) 
    return x.getId()=='2'

def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=np.int64)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=0
    return np.nonzero(sieve)[0][2:].astype(np.int64) 

from collections import defaultdict
  
#This class represents a directed graph using adjacency list representation
#class Graph:
#  
#    def __init__(self,vertices):
#        self.V= vertices #No. of vertices
#        self.graph = defaultdict(set) # default dictionary to store graph
#  
#    # function to add an edge to graph
#    def addEdge(self,u,v):
#        self.graph[u].add(v)
      
     # Use BFS to check path between s and d
#    def isReachable(self, s, d):
#        # Mark all the vertices as not visited
#        visited =[False]*(self.V)
#  
#        # Create a queue for BFS
#        queue=[]
#  
#        # Mark the source node as visited and enqueue it
#        queue.append(s)
#        visited[int(s)] = True
#  
#        while queue:
# 
#            #Dequeue a vertex from queue 
#            n = queue.pop(0)
#             
#            # If this adjacent node is the destination node,
#            # then return true
#            if n == int(d):
#                return True
# 
#            #  Else, continue to do BFS
#            for i in self.graph[n]:
#                if visited[i] == False:
#                    queue.append(i)
#                    visited[i] = True
#         # If BFS is complete without visited d
#        return False