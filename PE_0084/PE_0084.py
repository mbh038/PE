# -*- coding: utf-8 -*-
"""

P_0084

Monopoly odds

A player starts on the GO square and adds the scores on two 6-sided dice to 
determine the number of squares they advance in a clockwise direction. Without 
any further rules we would expect to visit each square with equal probability: 
2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) 
changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player 
to go directly to jail, if a player rolls three consecutive doubles, they do not 
advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player 
lands on CC or CH they take a card from the top of the respective pile and, after 
following the instructions, it is returned to the bottom of the pile. There are 
sixteen cards in each pile, but for the purpose of this problem we are only 
concerned with cards that order a movement; any instruction not concerned with 
movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL

Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. 
That is, the probability of finishing at that square after a roll. For this reason 
it should be clear that, with the exception of G2J for which the probability of 
finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 
request a movement to another square, and it is the final square that the player 
finishes at on each roll that we are interested in. We shall make no distinction 
between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule 
about requiring a double to "get out of jail", assuming that they pay to get out 
on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can 
concatenate these two-digit numbers to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are 
JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So 
these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit 
modal string.

Created on Fri Sep  2 03:59:36 2016
@author: mbh
"""
import random as rd
import matplotlib.pyplot as plt
import numpy as np
import itertools as it
import math
from operator import itemgetter
        
def monopoly(n,sides):
    
    """Monte Carlo method to find three most commonly visited squares"""
        
    chstack=[x for x in range(1,17)]
    ccstack=[x for x in range(1,17)]
    rd.shuffle(chstack)
    rd.shuffle(ccstack)
    ch=it.cycle(chstack)
    cc=it.cycle(ccstack)

    sqsc={k:0 for k in range(40)}    
    CC=[2,17,33]
    CH=[7,22,36]    
    throws=dice(sides)
    
    square=0
    doubles=[0,0,0]
    i=1
    
    while i <= n:
        i+=1
        throw=throws[rd.randint(0,len(throws)-1)]

        doubles[i%3]=(throw[0]==throw[1])
        if sum(doubles)==3:
            square=10
            sqsc[square]+=1
            doubles=[0,0,0]
            continue

        square=square+sum(throw)
        square=square%40

        if square in CH:
            square=chcard(square,next(ch))

        if square in CC:
            square=cccard(square,next(cc))

        if square == 30:
            square=10
        
        sqsc[square]+=1 
        
    sqsc={k:v/n for k,v in sqsc.items()}
    top10=[str(x[0]) for x in (sorted(sqsc.items(), key=itemgetter(1)))[-10:][::-1]]
    print(top10)
    for i in range(3):
        if len(top10[i])==1:
            top10[i]='0'+top10[i]    
    print(top10[0]+top10[1]+top10[2])  
    bar_width = 0.65
    opacity = 0.4
    plt.bar([k for k,v in sqsc.items()],[v for k,v in sqsc.items()],bar_width,
            alpha=opacity)    

def dice(sides):   
    throws=[]
    for throw in it.product(range(1,sides+1),repeat=2):
        throws.append(throw)
    return throws
            
def chcard(sq,cc):
    R=[5,15,25,35,math.inf]
    Rdic={0:R[0],1:R[1],2:R[2],3:R[3],4:R[0]}
    U=[12,28,math.inf]
    Udic={0:U[0],1:U[1],2:U[0]}
    cards={
           1:sq,
           2:sq,
           3:sq,
           4:sq,
           5:sq,
           6:sq,
           7:0, #Go
           8:10,# Jail
           9:11,#C1
           10:24,#E3
           11:39,#H2
           12:5,#R1
           13:Rdic[next(i for i,v in enumerate(R) if v > sq)],
           14:Rdic[next(i for i,v in enumerate(R) if v > sq)],
           15:Udic[next(i for i,v in enumerate(U) if v > sq)],
           16:(sq-3)%40
           }
    return cards[cc]
       

def cccard(sq,cc):    
    if cc in [1,2]: 
        return [0,0,10][cc]
    else:
        return sq
        
##############################################################################
#Try to solve as Markov chain problem
        
import numpy as np



