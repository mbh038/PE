# -*- coding: utf-8 -*-
"""

PE_0107

Minimal network


Borůvka's algorithm (See wikipedia)
  Input: A connected graph G whose edges have distinct weights
1   Initialize a forest T to be a set of one-vertex trees, one for each vertex of the graph.
2   While T has more than one component:
3     For each component C of T:
4       Begin with an empty set of edges S
5       For each vertex v in C:
6         Find the cheapest edge from v to a vertex outside of C, and add it to S
7       Add the cheapest edge in S to T
8 
    Combine trees connected by edges to form bigger components
9   Output: T is the minimum spanning tree of G.


Created on Fri Nov 11 12:17:31 2016
@author: mbh
"""





import time
import numpy as np

def p107(filename='p107_network.txt'):
    """
    Uses Boruvka's algorithm to find weight saving of the minimum spanning tree 
    of  network compared to the original network
    """
    t=time.clock()
    #read in network from file as dict of adjancies, with weights
    network=  {i+1:set([(j+1,int(c)) for j,c in enumerate(l.strip().split(',')) if 
                c != '-' and i>j]) for i,l in enumerate(open(filename))}

    # 'trees' starts as dict of each vertex in network
    # 'where' keeps track of which sub-network each vertex belongs to
    trees,where={},{}
    for i in range(1,len(network)+1):
        trees[i]=set([i])
        where[i]=i
    
    # create empty mst network
    mstEdges=set()    
    #loop until we have just one subnetwork - this will be the mst
    while len(trees)>1:
        #find minimum weighted edge out of each sub-network
        edges=set()
        for tree in trees:
            for node in trees[tree]:
                try:
                    minedges=[x for x in network[node] if x[0] not in trees[tree]]
                    minedge=[x for x in minedges if x[1] == min([x[1] for x in minedges])][0]
                    edges.add((node,minedge[0],minedge[1]))
                except IndexError:
                    pass

        #find minimim of these and add it to the mst
        cost=np.inf
        for edge in edges:
            if edge[2]<cost:
                cost=edge[2]
                cedge=edge       
        mstEdges.add(cedge)
         
        #update subnetworks in trees, and locations in where.
        x=where[cedge[0]]
        y=where[cedge[1]]
        for node in trees[x]:
            trees[y].add(node)
            where[node]=y
        del(trees[x])
               
    mstWeight=sum([x[2] for x in mstEdges])
    originalWeight=sum([sum([x[1] for x in v]) for k,v in network.items()])
    print(originalWeight-mstWeight,time.clock()-t)          


#not used below here
#my original i/o code - much more verbose than the version adapted from hansaplast,
def readfile(filename):
    """return network as dict of weighted adjacencies""" 
    with open(filename,'r') as file:
        data  = file.readlines()
    M={}
    count=0
    for line in data:
        count+=1
        row=[]
        col=0
        for x in line.strip().split(','):
            col+=1
            if col>count: #just read in lower diagonal half of matrix
                break
            if x=='-':
                continue
            row.append((col,int(x)))
        M[count]=row
    return M

#the concide hansaplast way of reading in the network    
def hansaplast(filename='test_network.txt'):
    network =  {i+1:[(j+1,int(c)) for j,c in enumerate(l.strip().split(',')) if c != '-' 
    and i>j]for i,l in enumerate(open(filename))}
    return network
    
def totalweight(M):
    return sum([sum([x[1] for x in v]) for k,v in M.items()])

    
#Page 242, Figure 17.5
class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        """Assumes src and dest are nodes, weight a float"""
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName() + '->(' + str(self.weight) + ')'\
               + self.dest.getName()

#Page 243, Figure 17.6
class Digraph(object):
    #nodes is a list of the nodes in the graph
    #edges is a dict mapping each node to a list of its children
    def __init__(self):
        self.nodes = {}
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes[node.getName()]=node
            self.edges[node.getName()] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def addWeightedEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        weight=edge.getWeight()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append((dest,weight))
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:-1] #omit final newline

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
    def addWeightedEdge(self, edge):
        Digraph.addWeightedEdge(self,edge)
        rev = WeightedEdge(edge.getDestination(), edge.getSource(),edge.getWeight())
        Digraph.addWeightedEdge(self, rev)
        
def totalDist(graph,path):
    """Assumes path is a list of nodes"""
    totalDist=0    
    for i in range(len(path)-1):
        for d in graph.edges[Node(path[i])]:
            if d[0]==Node(path[i+1]):
                totalDist +=float(d[1][0])
    return totalDist 
    
#Page 248, Figure 17.8
def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 

def DFS(graph, start, end, path, shortest):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start[0]]
    print ('Current DFS path:', printPath(path))
    if start[0] == end[0]:
        return path
    for node in graph.childrenOf(start[0]):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def search(graph, start, end):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None)
    

