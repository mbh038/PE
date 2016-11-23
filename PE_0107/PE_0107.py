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


Kruskal's algorithm: (see https://www.ics.uci.edu/~eppstein/161/960206.html)
    sort the edges of G in increasing order by length
    keep a subgraph S of G, initially empty
    for each edge e in sorted order
        if the endpoints of e are disconnected in S
        add e to S
    return S
    
Created on Fri Nov 11 12:17:31 2016
@author: mbh
"""





import time
import numpy as np

def p107Boruvka(filename='p107_network.txt'):
    """
    Uses Boruvka's algorithm to find weight saving of the minimum spanning tree 
    of  network compared to the original network
    """
    t=time.clock()
    #read in network from file as dict of adjacancies, with weights
    network=  {i+1:set([(j+1,int(c)) for j,c in enumerate(l.strip().split(',')) if 
                c != '-' and i>j]) for i,l in enumerate(open(filename))}

    # 'trees' starts as dict of each vertex in network
    # 'where' keeps track of which sub-network to which each vertex belongs
    trees,where={},{}
    for i in range(1,len(network)+1):
        trees[i]=set([i])
        where[i]=i
    
    # create empty mst network
    mstEdges=set() 
    #loop until we have just one sub-network - this will be the mst
    while len(trees)>1:
        #find minimum weighted edge out of each sub-network
        edges=set()
        for tree in trees:
            for node in trees[tree]:
                try:
                    minedges=[x for x in network[node] if x[0] not in trees[tree]]
                    v1,v2=[x for x in minedges if x[1] == min([x[1] for x in minedges])][0]
                    edges.add((node,v1,v2))
                except IndexError:
                    pass

        #find minimum of these and add it to the mst
        cost=np.inf
        for v1,v2,w in edges:
            if w<cost:
                cost=w
                c1,c2,cw=(v1,v2,w)       
        mstEdges.add((c1,c2,cw))

        #update subnetworks in 'trees', and locations in 'where'.
        v1,v2=where[c1],where[c2]
        for node in trees[v1]:
            trees[v2].add(node)
            where[node]=v2
        del(trees[v1])
                
    mstWeight=sum([x[2] for x in mstEdges])
    originalWeight=sum([sum([x[1] for x in v]) for k,v in network.items()])
    print(originalWeight-mstWeight,time.clock()-t) 
    return mstEdges         

#now try it with Kruskal's algorithm
#Kruskal's algorithm: (see https://www.ics.uci.edu/~eppstein/161/960206.html)
#    sort the edges of G in increasing order by length
#    keep a subgraph S of G, initially empty
#    for each edge e in sorted order
#        if the endpoints of e are disconnected in S
#        add e to S
#    return S
def p107Kruskal(filename='test_network.txt'):
    t=time.clock()
    network =  sorted([(int(c),i+1,j+1) for i,l in enumerate(open(filename)) for j,c in enumerate(l.strip().split(',')) if c != '-' 
    and i<j])
    print(time.clock()-t)
    nvertices=len(set([x[1] for x in network]+[x[2] for x in network]))
    originalWeight=sum([x[0] for x in network])
    print('Original weight:',originalWeight)
    w,v1,v2=[x for x in network[0]]
    V={1:set([v1,v2])}
    mst=[]
    S=w    
    for w,v1,v2 in network[1:]:
        #once all vertices are in one sub-netork, we are done
        if len(V)==1 and len([v for k,v in V.items()][0])==nvertices:
            break
        S+=w
        mst.append((w,v1,v2))
        newbag=max([k for k,v in V.items()])+1
        nodes={node:bag for bag,vertices in V.items() for node in [v1,v2] if node in vertices}
        if len(nodes)==2:
            bag1,bag2=[v for k,v in nodes.items()]
            if bag1==bag2: #both ends of edge are connected - omit this edge
                S-=w
                del(mst[-1])
                continue
            V[newbag]=V[bag1].union(V[bag2])
            del(V[bag1])
            del(V[bag2])
        if len(nodes)==1:
            node,bag=[(node,nodes[node]) for node in nodes][0]
            V[bag].add(v1)
            V[bag].add(v2)
        if len(nodes)==0:
            V[newbag]=set([v1,v2])
    print(originalWeight-S,time.clock()-t)
    return mst    

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

#the concise hansaplast way of reading in the network    
def hansaplast(filename='test_network.txt'):
    network =  {i+1:[(j+1,int(c)) for j,c in enumerate(l.strip().split(',')) if c != '-' 
    and i>j]for i,l in enumerate(open(filename))}
    return network
    
def totalweight(M):
    return sum([sum([x[1] for x in v]) for k,v in M.items()])

#hansaplast's implementation of Kruskal for p107:
def p107hansaplast():
    t=time.clock()
    edges = [(int(c),i,j) for i,l in enumerate(open('p107_network.txt'))
                      for j,c in enumerate(l.strip().split(',')) if c != '-' and i<j]
    new_weight, trees = 0, [{i} for i in range(40)]
    for weight,v1,v2 in sorted(edges):
    	t1,t2 = [next(t for t in trees if s in t) for s in [v1,v2]]
    	if t1 != t2:
    		trees = [t for t in trees if t not in [t1,t2]] + [t1|t2]
    		new_weight += weight
    print(sum(e[0] for e in edges)-new_weight,time.clock()-t)