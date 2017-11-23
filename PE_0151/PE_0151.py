# -*- coding: utf-8 -*-
"""

PE_051

Paper sheets of standard sizes: an expected-value problem

Created on Fri Apr 28 17:05:55 2017
@author: mbh

"""
import random as rd
import time

def p151():
    
    n=4
    t=time.clock()
    smaller={8:[4,2,1],4:[2,1],2:[1],1:[]}
    am=[({8:1,4:1,2:1,1:1},0)]
    pm=[]
    
    print(am)
    for k in range(1,2**n-2):
        flag=0
        weights={k:1 for k in range(2**n)}
        print("k=",k)
#        print("am: ",am)
        envcount=-1
        for envelope in am:
            envcount+=1
            sheets=envelope[0]
            weight=envelope[1]
            nSheets=sum([nSize for sheetSize,nSize in sheets.items()])
            if nSheets==1:
                weight*=1
            for sheetSize,nSize in sheets.items():
#                print(sheetSize,nSize)
                if nSize==0:
                    continue
                newEnvelope=sheets.copy()#{k:v for k,v in sheets.items()}
                newEnvelope[sheetSize]-=1#=sheets[sheetSize]-1
                for m in smaller[sheetSize]:
                    newEnvelope[m]+=1#sheets[m]+1
                nSheetsNew=sum(newEnvelope.values())#sum([nSize for sheetSize,nSize in newEnvelope.items()])
                if nSheets==1:
                    weight*=nSize/nSheetsNew
                    flag+=1
                pm.append((newEnvelope,weight))
#                print(envcount,sheetSize,newEnvelope,weight)
#        print("pm: ",pm)
        print(len(am),len(pm))
        am=pm[:]
        pm=[]
        
        print (sum([x[1] for x in am])/len(am))
        if flag: print("Batch: ",k,", ",flag, "Single sheet(s)")
        
#        for envelope in am:
#            weights[envelope[1]]+=1
#            
#        print (weights)
        
    print(time.clock()-t)
    
def P(a=1, b=1, c=1, d=1):
	""" a, b, c, d == A2, A3, A4, A5
		Have to ignore the case when only a A5 paper is left.
	"""
	s = a + b + c + d
	p, x = 0.0, 0.0

	if s == 0: return 0
	if s == 1: x  = 1.0  # one paper
	
	if a > 0 : p += 1.0 * a / s * (x + P(a-1, b+1, c+1, d+1))
	if b > 0 : p += 1.0 * b / s * (x + P(a  , b-1, c+1, d+1))
	if c > 0 : p += 1.0 * c / s * (x + P(a  , b  , c-1, d+1))
	if d > 0 : p += 1.0 * d / s * (P(a  , b  , c  , d-1))
	
	#print('*', a, b, c, d, '->', p)

	print(p)


def MrDrake():
    m = [dict() for i in range(2 ** 4)]
    m[1][(1, 1, 1, 1)] = 1.0
    
    for i in range(1, len(m) - 1):
        for j in m[i]:
            n = sum(j)
            if j[0] > 0:
                q = (j[0] - 1, j[1] + 1, j[2] + 1, j[3] + 1)
                if q not in m[i + 1]: m[i + 1][q] = 0.0
                m[i + 1][q] += m[i][j] * j[0] / n
            if j[1] > 0:
                q = (j[0], j[1] - 1, j[2] + 1, j[3] + 1)
                if q not in m[i + 1]: m[i + 1][q] = 0.0
                m[i + 1][q] += m[i][j] * j[1] / n
            if j[2] > 0:
                q = (j[0], j[1], j[2] - 1, j[3] + 1)
                if q not in m[i + 1]: m[i + 1][q] = 0.0
                m[i + 1][q] += m[i][j] * j[2] / n
            if j[3] > 0:
                q = (j[0], j[1], j[2], j[3] - 1)
                if q not in m[i + 1]: m[i + 1][q] = 0.0
                m[i + 1][q] += m[i][j] * j[3] / n
    
    print (m[8][(1,0,0,0)]+m[12][(0,1,0,0)]+m[14][(0,0,1,0)])
      
            
        

        
        
                
                    
                
                    
                    
                    
    
    
    

#Monte carlo
def p151mc(n):
    
    divs={1:[1],2:[1],4:[1,2],8:[1,2,4],16:[1,2,4,8]}
    sum1Tot=0
    count=0
    
    while 1:
        count+=1
        sheets=divs[n][:]
        sum1=0
        for k in range(1,n-1):
            pick=rd.randint(0,len(sheets)-1)
            picked=sheets[pick]
            del(sheets[pick])
            if picked>1:
                sheets+=divs[picked]
#            print (k,pick,picked,divs[picked],sheets)
            if len(sheets)==1:
                sum1+=1
#        print(sum1-1)
        sum1Tot+=sum1-1
        ave=sum1Tot/count
        if not count%100000:
            print(ave)

        
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
        
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

          
            
        
        

