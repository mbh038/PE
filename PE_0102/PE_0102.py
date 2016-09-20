# -*- coding: utf-8 -*-
"""
PE_0102

Triangle Containment

Created on Wed Sep  7 15:27:02 2016
@author: mbh
"""
import math
from timeit import default_timer as timer


def p102(filename='p102_triangles.txt'):
    start=timer()
    with open(filename,'r') as file:
        data  = file.readlines()        
    coords=[[int(x) for x in line.rstrip().split(',') ] for line in data]
    triangles=[]
    for t in coords:
        triangles.append([(t[0],t[1]),(t[2],t[3]),(t[4],t[5])])
    nc=sum([contains(t) for t in triangles])
    print(nc-1)
    print('Elapsed time:',timer()-start,'s')
    
           
def contains(xy):
       
    rc=math.sqrt(2)*1000           
    xmid=0.5*(xy[0][0]+xy[1][0]) 
    ymid=0.5*(xy[0][1]+xy[1][1])
    rmid=math.sqrt(xmid**2+ymid**2)
    xray=(rc/rmid)*xmid
    yray=(rc/rmid)*ymid
        
    try:
        mray=(xy[0][1]+xy[1][1])/(xy[0][0]+xy[1][0])
    except ZeroDivisionError:
        mray=(xy[0][1]+xy[1][1])*math.inf

    m,c,x,y=[],[],[],[]
    cross=0 
    for i in [0,1]:
        try:
            m.append((xy[2][1]-xy[i][1])/(xy[2][0]-xy[i][0]))
            c.append(xy[2][1]-m[i]*xy[2][0])
            x.append(c[i]/(mray-m[i]))
        except:
            x.append(xy[i][0])
        y.append(mray*x[i])

        if x[i]>=min(xy[i][0],xy[2][0]) and x[i]<=max(xy[i][0],xy[2][0]) and y[i]>=min(xy[i][1],xy[2][1]) and y[i]<=max(xy[i][1],xy[2][1]):
            if x[i]>=min(0,xray) and x[i]<=max(0,xray) and y[i]>=min(0,yray) and y[i]<=max(0,yray):
                cross+=1
        
    return cross%2==0

 
from matplotlib import pyplot as plt   
def triplot(triangle,ray):
    
    X=[point[0] for point in triangle]
    X.append(X[0])
    Y=[point[1] for point in triangle]
    Y.append(Y[0])
#    plt.plot(X,Y)
    plt.plot(X,Y,[ray[0][0],ray[1][0]],[ray[0][1],ray[1][1]])
    plt.plot([-10,-10,10,10,-10],[10,-10,-10,10,10])
    plt.show()
    
#uses idea of cross products - all should have same sign
def p102v2(filename='p102_triangles.txt'):

    with open(filename,'r') as file:
        data  = file.readlines()        
    coords=[[int(x) for x in line.rstrip().split(',') ] for line in data]
    triangles=[]
    for t in coords:
        triangles.append([(t[0],t[1]),(t[2],t[3]),(t[4],t[5])])
        
    contains=0
    for t in triangles:
        cp0=(t[0][0]*t[1][1]-t[0][1]*t[1][0])>0
        cp1=(t[1][0]*t[2][1]-t[1][1]*t[2][0])>0
        cp2=(t[2][0]*t[0][1]-t[2][1]*t[0][0])>0
        signs=set([cp0,cp1,cp2])
        if len(signs)==1:
            contains+=1
    print(contains)
    

#neater code using cross-product idea
#FJ_Sevilla
f = open('p102_triangles.txt')
cont = 0
for line in f:
    t=[int(p) for p in line.split(",")]
    print (t)
    cont += (t[0]*t[3]-t[2]*t[1] >0) == (t[2]*t[5]-t[4]*t[3]>0) == (t[4]*t[1]-t[0]*t[5]>0)
f.close()
print(cont)