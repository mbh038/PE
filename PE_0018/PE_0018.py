import pylab, random
from rcParamsSettings import *
import operator

#Page 236, Figure 17.2
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value)\
                 + ', ' + str(self.weight) + '>'
        return result

def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items

#Page 237, Figure 17.3
def greedy(items, maxWeight, keyFunction):
    """Assumes Items a list, maxWeight >= 0,
         keyFunction maps elements of Items to floats"""
    itemsCopy = sorted(items, key=keyFunction, reverse = True)
    result = []
    totalValue = 0.0
    totalWeight = 0.0
    for i in range(len(itemsCopy)):
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print 'Total value of items taken = ', val
    for item in taken:
        print '   ', item

def testGreedys(maxWeight = 20):
    items = buildItems()
    print 'Use greedy by value to fill knapsack of size', maxWeight
    testGreedy(items, maxWeight, value)
    print '\nUse greedy by weight to fill knapsack of size', maxWeight
    testGreedy(items, maxWeight, weightInverse)
    print '\nUse greedy by density to fill knapsack of size', maxWeight
    testGreedy(items, maxWeight, density)

#Page 239, Figure 17.4
def chooseBest(pset, maxWeight, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)

def testBest(maxWeight = 20):
    items = buildItems()
    pset = genPowerset(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue,
                            Item.getWeight)
    print 'Total value of items taken =', val
    for item in taken:
        print item

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
    sumpath=0
    for n in path:
        sumpath += n.getValue()
    return sumpath
        
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
#            if shortest == None or sumPath(path) > sumPath(shortest):
            if shortest == None or len(path) <= len(shortest):
                newPath = DFS(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath  
    return shortest

def search(graph, start, end):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None)
#    return BFS(graph, start, end)

#Page 248, Figure 17.9
def testSP():
    nodes = []
    for name in range(6): #Create 6 nodes
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    sp = search(g, nodes[0], nodes[5])
    print 'Shortest path found by DFS:', printPath(sp)

#Page 250, Figure 17.10
def BFS(graph, start, end):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        #Get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        print 'Current BFS path:', printPath(tmpPath)
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None
    
def PE_0018(filename):
    
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
    
    pathsum=[]
    for n in [x+0.5*len(triangle)*(len(triangle)-1) for x in range(len(triangle))]:
       sp = search(g, nodes[0], nodes[int(n)])
       pathsum.append(sumPath(sp))
       print 'Shortest path found by DFS:', printPath(sp)
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
    
    # 2) Uses the string function split to line from the file
    # into a list of substrings
#    numbers = list()
#    dataFile = open('C:\\PythonCourse\\unit3\\numbers.txt', 'r')
#    
#    for eachLine in dataFile:
#        # Simplify the script by using a python inbuilt
#        # function to separate the tokens 
#        substrs = eachLine.split(',',eachLine.count(','))
#        # Iterate throught the output and check that they 
#        # are numbers before adding to the numbers list
#        for strVar in substrs:
#            if strVar.isdigit():
#                numbers.append(int(strVar))
#    
#    print numbers
#    
#    dataFile.close()