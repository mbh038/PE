# -*- coding: utf-8 -*-
"""

PE_0096

Su Doku

Created on Fri Jul 29 17:06:41 2016
@author: mbh
"""

import copy
from timeit import default_timer as timer 

def main1(filename):
    start=timer()
    grids=readGrids(filename)
    solved=0
    tl3=0
    
    for grid in grids:
        # first the easy wins - fill in all singles and hidden singles
        grid,changes,remaining=singles(grid) 
        # for the remainder, follow through consequences of all candidates.
        #  if only one candidate avoids invalid consequences, insert that
        # candidate.         
        while remaining>0:
            for i in range(9):
                for j in range(9):
                    grid,valid=insert(grid,i,j)
                    results={'T':[],'F':[]}
                    for result in valid:
                        if result[1]==True:
                            results['T'].append(result[0])
                    if len(results['T'])==1:
                        grid[i][j]=str(results['T'][0])                        
                        grid,changes,remaining=singles(grid)                       
                    
        if remaining==0:
            solved+=1   
            
        tl3+=100*int(grid[0][0]) +10*int(grid[0][1])+int(grid[0][2])
    print (tl3)
    print (solved,'puzzles solved') # if <50, more strategies required!
    print('Elapsed time: ',timer()-start,'s')

def singles(grid):
    """fill in all singles and hidden singles"""
    changes=1
    while changes>0: 
        grid,changes,remaining=fillHiddenSingles(grid)
        grid,changes,remaining=fillSingles(grid)
    return grid,changes,remaining
    
def insert(grid,r,c):
    """
    return original grid and a list 'valid' of tuples, (candidate value, Boolean)
    where Boolean is True if insertion of this candidate leads to a valid grid, Falise
    if not
    """
    valid=[]        
    oldgrid=copy.deepcopy(grid)
    if grid[r][c]=='0':

        cs=candidates(grid)
        for i in range(len(cs[(r,c)])):
            flag=False
            grid[r][c]=str(list(cs[(r,c)])[i])
            grid,changes,remaining=singles(grid)
            if checkValid(grid):
                flag=True          
            else:
                grid=copy.deepcopy(oldgrid)
            valid.append((list(cs[(r,c)])[i],flag))
    return oldgrid,valid
                   
def checkValid(grid):
    """Returns True if grid is valid, False if not. grid need not be complete"""
    blocksList=[]
    for i in range(9):
        blocksList.append([grid[i][j] for j in range(9) if grid[i][j]!='0'])
        if len(set(blocksList[-1]))<len(blocksList[-1]):
            return False
        blocksList.append([grid[j][i] for j in range(9) if grid[j][i]!='0'])
        if len(set(blocksList[-1]))<len(blocksList[-1]):
            return False
    for i in range (3):
        for j in range (3):
            blocksList.append([grid[p][q] for p in range(9) for q in range(9) if grid[p][q]!='0' and p//3==i and q//3==j])
            if len(set(blocksList[-1]))<len(blocksList[-1]):
                return False
    return True


def candidates(grid):
    """returns dictionary of candidates for unfilled squares in grid"""
    candidates={}    
    for r in range(len(grid)):        
        for c in range(len(grid[r])): 
            options=set(range(1,10))
            if grid[r][c]=='0':
                options=options.difference(readRow(grid,r))
                options=options.difference(readColumn(grid,c))
                options=options.difference(readSquare(grid,r,c))
                candidates[(r,c)]=options
    return candidates


def fillSingles(grid):
    """fill squares in grid for which there is a single candidate"""
    newgrid=[['0']*9]*9
    changes=0    
    while newgrid!=grid:
        newgrid=copy.deepcopy(grid)
        cs=candidates(grid)
        for key, value in cs.items():
            if len(value)==1:
                changes+=1
                grid[key[0]][key[1]]=str(value.pop())        
    return grid,changes,len(cs)
                

def fillHiddenSingles(grid):
    """
    fill hidden singles squares - squares with multiple candidates, but 
    where one candidate is unique in that block (r,c or region) to that square
    """
    newgrid=[['0']*9]*9
    changes=0 
    while newgrid!=grid:
        newgrid=copy.deepcopy(grid)
        cs=candidates(grid)
        blocksList=blocks(cs)
        for block in blocksList:
            digits={x:[k for k,v in block.items() if x in v] for x in range(1,10)}
            hiddenSingles=[(v[0],k) for k,v in digits.items() if len(v)==1]
            for square in hiddenSingles:
                changes+=1
                grid[square[0][0]][square[0][1]]=str(square[1])
    return grid,changes,len(cs)
               
def blocks(squares):
    """
    returns list of dictionaries, one for each r,c or 3x3 block, where each list 
    contains the candidates for the squares in that block
    Input is 'squares', the dict of candidates for the whole puzzle as generated by 
    candidates().
    """
    blocksList=[]
    for i in range(9):
        blocksList.append({k:v for k,v in squares.items() if k[0]==i })
        blocksList.append({k:v for k,v in squares.items() if k[1]==i })
    for i in range (3):
        for j in range (3):
            blocksList.append({k:v for k,v in squares.items() if k[0]//3==i and k[1]//3==j})
    return blocksList
    
def readRow(grid, row):
    return set([int(x) for x in grid[row]])
    
def readColumn(grid,column):
    return set([int (grid[row][column]) for row in range(9)])
    
def readSquare(grid,row,column):   
    r=row-row%3
    c=column-column%3    
    square=[int(grid[x][y])for x in range(r,r+3) for y in range(c,c+3)]    
    return set(square)
    
def readGrids(filename):    
    with open(filename) as f:
        grids=[]
        for line in f:
            if ('Grid ') in line:               
                count=0
                grids.append([['0']*9]*9)
                while count<9:                    
                    grids[-1][count]=[x for x in f.readline().rstrip()]
                    count+=1
        return (grids)
        
#from collections import Counter
#def nakedPairs(grid):
#    newgrid=[['0']*9]*9
#    changes=0 
#    while newgrid!=grid:
#        newgrid=copy.deepcopy(grid)
#        cs=candidates(grid)
#        blocksList=blocks(cs)
##        print (blocksList)
#        blocknum=0
#        for block in blocksList:
#            blocknum+=1
#            pairs=[(k,v) for k,v in block.items() if len(v)==2]
#            print(blocknum,pairs)
#            for x in pairs:
#                if pairs.count(x[1])==2:
#                    print (blocknum,x)
#            print ([x for x in pairs if pairs.count(x) ==2 ])
                    

        
     

#def fillGrid(grid):
#    newgrid=[['0']*9]*9
#    changes=0
#    remaining=0
#    while newgrid!=grid:
#        newgrid=copy.deepcopy(grid)
#        remaining=0
#        for r in range(9):        
#            for c in range(9):
#                options=set(range(1,10))
#                if grid[r][c]=='0':
#                    options=options.difference(readRow(grid,r))
#                    print(readRow(grid,r))
#                    options=options.difference(readColumn(grid,c))
#                    options=options.difference(readSquare(grid,r,c))
##                    print (r,c,options)
#                    if len(options)==1:
#                        changes+=1
#                        grid[r][c]=str(options.pop())
#                    remaining+=1
#    return (grid,changes,remaining)



#def readGrid(n):   
#    with open("p096_sudoku.txt") as f:
#        for line in f:
#            if ('Grid '+n) in line:
#                grid=[]
#                count=0
#                while count<9:
#                    count+=1
#                    grid.append([x for x in f.readline().rstrip()])
#                return (grid)
                


