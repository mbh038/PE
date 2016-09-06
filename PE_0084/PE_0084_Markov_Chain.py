# -*- coding: utf-8 -*-
"""

PE_0084 (using Markov Chain)

Monopoly Odds using Markov Chain

Created on Sun Sep  4 11:00:43 2016
@author: mbh
"""
import numpy as np
import random as rd
import itertools as it
import math
import matplotlib.pyplot as plt
from operator import itemgetter
from timeit import default_timer as timer

#Snakes and  Ladders
def Asl():
    """find transition matrix for snakes and ladders"""
    """"A(i,j) is probsbility of going from square j to square i"""
    A=np.zeros([101,101])
    print(np.shape(A))    
    
    c={1:38,4:14,9:31,16:6,21:42,28:84,36:44,47:26,49:11,51:67,56:53,62:19,64:60,
       71:91,80:100,87:24,93:73,95:75,98:78}

    for i in range(0,101):
        js=[]
        for j in range(i+1,i+7):
            js.append(j)
            if j<=100:
                A[j][i]=1/6
            else:
                A[i][i]+=1/6
            if j in c:
                A[j][i]-=(1/6)
                A[c[j]][i]+=(1/6)   
    return A
    
def sl(n):
    """find steady state vector for s & l"""
    x0=np.zeros([101,1])
    x0[0][0]=1
    A=Asl()
    x=x0
    p50=[]
    p70=[]
    p100=[]
    for i in range(n):
        x=np.dot(A,x)
        p50.append(x[50])
        p70.append(x[70])
        p100.append(x[100])
#    plt.plot([i for i in range(100)],p50[0:100],[i for i in range(100)],p70[0:100])
    plt.show()
    plt.plot([i for i in range(n)],p100[0:n])
    plt.show()
    plt.plot([i for i in range(n-1)],[p100[i+1]-p100[i] for i in range(n-1)])
    plt.show()


#Monopoly
def ss(sides,turns):
    """find steady state vector for Monopoly"""
    start=timer()
    A=Am(sides)
    x0=np.zeros([40,1])
    x0[0][0]=1
    x=x0
    i=0
    while i <=turns:
        i+=1        
        x=np.dot(A,x)
    xdic={k:x[k][0] for k in range(40)}
#    print(xdic)
    top10=[str(x[0]) for x in (sorted(xdic.items(), key=itemgetter(1)))[-10:][::-1]]
    print (top10)
    print('Elapsed time:',timer()-start,'s')
    
def Am(sides):
    """create the transition matrix"""
    A=A=np.zeros([40,40])
    
    CC=[2,17,33]
    CH=[7,22,36]    
    pscores=dice(sides)
        
    for f in range(40):
        for score in range(2,2*sides+1):
            t=(f+score)%40
            if t in CH:
                for k,v in chcard(t).items():
#                    print (f,t,k,v)
                    A[k,f]+=pscores[score]*v
            elif t in CC:
                for k,v in cccard(t).items():
                    A[k,f]+=pscores[score]*v
            elif t==31:
                t=10
                A[t,f]+=pscores[score]           
            else:
                A[t,f]+=pscores[score]            
    return A
    
def dice(n): 
    """returns dict of the probabilities of the possible scores for 2 n sided dice"""
    scores={k:0 for k in range(2,2*n+1)}
    for throw in it.product(range(1,n+1),repeat=2):
        scores[sum(throw)]+=1/n**2        
    return scores
    
def chcard(sq):
    R=[15,25,35,math.inf]
    Rdic={0:R[0],1:R[1],2:R[2],3:R[0]}
    Rvals={False:1/8,True:0}
    U=[12,28,math.inf]
    Udic={0:U[0],1:U[1],2:U[0]}    
    ch36={False:0,True:1/8}
       
    dest={sq:6/16,
          0:1/16,
          10:1/16,
          11:1/16,
          24:1/16,
          39:1/16,
          5:1/16+ch36[sq==36],
          Rdic[next(i for i,v in enumerate(R) if v > sq)]:Rvals[sq==36],
          Udic[next(i for i,v in enumerate(U) if v > sq)]:1/16,
          (sq-3)%40:1/16}
    return dest
    
def cccard(sq):
    dest={sq:7/8,0:1/16,10:1/16} 
    return dest        
    
