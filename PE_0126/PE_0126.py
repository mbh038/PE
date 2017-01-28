# -*- coding: utf-8 -*-
"""

PE_0126

Created on Thu Jan  5 05:23:10 2017
@author: mbh
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pylab



import numpy as np
import itertools as it
import queue
import time


def AL(a,b,c):
    A=2*(a*b+a*c+b*c)
    L=4*(a+b+c)
    return A,L,A/L
#a,b,c are cuboid side lengths, n is layer
def abc(a,b,c,n):
    """area,length and n are all positive integers"""
    return 2*(a*b+a*c+b*c+2*(n-1)*(a+b+c)+2*(n-2)*(n-1))
    
#A is total surface ara of cuboid, L is total edge length, n is layer
def ALn(A,L,n):
    """area,length and L are all positive integers"""
    return A+(n-1)*(L+4*(n-2))
    
def ALn2(A,L,n):
    """area,length and L are all positive integers"""
    if n==1:
        return A
    if n==2:
        return A+L
    return A+(n-1)*L+8

def LtoA(L,Amin,Amax):
    if L%4:
        return {}
    L//=4
    Az=set()
    for a in range(1,L-1):
        for b in range(1,L-a):
            c=L-a-b
            A=2*(a*(b+c)+b*c)
#            print(a,b,c,A)
            Az.add(A)

    Az= np.array(sorted(list(Az)))
    Az=Az[Az>=Amin]
    Az=Az[Az<=Amax]
    return Az
    
def Aexplore(Lmax,f):
    x=[]
    y=[]
    for L in range(12,Lmax+1,4):
        Az=LtoA(L,1,Lmax-6)
#        print(L,len(Az),len(set(Az)))
        y.extend([x for x in Az])
        x.extend([L]*len(Az))
    print([(L,A) for L,A in zip(x[:10],y[:10])])
    print([(L,A) for L,A in zip(x[-65:],y[-65:])])
    plt.plot(x,y,'ro')
    plt.axis([0, int(f*max(x)), 0, max(y)+10])
    plt.xlabel('L')
    plt.ylabel('A')
    plt.show()
        
    
#Lmax cannot be greater than A+6
def AtoL(A,Lmin,Lmax):
    if A%2:
        return []
    Lz=[]
    error_count=0
    for x in range (1,(A-1)//4+1):
        for y in range (1,(A//2-x)//(x+1)+1):
            z=((A//2)-x*y)//(x+y)
            if 2*(x*y+x*z+y*z) == A:
                Lz.append(tuple((sorted([x,y,z]))))
            if 2*(x*y+x*z+y*z) !=A:
                error_count+=1
#                print('error',x,y,z,2*(x*y+x*z+y*z))
    print (error_count,'errors')
    print (len(Lz),'solutions')
    print ('xmax',max([x[0] for x in Lz]),'xmin',min([x[0] for x in Lz]))
    print ('ymax',max([y[1] for y in Lz]),'ymin',min([y[1] for y in Lz]))
    print ('zmax',max([z[2] for z in Lz]),'ymin',min([z[2] for z in Lz]))
    print ('Lmax',max([4*sum(x) for x in Lz]),'Lmin',min([4*sum(x) for x in Lz]))
    return Lz            
    
def series(a,b,c,terms):
    return [abc(a,b,c,x) for x in range(1,terms+1)]
    
def stomax(area,length,maxval):
    s=[]
    i=1
    while 1:
        term=abc(area,length,i)
        if term>maxval:
            break
        s.append(term)
        i+=1
    return s
        
def bounds(A,L,target):
#    D=((L-1)**2+target-2*A)**.5
    D=pow((pow(L-1,2)+target-2*A),0.5)
#    root1=(-L+3-D)/2
    root2=(-L+3+D)//2
    return int(root2)
    
def srec(a,b,c,L,memo={}):
    if L<=2:
        return 2*(a*(b+c)+b*c+2*(L-1)*(a+b+c+L-2))
    try:
        return memo[L]
    except KeyError:
        result=2*srec(a,b,c,L-1,memo)-srec(a,b,c,L-2,memo)+8
        memo[L]=result
        return result

def look(dmax,searchval):
    abcvals=[x for x in range(1,dmax+1)]
    q=queue.PriorityQueue()
    for a,b,c in it.combinations_with_replacement(abcvals,3):
        area=a*(b+c)+b*c
        length=a+b+c        
        q.put((abc(area,length,1),abc(area,length,2),(a,b,c),stomax(area,length,searchval),bounds(area,length,searchval)))
    while 1:
        if q.empty():
            break
        print(q.get())

def test(a,b,c):
    terms=10
    t=time.clock()  
    for i in range(100):
        s1=[abc(a,b,c,x) for x in range(1,terms+1)]
    print(s1,time.clock()-t)
    t=time.clock()  
    for i in range(100000):
        s2=[srec(a,b,c,x) for x in range(1,terms+1)]
    print(s2,time.clock()-t)
    
    
def C(nseek):
    
    t=time.clock()
    
    vals={}
    found=set()
    Lmax=25000
    Arange=25000
    Nrange=250
    nval=[]
    count=0
    for n in range(1,Nrange+1):
        Lrange=Lmax
        if n>5 and n<=10:
            Lrange=Lmax//5
        if n>10:
            Lrange=Lmax//10
        for L in range (12,Lrange+4,4):
            Az=LtoA(L,2,Arange+4)
    #        print (min(Az))
            for A in Az:
    #            for n in range(1,Nrange+1):
                count+=1
                val=A+(n-1)*(L+4*(n-2))
#                if val==2056:
#                    nval.append((L,A,n))
#                    print(count,L,A,n)
                vals[val]=vals.get(val,0)+1
                if vals[val]==nseek:
                    found.add(val)
                if vals[val]>nseek:
                    found.discard(val)
    print(min([val for val in found]),Lrange,Arange,Nrange)
        

    print(time.clock()-t)
    return nval


    
def Cseek(nseek):
    
    t=time.clock()
    
    coords=[]
    found=set()
    Lrange=nseek+6
    Nrange=100
    for L in range (12,nseek+8,4):
        for A in LtoA(L,0,nseek+2):
            val=0
            n=1
            while val<nseek:
                val=A+(n-1)*(L+4*(n-2))
                if val==nseek:
                    coords.append((L,A,n))
                n+=1
    print(time.clock()-t)
    L=[x[0] for x in coords]
    A=[x[1] for x in coords]
    n=[x[2] for x in coords]
    AL=[A[i]/L[i] for i in range(len(L))]
    
#2D  plots
    plt.plot(A,n,'ro')
    plt.xlabel('A')
    plt.ylabel('n')
    plt.show()
    plt.plot(L,n,'ro')
    plt.xlabel('L')
    plt.ylabel('n')
    plt.show()
    plt.plot(L,A,'bo')
    plt.xlabel('L')
    plt.ylabel('A')    
    plt.show()
    

# a 3D plot
    fig = pylab.figure()
    ax = Axes3D(fig)   
    ax.scatter(L, A, n)    
    ax.set_xlabel('L')
    ax.set_ylabel('A')
    ax.set_zlabel('n')
    plt.show()
    
#more 2D
    plt.plot(AL,n,'ro')
    plt.xlabel('AL')
    plt.ylabel('n')
    plt.show()


    print ('Lmax:',max(L),'Lmin:',min(L))
    print ('Amax:',max(A),'Amin:',min(A))
    print ('nmax:',max(n),'nmin:',min(n))
    print(len(coords))
    return coords

    
def prime_factors(n):
    """returns the prime factors of n"""    
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors   