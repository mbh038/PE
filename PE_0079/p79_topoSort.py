#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 08:12:06 2017

@author: mbh
"""

import time

#construct a DAG from the digits of the login attempts. We know that digit 0 comes before
#digit 1 in the code, whch comes before digit 2

#Then , do DFS (I use oop DFS code from pythonDS)

# the digit order is the reverse of the finish time for each of the digits in the graph.
def p79(filename='p079_keylog.txt'):
    
    t=time.clock()
    
    g=DFSGraph()
    
    with open(filename,'r') as file:
        trios  = file.readlines() 
        
    for trio in trios:
        g.addEdge(trio[0],trio[1])
        g.addEdge(trio[0],trio[2])
        g.addEdge(trio[1],trio[2])
           
    g.dfs()
    
    code=[]
    for id in g.getVertices():
        v=g.getVertex(id)
        code.append((v.getFinish(),id))        
    code=sorted(code)
    code=code[::-1]    
    final=[c[1] for c in code]
    print(''.join([str(d) for d in final]))
    print(time.clock()-t)

#code from:
#http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
#Chapter 7
class Vertex:
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    # def __lt__(self,o):
    #     return self.id < o.id
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id
#    
#    
class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices
    
    def addEdge(self,f,t,cost=0):
            if f not in self.vertices:
                nv = self.addVertex(f)
            if t not in self.vertices:
                nv = self.addVertex(t)
            self.vertices[f].addNeighbor(self.vertices[t],cost)
    
    def getVertices(self):
        return list(self.vertices.keys())
        
    def __iter__(self):
        return iter(self.vertices.values())    

#code from
#https://runestone.academy/runestone/static/pythonds/index.html
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsVisit(aVertex)

    def dfsVisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsVisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)
        
