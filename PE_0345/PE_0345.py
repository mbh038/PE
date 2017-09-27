#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

PE_0345

Matrix Sum

Created on Mon Sep 18 05:18:38 2017

We define the Matrix Sum of a matrix as the maximum sum of matrix elements with 
each element being the only one in his row and column. For example, the Matrix 
Sum of the matrix below equals 3315 ( = 863 + 383 + 343 + 959 + 767):
    
  7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303

Find the matrix sum of:
    
    
7 53 183 439 863 497 383 563 79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805


@author: mbh
"""

from munkres import Munkres, print_matrix
import sys
import time
import random as rd

def p345(filename='pe345.txt'):
    t=time.clock()
    matrix=readMatrix(filename)
    print(time.clock()-t)
#    mProfit=costToProfit(mCost)
    mrProfit(matrix)
    print(time.clock()-t)

def readMatrix(filename='pe345.txt'):
    m=[]    
    with open(filename, 'r') as fh:
        for line in fh:
            m.append([int(x) for x in line.split(',')] ) 
        fh.close()
    return m    

def costToProfit(matrix,largeValue=1000):
    for row in matrix:
        for i in range(len(row)):
            row[i]=largeValue-row[i]
    return matrix
    
    
def transpose(m):
    mflip=[]
    for i in range(len(m)): 
        rowOrCol=[]
        for j in range(len(m)):
            rowOrCol.append(m[j][i])
        mflip.append(rowOrCol)
    return mflip

def subtractRowMins(m):      
    for row in m:
#        print(row)
        rowMin=min(row)
        for i in range(len(row)):
            row[i]-=rowMin
    return m

def subtractColMins(m):
    mCol=transpose(m)
    mCol=subtractRowMins(mCol)
    mRow=transpose(mCol)
    return mRow
    
def mrCost(matrix):
    m = Munkres()
    indexes = m.compute(matrix)
    print_matrix(matrix, msg='Lowest cost through this matrix:')
    total = 0
    for row, column in indexes:
        value = matrix[row][column]
        total += value
    print ('(%d, %d) -> %d' % (row, column, value))
    print ('total cost: %d' % total)
    
def mrProfit(matrix):
    cost_matrix = []
    for row in matrix:
        cost_row = []
        for col in row:
            cost_row += [sys.maxsize - col]
        cost_matrix += [cost_row]
    
    m = Munkres()
    indexes = m.compute(cost_matrix)
    print_matrix(matrix, msg='Highest profit through this matrix:')
    total = 0
    for row, column in indexes:
        value = matrix[row][column]
        total += value
        print ('(%d, %d) -> %d' % (row, column, value))    
    print ('total profit=%d' % total)


#Implements genetic algorithm (idea from PE user Eventhorizon)    
def p345genetic(fileName='pe345.txt'):
    
    t=time.clock()
    
    matrix=readMatrix(fileName)    
    sols=[]
    
    for i in range(40000):
        sols.append(rdsol(matrix))  #find large number of random solutions (for each row, choose columns randomly)  
    sols.sort(key=lambda x: x[0])    
    sols=sols[-400:]   #take the top 400
    
    newMax=sols[-1][0]
    gen=0
    while 1:
        gen+=1
        print("generation:",gen)
        newSols=[]
        for sol in sols:
            newSol=colSwap(matrix,sol[1])
            for solx in newSol:
                newSols.append(solx)   
        newSols.sort(key=lambda x: x[0]) 
        newSols=newSols[-400:]        
        if newSols[-1][0]==newMax:
            print(newMax)
            print(time.clock()-t)
            break
        newMax=newSols[-1][0]
        sols=newSols[:]

    
    
       
def colSwap(matrix,colList):
    sols=[]
    n=len(matrix)
    msum=0
    for k in range(n):
        msum+=matrix[k][colList[k]]
    sols.append((msum,colList))
    for i in range(n-1):
        for j in range(i+1,n):
            newSol=colList[:]
            newSol[i]=colList[j]
            newSol[j]=colList[i]
            sols.append((matrixSum(matrix,newSol),newSol))
    return sols
                   
#pick a random solution
def rdsol(matrix):    
    n=len(matrix)
    cols=list(range(n))
    rd.shuffle(cols)
    return matrixSum(matrix,cols),cols

def matrixSum(matrix,columns):
    msum=0
    for i in range(len(matrix)):
        msum+=matrix[i][columns[i]]
    return msum       

#code by other users

def drake(filename='pe345.txt'):
    matrix=readMatrix(filename)
    n = len(matrix)
    print(n)

    dp = {0:0}
    
    for row in range(n):
        z = {}
        for column in range(n):
            x = 1<<column
            print (x)
            for d in dp:
                if x&d: continue
                y = matrix[column][row] + dp[d]
                if x|d not in z or z[x|d] < y: z[x|d] = y
        dp = z
    
    print (dp[(1<<n)-1])
    
#Peter de Rivaz
def euler345():
   A="""7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805"""

   B=A.split('\n')
   print(B)
   C=[map(int,b.split()) for b in B]
   print([j for j in C])
   return
   @Memoize
   def f(A,B):
      """Maximum using rows A and columns B"""
      if len(A)==0: return 0
      return max(C[A[0]][b]+f(A[1:],B[:j]+B[j+1:]) for j,b in enumerate(B))      
   print (f(tuple(range(len(C))),tuple(range(len(C[0])))))