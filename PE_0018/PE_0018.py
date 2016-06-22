import pylab, random
from rcParamsSettings import *
import operator
import time

def PE_0018(filename):
    start_time = time.time()
    triangle = readcsv(filename)
    print triangle
    frontier=triangle[-1]
    for line in range(len(triangle)-2,-1,-1):
        newFrontier=[]
        for number in range(len(triangle[line])):
            newFrontier.append(triangle[line][number]+max(frontier[number],frontier[number+1]))           
        frontier=newFrontier
    print ' Maximum sum=: ',frontier[0] 
    print("--- %s seconds ---" % (time.time() - start_time))        
    return frontier

# Attempt at DFS OOP - but it does not work!!

#Page 242, Figure 17.5
class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def setValue(self,value):
        self.value=value
    def getValue(self):
        return self.value
    def setLine(self,line):
        self.line=line
    def getLine(self):
        return self.line
    def setNumber(self,number):
        self.number=number
    def getNumber(self):
        return self.number
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
        self.nodes = []
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
#    def addWeightedEdge(self, weightededge):
#        src = weightededge.getSource()
#        dest = weightededge.getDestination()
#        weight = weightededge.getWeight()
#        if not(src in self.nodes and dest in self.nodes):
#            raise ValueError('Node not in graph')
#        self.edges[src].append(dest)
#        self.edges[src].append(weight)
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

#Page 248, Figure 17.8
def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''    
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 

def sumPath(path):
    """Assumes path is a list of nodes"""
    sumpath=0
    for n in path:
        sumpath += n.getValue()
    return sumpath
    
#def sumEdge(path):
#    """Assumes path is a list of nodes"""
#    sumedge=0
#    for n in path:
#        sumedge += n.getValue()
#    return sumedge
        
def DFS(graph, start, end, path, shortest):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start]  
    print 'Current DFS path:', printPath(path),'path sum: ',sumPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
#            print 'Current DFS path:', printPath(path),'path sum: ',sumPath(path)
            if shortest == None or sumPath(path) > sumPath(shortest):
                if shortest != None:
                    print 'Current DFS path:', printPath(path),'path sum: ',sumPath(path)
                    print 'Current shortest path:', printPath(shortest),'path sum: ',sumPath(shortest)
#            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath  
    return shortest

def search(graph, start, end):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None)
#    return BFS(graph, start, end)


def PE_0018DFS(filename):
    
    #lines=[]
    nodes=[]
    #nnodes=0
    n=0
    g = Digraph()
    triangle = readcsv(filename)
    for line in range(len(triangle)):
        for number in range(len(triangle[line])):
            nodes.append(Node(str(n)))
            nodes[n].setLine(line)
            nodes[n].setNumber(number)
            nodes[n].setValue(triangle[line][number])
            n=n+1
                     
    g = Digraph()
    for n in nodes:
        g.addNode(n)
        
    for line in range(len(triangle)-1): 
        for number in range(len(triangle[line])):
            parent = [nodes[t] for t in range(len(nodes)) if nodes[t].getLine() == line and nodes[t].getNumber()==number]
            child1 = [nodes[t] for t in range(len(nodes)) if nodes[t].getLine() == line+1 and nodes[t].getNumber()==number]
            child2 = [nodes[t] for t in range(len(nodes)) if nodes[t].getLine() == line+1 and nodes[t].getNumber()==number+1]
#            print parent[0].getLine(),parent[0].getNumber()
#            print child1[0].getLine(),child1[0].getNumber(),child2[0].getLine(),child2[0].getNumber()
            g.addEdge(Edge(parent[0],child1[0]))
            g.addEdge(Edge(parent[0],child2[0]))
#            g.addWeightedEdge(WeightedEdge(parent[0],child1[0],child1[0].getValue()))
#            g.addWeightedEdge(WeightedEdge(parent[0],child2[0],child2[0].getValue()))
    
    pathsum=[]
    for n in [x+0.5*len(triangle)*(len(triangle)-1) for x in range(len(triangle))]:
       sp = search(g, nodes[0], nodes[int(n)])
       pathsum.append(sumPath(sp))
       print 'Shortest path found by DFS:', printPath(sp)
       print
#    sp = search(g, nodes[0], nodes[8])
#    pathsum.append(sumPath(sp))
#    print 'Shortest path found by DFS:', printPath(sp)
    return g,pathsum
    
    
    
    
def readcsv (filename):
    #Import the string functions from python
    import string
    
    # 1) Splits the text file into individual characters
    # to identify the commas and parsing the individual 
    # tokens.
    
    # create a list to store the inputted numbers
    numbers = list()
    # Open the input text file for reading
    dataFile = open(filename, 'r')
    
    # Loop through each line of the input data file
    for eachLine in dataFile:
        numbersline=list()
    # setup a temporay variable
        tmpStr = ''
        # loop through each character in the line
        for char in eachLine:
            # check whether the char is a number
            if char.isdigit():
                # if it is a number add it to the tmpStr
                tmpStr += char
                # if a comma is identified and tmpStr has a 
                # value then append it to the numbers list
            elif char == ',' and tmpStr != '':
                numbersline.append(int(tmpStr))
                tmpStr = ''
        # if the tmpStr contains a number add it to the 
        # numbers list.
        if tmpStr.isdigit():
            numbersline.append(int(tmpStr))
        numbers.append(numbersline)
    # Print the number list
    #print numbers
    # Close the input data file.
    dataFile.close()
    return numbers
 